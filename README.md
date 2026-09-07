# validkit

`validkit` ist eine kleine, eigenständige Python-Bibliothek mit neun reinen Prüf-
und Normalisierungsfunktionen. Sie ist dependency-frei (nur Standardbibliothek),
vollständig typannotiert und meldet ungültige Eingaben mit aussagekräftigen
Fehlern. Jede Funktion ist unabhängig nutzbar und wird über die öffentliche API
`validkit/__init__.py` exportiert. Es gibt keine CLI, keine UI und keinen
Netzwerkzugriff.

## Tech-Stack

- **Sprache**: Python
- **Laufzeit**: Python 3.10+
- **Test-Framework**: pytest
- **Abhängigkeiten**: keine (nur Standardbibliothek)
- **Packaging**: `pyproject.toml`

## Installation

```bash
pip install -e .
```

## Ausführung

```bash
python -c "import validkit; print(validkit.__all__)"
```

## Tests

```bash
pytest
```

## Öffentliche API

Alle neun Funktionen werden über `validkit/__init__.py` exportiert (`__all__`
enthält genau diese neun Namen).

```python
from validkit import (
    clamp,
    is_valid_email,
    is_valid_iban,
    is_valid_isbn13,
    luhn_check,
    mask_secret,
    normalize_phone,
    slugify,
    strip_accents,
)
```

## Beispiele

Ein kurzes, ausführbares Beispiel pro Funktion:

### `is_valid_email(text: str) -> bool`

```python
from validkit import is_valid_email

is_valid_email("user@example.com")  # -> True
```

### `luhn_check(digits: str) -> bool`

```python
from validkit import luhn_check

luhn_check("79927398713")  # -> True
```

### `is_valid_iban(text: str) -> bool`

```python
from validkit import is_valid_iban

is_valid_iban("DE89370400440532013000")  # -> True
```

### `is_valid_isbn13(text: str) -> bool`

```python
from validkit import is_valid_isbn13

is_valid_isbn13("9780306406157")  # -> True
```

### `normalize_phone(text: str, country_code: str) -> str`

```python
from validkit import normalize_phone

normalize_phone("+49 170 1234567", "DE")  # -> '+491701234567'
```

### `strip_accents(text: str) -> str`

```python
from validkit import strip_accents

strip_accents("Müller Straße")  # -> 'Muller Strasse'
```

### `mask_secret(text: str, keep: int = 4) -> str`

```python
from validkit import mask_secret

mask_secret("hunter2secret", keep=4)  # -> maskiert, nur die letzten 4 Zeichen sichtbar
```

### `slugify(text: str) -> str`

```python
from validkit import slugify

slugify("Héllo Wörld!")  # -> 'hello-world'
```

### `clamp(value: int | float, low: int | float, high: int | float) -> int | float`

```python
from validkit import clamp

clamp(5, 1, 10)  # -> 5
```
