import inspect

import validkit


def test_all_nine_names_importable():
    assert hasattr(validkit, "is_valid_email")
    assert hasattr(validkit, "luhn_check")
    assert hasattr(validkit, "is_valid_iban")
    assert hasattr(validkit, "is_valid_isbn13")
    assert hasattr(validkit, "normalize_phone")
    assert hasattr(validkit, "strip_accents")
    assert hasattr(validkit, "mask_secret")
    assert hasattr(validkit, "slugify")
    assert hasattr(validkit, "clamp")


def test_all_exports_exactly_nine_names():
    assert sorted(validkit.__all__) == [
        "clamp",
        "is_valid_email",
        "is_valid_iban",
        "is_valid_isbn13",
        "luhn_check",
        "mask_secret",
        "normalize_phone",
        "slugify",
        "strip_accents",
    ]


def test_signatures():
    assert list(inspect.signature(validkit.is_valid_email).parameters) == ["text"]
    assert inspect.signature(validkit.is_valid_email).return_annotation is bool

    assert list(inspect.signature(validkit.luhn_check).parameters) == ["digits"]
    assert inspect.signature(validkit.luhn_check).return_annotation is bool

    assert list(inspect.signature(validkit.is_valid_iban).parameters) == ["text"]
    assert inspect.signature(validkit.is_valid_iban).return_annotation is bool

    assert list(inspect.signature(validkit.is_valid_isbn13).parameters) == ["text"]
    assert inspect.signature(validkit.is_valid_isbn13).return_annotation is bool

    assert list(inspect.signature(validkit.normalize_phone).parameters) == [
        "text",
        "country_code",
    ]
    assert inspect.signature(validkit.normalize_phone).return_annotation is str

    assert list(inspect.signature(validkit.strip_accents).parameters) == ["text"]
    assert inspect.signature(validkit.strip_accents).return_annotation is str

    assert list(inspect.signature(validkit.mask_secret).parameters) == ["text", "keep"]
    keep = inspect.signature(validkit.mask_secret).parameters["keep"]
    assert keep.default == 4
    assert inspect.signature(validkit.mask_secret).return_annotation is str

    assert list(inspect.signature(validkit.slugify).parameters) == ["text"]
    assert inspect.signature(validkit.slugify).return_annotation is str

    assert list(inspect.signature(validkit.clamp).parameters) == [
        "value",
        "low",
        "high",
    ]
    assert inspect.signature(validkit.clamp).return_annotation is not inspect.Parameter.empty
