"""Telefonnummern-Normalisierung in das E.164-Format."""

import re

_MIN_DIGITS = 7
_MAX_DIGITS = 15

_DIALING_CODES = {
    "DE": "49",
    "AT": "43",
    "CH": "41",
    "US": "1",
    "CA": "1",
    "GB": "44",
    "FR": "33",
    "IT": "39",
    "ES": "34",
    "NL": "31",
    "BE": "32",
    "PL": "48",
    "CZ": "420",
    "SE": "46",
    "NO": "47",
    "DK": "45",
    "FI": "358",
    "PT": "351",
    "IE": "353",
    "LU": "352",
    "GR": "30",
    "HU": "36",
    "RO": "40",
    "BG": "359",
    "HR": "385",
    "SI": "386",
    "SK": "421",
    "LT": "370",
    "LV": "371",
    "EE": "372",
    "RU": "7",
    "UA": "380",
    "TR": "90",
    "JP": "81",
    "CN": "86",
    "IN": "91",
    "AU": "61",
    "NZ": "64",
    "BR": "55",
    "MX": "52",
}


def normalize_phone(text: str, country_code: str) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if not isinstance(country_code, str):
        raise TypeError("country_code must be a str")

    cc = country_code.strip().upper()
    if not cc:
        raise ValueError("country_code must not be empty")

    dialing_code = _DIALING_CODES.get(cc)
    if dialing_code is None:
        raise ValueError("unsupported country_code")

    digits = re.sub(r"\D", "", text)
    if not digits:
        raise ValueError("phone number must contain digits")

    if text.strip().startswith("+"):
        number = digits
    else:
        number = digits
        if number.startswith("0"):
            number = number[1:]
        number = dialing_code + number

    if len(number) > _MAX_DIGITS:
        raise ValueError("phone number is too long")
    if len(number) < _MIN_DIGITS:
        raise ValueError("phone number is too short")

    return "+" + number
