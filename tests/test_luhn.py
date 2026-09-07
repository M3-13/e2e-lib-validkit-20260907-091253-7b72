import pytest

from validkit import luhn_check


def test_valid_number_returns_true():
    assert luhn_check("79927398713") is True


def test_changed_digit_returns_false():
    assert luhn_check("79927398712") is False


def test_spaces_are_tolerated():
    assert luhn_check("7992 7398 713") is True


def test_hyphens_are_tolerated():
    assert luhn_check("7992-7398-713") is True


def test_mixed_spaces_and_hyphens_are_tolerated():
    assert luhn_check("7 992-7398-7 13") is True


def test_non_digit_returns_false():
    assert luhn_check("7992a7398b713") is False


def test_empty_string_returns_false():
    assert luhn_check("") is False


def test_whitespace_only_returns_false():
    assert luhn_check("   - - ") is False


def test_none_raises_type_error():
    with pytest.raises(TypeError):
        luhn_check(None)


def test_non_string_raises_type_error():
    with pytest.raises(TypeError):
        luhn_check(79927398713)


def test_type_error_message_does_not_leak_input():
    with pytest.raises(TypeError) as exc_info:
        luhn_check(79927398713)
    assert "79927398713" not in str(exc_info.value)
