import pytest

from validkit.text import slugify, strip_accents


def test_strip_accents_removes_diacritics():
    assert strip_accents("Müller Straße") == "Muller Strasse"


def test_strip_accents_handles_various_accents():
    assert strip_accents("ÁÉÍÓÚ àèìòù") == "AEIOU aeiou"


def test_strip_accents_returns_unchanged_text_without_accents():
    assert strip_accents("Hello World") == "Hello World"


def test_strip_accents_empty_input():
    assert strip_accents("") == ""


def test_strip_accents_rejects_non_string():
    with pytest.raises(TypeError):
        strip_accents(None)
    with pytest.raises(TypeError):
        strip_accents(123)


def test_slugify_basic_conversion():
    assert slugify("Héllo Wörld!") == "hello-world"


def test_slugify_lowercases_and_replaces_spaces():
    assert slugify("Hello World") == "hello-world"


def test_slugify_collapses_multiple_separators():
    assert slugify("Hello   World!!") == "hello-world"


def test_slugify_strips_leading_and_trailing_separators():
    assert slugify("  --Hello World--  ") == "hello-world"


def test_slugify_preserves_digits_and_hyphens():
    assert slugify("Version 2.0.1") == "version-2-0-1"


def test_slugify_empty_input():
    assert slugify("") == ""


def test_slugify_only_special_characters():
    assert slugify("!!!") == ""


def test_slugify_rejects_non_string():
    with pytest.raises(TypeError):
        slugify(None)
    with pytest.raises(TypeError):
        slugify(123)
