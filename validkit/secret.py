def mask_secret(text: str, keep: int = 4) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if not isinstance(keep, int):
        raise TypeError("keep must be an int")
    if keep < 0:
        raise ValueError("keep must be non-negative")

    length = len(text)
    if keep >= length:
        return "*" * length
    return "*" * (length - keep) + text[length - keep :]
