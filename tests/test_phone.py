from src.phone import Phone
import pytest


@pytest.fixture
def phone():
    return Phone("Phone", 5000, 5, 2)


def test_calculate_total_price(phone):
    assert phone.calculate_total_price() == 25000


def test_fullname(phone):
    assert phone.name == 'Phone'


def test_repr_(phone):
    assert repr(phone) == f"Phone('Phone', 5000, 5, 2)"


def test_add():
    item_1 = Phone('Item', 1000.0, 5, 2)
    item_2 = Phone('Item', 1000.0, 5, 2)
    assert item_1 + item_2 == 10