import pytest
from phantom.core.scope import UnauthorizedTargetError, expand_targets, is_authorized_target


def test_loopback_and_localhost_are_authorized():
    assert is_authorized_target("127.0.0.1") is True
    assert is_authorized_target("localhost") is True


def test_private_network_is_authorized():
    assert is_authorized_target("192.168.1.10") is True
    assert is_authorized_target("10.0.0.5") is True


def test_public_ip_is_blocked_by_default():
    assert is_authorized_target("8.8.8.8") is False


def test_public_ip_allowed_only_when_explicit():
    assert is_authorized_target("8.8.8.8", allow_public=True) is True


def test_invalid_host_is_rejected():
    assert is_authorized_target("not-a-real-host.invalid") is False


def test_expand_targets_private_cidr():
    hosts = expand_targets("192.168.1.0/29")
    assert len(hosts) == 6
    assert hosts[0] == "192.168.1.1"
    assert hosts[-1] == "192.168.1.6"


def test_expand_targets_blocks_public_cidr():
    with pytest.raises(UnauthorizedTargetError):
        expand_targets("8.8.8.0/29")
