import pytest

from validkit.iban import is_valid_iban


def test_valid_german_iban():
    assert is_valid_iban("DE89370400440532013000") is True


def test_valid_foreign_ibans():
    assert is_valid_iban("GB82WEST12345698765432") is True
    assert is_valid_iban("AT611904300234573201") is True


def test_wrong_check_digit():
    assert is_valid_iban("DE89370400440532013001") is False


def test_unknown_country_code():
    assert is_valid_iban("ZZ89370400440532013000") is False


def test_length_mismatch_for_country():
    assert is_valid_iban("DE8937040044053201") is False


def test_input_longer_than_34_chars():
    assert is_valid_iban("DE" + "0" * 40) is False


def test_boundary_34_chars_does_not_raise():
    assert is_valid_iban("A" * 34) is False


def test_non_alphanumeric_characters():
    assert is_valid_iban("DE89 3704 0044 0532 0130 00") is False


def test_empty_string():
    assert is_valid_iban("") is False


def test_wrong_type_raises_typeerror():
    with pytest.raises(TypeError):
        is_valid_iban(None)  # type: ignore[arg-type]


def test_typeerror_message_hides_input():
    with pytest.raises(TypeError) as exc:
        is_valid_iban(12345)  # type: ignore[arg-type]
    assert "12345" not in str(exc.value)
