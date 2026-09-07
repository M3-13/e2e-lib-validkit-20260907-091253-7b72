import pytest

from validkit.numeric import clamp


def test_value_within_range_unchanged():
    assert clamp(5, 1, 10) == 5


def test_value_below_range_clamped_to_low():
    assert clamp(-3, 0, 10) == 0


def test_value_above_range_clamped_to_high():
    assert clamp(15, 0, 10) == 10


def test_low_boundary_returns_low():
    assert clamp(0, 0, 10) == 0


def test_high_boundary_returns_high():
    assert clamp(10, 0, 10) == 10


def test_low_equals_high_returns_that_value():
    assert clamp(7, 5, 5) == 5


def test_float_input_preserves_float_type():
    result = clamp(5.0, 1, 10)
    assert result == 5.0
    assert type(result) is float


def test_float_clamped_to_int_bound_preserves_float_type():
    result = clamp(-3.5, 0, 10)
    assert result == 0.0
    assert type(result) is float


def test_int_input_preserves_int_type():
    result = clamp(5, 1, 10)
    assert type(result) is int


def test_negative_range():
    assert clamp(-50, -100, -10) == -50
    assert clamp(-200, -100, -10) == -100
    assert clamp(-5, -100, -10) == -10


def test_low_greater_than_high_raises_value_error():
    with pytest.raises(ValueError):
        clamp(5, 10, 1)


def test_low_greater_than_high_error_message_has_no_input_value():
    with pytest.raises(ValueError) as exc_info:
        clamp(42, 10, 1)
    assert "42" not in str(exc_info.value)
