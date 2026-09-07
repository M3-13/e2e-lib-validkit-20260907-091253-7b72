import pytest

from validkit.isbn import is_valid_isbn13


def test_valid_isbn13_returns_true():
    assert is_valid_isbn13("9780306406157") is True


def test_wrong_check_digit_returns_false():
    assert is_valid_isbn13("9780306406158") is False


def test_too_short_returns_false():
    assert is_valid_isbn13("978030640615") is False


def test_too_long_returns_false():
    assert is_valid_isbn13("97803064061570") is False


def test_non_digit_character_returns_false():
    assert is_valid_isbn13("978030640615X") is False


def test_other_valid_isbn_returns_true():
    assert is_valid_isbn13("9783161484100") is True


def test_wrong_type_raises_type_error():
    with pytest.raises(TypeError):
        is_valid_isbn13(None)


def test_wrong_type_message_does_not_leak_input():
    with pytest.raises(TypeError) as exc_info:
        is_valid_isbn13(None)
    assert "None" not in str(exc_info.value)
