import pytest

from validkit.email import is_valid_email


def test_valid_basic_email():
    assert is_valid_email("user@example.com") is True


def test_valid_email_with_subdomain():
    assert is_valid_email("user@sub.example.com") is True


def test_invalid_missing_domain():
    assert is_valid_email("user@") is False


def test_invalid_missing_local_part():
    assert is_valid_email("@example.com") is False


def test_invalid_no_at_sign():
    assert is_valid_email("user example.com") is False


def test_invalid_empty_string():
    assert is_valid_email("") is False


def test_invalid_whitespace_in_local_part():
    assert is_valid_email("user name@example.com") is False


def test_exactly_max_length_is_accepted():
    candidate = "a" * 64 + "@" + "b" * 185 + ".com"
    assert len(candidate) == 254
    assert is_valid_email(candidate) is True


def test_over_max_length_returns_false():
    candidate = "a" * 64 + "@" + "b" * 186 + ".com"
    assert len(candidate) > 254
    assert is_valid_email(candidate) is False


@pytest.mark.parametrize("bad", [None, 123, 4.2, ["user@example.com"], b"user@example.com"])
def test_wrong_type_raises_type_error(bad):
    with pytest.raises(TypeError):
        is_valid_email(bad)
