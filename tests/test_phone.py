import pytest

from validkit.phone import normalize_phone


def test_normal_international_german():
    assert normalize_phone("+49 170 1234567", country_code="DE") == "+491701234567"


def test_normal_national_with_trunk_prefix():
    assert normalize_phone("0170 1234567", country_code="DE") == "+491701234567"


def test_normal_national_without_trunk_prefix():
    assert normalize_phone("170 1234567", country_code="DE") == "+491701234567"


def test_normal_already_e164_is_idempotent():
    assert normalize_phone("+491701234567", country_code="DE") == "+491701234567"


def test_normal_strips_formatting_characters():
    assert normalize_phone("+49 (170) 123-4567", country_code="DE") == "+491701234567"


def test_normal_lowercase_country_code():
    assert normalize_phone("0170 1234567", country_code="de") == "+491701234567"


def test_empty_input_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("", country_code="DE")


def test_whitespace_only_input_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("   ", country_code="DE")


def test_no_digits_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("abc-def", country_code="DE")


def test_too_short_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("1", country_code="DE")


def test_too_long_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("0170 1234567890123456789", country_code="DE")


def test_unsupported_country_code_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("0170 1234567", country_code="ZZ")


def test_empty_country_code_raises_value_error():
    with pytest.raises(ValueError):
        normalize_phone("0170 1234567", country_code="")


def test_non_string_text_raises_type_error():
    with pytest.raises(TypeError):
        normalize_phone(491701234567, country_code="DE")


def test_none_text_raises_type_error():
    with pytest.raises(TypeError):
        normalize_phone(None, country_code="DE")


def test_non_string_country_code_raises_type_error():
    with pytest.raises(TypeError):
        normalize_phone("0170 1234567", country_code=49)


def test_value_error_message_does_not_contain_input_digits():
    with pytest.raises(ValueError) as excinfo:
        normalize_phone("+49 170 1234567890123456789", country_code="DE")
    message = str(excinfo.value)
    assert not any(ch.isdigit() for ch in message)


def test_type_error_message_does_not_contain_input():
    with pytest.raises(TypeError) as excinfo:
        normalize_phone("+49 170 1234567", country_code=49)
    message = str(excinfo.value)
    assert "491701234567" not in message
