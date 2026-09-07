import pytest

from validkit.secret import mask_secret


def test_mask_secret_keeps_last_four_characters():
    assert mask_secret("hunter2secret", keep=4) == "*********cret"


def test_mask_secret_keep_zero_masks_fully():
    assert mask_secret("hunter2secret", keep=0) == "*" * len("hunter2secret")


def test_mask_secret_keep_greater_or_equal_to_length_masks_fully():
    text = "hunter2secret"
    assert mask_secret(text, keep=len(text)) == "*" * len(text)
    assert mask_secret(text, keep=len(text) + 5) == "*" * len(text)


def test_mask_secret_empty_text():
    assert mask_secret("", keep=4) == ""
    assert mask_secret("", keep=0) == ""


def test_mask_secret_default_keep_is_four():
    assert mask_secret("hunter2secret") == "*********cret"


def test_mask_secret_negative_keep_raises_value_error():
    with pytest.raises(ValueError):
        mask_secret("hunter2secret", keep=-1)


def test_mask_secret_negative_keep_error_message_hides_secret():
    with pytest.raises(ValueError) as excinfo:
        mask_secret("hunter2secret", keep=-1)
    assert "hunter2secret" not in str(excinfo.value)


def test_mask_secret_non_string_text_raises_type_error():
    with pytest.raises(TypeError):
        mask_secret(12345)


def test_mask_secret_non_int_keep_raises_type_error():
    with pytest.raises(TypeError):
        mask_secret("hunter2secret", keep="4")


def test_mask_secret_type_error_message_hides_input():
    with pytest.raises(TypeError) as excinfo:
        mask_secret("hunter2secret", keep="4")
    assert "hunter2secret" not in str(excinfo.value)
