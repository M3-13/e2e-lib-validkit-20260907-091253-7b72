"""E-Mail-Adressen-Validierung (nur Standardbibliothek)."""

import re

_MAX_LENGTH = 254

_EMAIL_RE = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")


def is_valid_email(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if len(text) > _MAX_LENGTH:
        return False
    return _EMAIL_RE.fullmatch(text) is not None
