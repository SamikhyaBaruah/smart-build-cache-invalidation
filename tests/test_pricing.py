
import pytest
from src.pricing import apply_discount


def test_apply_discount():
    assert apply_discount(100, 10) == 90.0


def test_full_discount():
    assert apply_discount(100, 100) == 0.0


def test_invalid_discount():
    with pytest.raises(ValueError):
        apply_discount(100, 120)


def test_negative_price():
    with pytest.raises(ValueError):
        apply_discount(-10, 10)
