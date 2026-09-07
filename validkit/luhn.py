def luhn_check(digits: str) -> bool:
    if not isinstance(digits, str):
        raise TypeError("luhn_check expects a string of digits")
    cleaned = digits.replace(" ", "").replace("-", "")
    if not cleaned or any(c < "0" or c > "9" for c in cleaned):
        return False
    total = 0
    for i, ch in enumerate(reversed(cleaned)):
        n = int(ch)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n
    return total % 10 == 0
