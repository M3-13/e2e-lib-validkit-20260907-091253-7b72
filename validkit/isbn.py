def is_valid_isbn13(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("is_valid_isbn13 expects a string argument")
    if len(text) > 13:
        return False
    if len(text) != 13 or not text.isascii() or not text.isdigit():
        return False
    total = 0
    for index in range(12):
        total += int(text[index]) * (1 if index % 2 == 0 else 3)
    check_digit = (10 - total % 10) % 10
    return check_digit == int(text[12])
