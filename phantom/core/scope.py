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
