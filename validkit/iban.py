"""IBAN-Validierung nach ISO 13616-1."""

# Offizielle IBAN-Längen je Ländercode (ISO 13616-1 Registry).
_IBAN_LENGTHS: dict[str, int] = {
    "AD": 24,
    "AE": 23,
    "AL": 28,
    "AT": 20,
    "AZ": 28,
    "BA": 20,
    "BE": 16,
    "BG": 22,
    "BH": 22,
    "BR": 29,
    "BY": 28,
    "CH": 21,
    "CR": 22,
    "CY": 28,
    "CZ": 24,
    "DE": 22,
    "DK": 18,
    "DO": 28,
    "EE": 20,
    "EG": 29,
    "ES": 24,
    "FI": 18,
    "FO": 18,
    "FR": 27,
    "GB": 22,
    "GE": 22,
    "GI": 23,
    "GL": 18,
    "GR": 27,
    "GT": 28,
    "HR": 21,
    "HU": 28,
    "IE": 22,
    "IL": 23,
    "IQ": 23,
    "IS": 26,
    "IT": 27,
    "JO": 30,
    "KW": 30,
    "KZ": 20,
    "LB": 28,
    "LC": 32,
    "LI": 21,
    "LT": 20,
    "LU": 20,
    "LV": 21,
    "MC": 27,
    "MD": 24,
    "ME": 22,
    "MK": 19,
    "MR": 27,
    "MT": 31,
    "MU": 30,
    "NL": 18,
    "NO": 15,
    "PK": 24,
    "PL": 28,
    "PS": 29,
    "PT": 25,
    "QA": 29,
    "RO": 24,
    "RS": 22,
    "SA": 24,
    "SC": 31,
    "SE": 24,
    "SI": 19,
    "SK": 24,
    "SM": 27,
    "ST": 25,
    "SV": 28,
    "TL": 23,
    "TN": 24,
    "TR": 26,
    "UA": 29,
    "VA": 22,
    "VG": 24,
    "XK": 20,
}

# Feste Maximallänge einer IBAN nach ISO 13616-1 (Ländercode 2 + Prüfziffer 2 + BBAN <= 30).
_MAX_LENGTH = 34


def _convert_char(ch: str) -> str | None:
    """Konvertiert ein Zeichen in seine Zifferndarstellung (A=10, ..., Z=35)."""
    if "0" <= ch <= "9":
        return ch
    if "A" <= ch <= "Z":
        return str(ord(ch) - ord("A") + 10)
    if "a" <= ch <= "z":
        return str(ord(ch) - ord("a") + 10)
    return None


def is_valid_iban(text: str) -> bool:
    """Prüft eine IBAN per Ländercode, Länge und Modulo-97-Verfahren."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if len(text) > _MAX_LENGTH:
        return False

    expected_length = _IBAN_LENGTHS.get(text[:2].upper())
    if expected_length is None:
        return False

    if len(text) != expected_length:
        return False

    if not text[2:4].isdigit():
        return False

    rearranged = text[4:] + text[:4]
    converted: list[str] = []
    for ch in rearranged:
        digit = _convert_char(ch)
        if digit is None:
            return False
        converted.append(digit)

    return int("".join(converted)) % 97 == 1
