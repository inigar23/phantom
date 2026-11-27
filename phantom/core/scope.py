"""Target authorization and scope validation guardrails."""

import ipaddress
import socket


class UnauthorizedTargetError(ValueError):
    """Raised when a scan targets an IP or host outside the authorized scope."""


def is_authorized_target(host: str, allow_public: bool = False) -> bool:
    """Return True if host is local/private, or if public scanning is explicitly enabled."""
    try:
        resolved_ip = socket.gethostbyname(host)
        ip_obj = ipaddress.ip_address(resolved_ip)
    except (socket.gaierror, ValueError):
        return False

    if allow_public:
        return True

    return ip_obj.is_loopback or ip_obj.is_private


def expand_targets(target: str, allow_public: bool = False) -> list[str]:
    """Expand a single host/IP or CIDR subnet into authorized target IPs/hosts."""
    if "/" in target:
        try:
            network = ipaddress.ip_network(target, strict=False)
        except ValueError as exc:
            raise UnauthorizedTargetError(f"Invalid CIDR target: '{target}'") from exc

        if not allow_public and not (network.is_loopback or network.is_private):
            raise UnauthorizedTargetError(
                f"Subnet '{target}' is outside authorized local/private scope."
            )

        if network.num_addresses == 1:
            return [str(network.network_address)]
        return [str(ip) for ip in network.hosts()]

    if not is_authorized_target(target, allow_public=allow_public):
        raise UnauthorizedTargetError(
            f"Target '{target}' is outside authorized local/private scope."
        )
    return [target]
