import re
import unicodedata

# Characters without a canonical decomposition in NFD that must still be
# transliterated so strip_accents('Straße') yields 'Strasse'.
_TRANSLITERATIONS = {
    "ß": "ss",
    "ẞ": "SS",
}


def strip_accents(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("strip_accents expects a string")

    for source, target in _TRANSLITERATIONS.items():
        text = text.replace(source, target)

    decomposed = unicodedata.normalize("NFD", text)
    return "".join(char for char in decomposed if not unicodedata.combining(char))


def slugify(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError("slugify expects a string")

    normalized = strip_accents(text).lower()
    slug = re.sub(r"[^a-z0-9]+", "-", normalized)
    return slug.strip("-")
