def clamp(value: int | float, low: int | float, high: int | float) -> int | float:
    """Begrenzt ``value`` auf den Bereich [low, high] und erhält den numerischen Typ."""

    if low > high:
        raise ValueError("low must not be greater than high")

    result = min(max(value, low), high)
    if isinstance(value, int):
        return int(result)
    return float(result)
