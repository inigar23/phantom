import socket

from phantom.core.scope import UnauthorizedTargetError, is_authorized_target


def is_port_open(host: str, port: int, timeout: float = 1.0) -> bool:
    """Check whether a single TCP port is open on the target host."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            return sock.connect_ex((host, port)) == 0
    except (socket.gaierror, OSError):
        return False


def scan_ports(
    host: str,
    ports: list[int],
    timeout: float = 1.0,
    allow_public: bool = False,
) -> list[int]:
    """Scan a list of TCP ports on an authorized host and return open ports."""
    if not is_authorized_target(host, allow_public=allow_public):
        raise UnauthorizedTargetError(
            f"Target '{host}' is outside authorized local/private scope."
        )

    open_ports: list[int] = []
    for port in ports:
        if is_port_open(host, port, timeout):
            open_ports.append(port)
    return open_ports


if __name__ == "__main__":
    common_ports = [21, 22, 80, 135, 443, 445, 3306, 8080, 8090, 59999]
    found = scan_ports("127.0.0.1", common_ports)
    print(f"Open ports on 127.0.0.1: {found}")
    print("Invalid host test:", is_port_open("not-a-real-host.invalid", 80))
