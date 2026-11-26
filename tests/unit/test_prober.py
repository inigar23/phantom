import socket
import pytest
from phantom.core.scope import UnauthorizedTargetError
from phantom.modules.recon.prober import is_port_open, scan_ports


def test_open_port_detected():
    """Verify is_port_open returns True for an active listening port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(("127.0.0.1", 0))
        server.listen(1)
        open_port = server.getsockname()[1]

        assert is_port_open("127.0.0.1", open_port) is True


def test_invalid_host_returns_false():
    """Verify invalid hostnames fail safely without crashing."""
    assert is_port_open("not-a-real-host.invalid", 80) is False


def test_scan_ports_finds_only_open_ports():
    """Verify scan_ports returns only the open port from a mixed list."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(("127.0.0.1", 0))
        server.listen(1)
        open_port = server.getsockname()[1]

        results = scan_ports("127.0.0.1", [open_port, 59998])
        assert results == [open_port]


def test_scan_ports_blocks_public_ip():
    """Verify scan_ports refuses to scan public IPs by default."""
    with pytest.raises(UnauthorizedTargetError):
        scan_ports("8.8.8.8", [80])