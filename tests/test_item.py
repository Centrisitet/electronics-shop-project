"""Здесь надо написать тесты с использованием pytest для модуля item."""

from src.item import Item
import pytest


@pytest.fixture
def item():
    return Item('Item', 1000.0, 5)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 5000


def test_apply_discount(item):
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 800.0


def test_fullname(item):
    assert item.name == 'Item'


def test_repr_(item):
    assert repr(item) == f"Item('Item', 1000.0, 5)"


def test_str(item):
    assert str(item) == 'Item'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
