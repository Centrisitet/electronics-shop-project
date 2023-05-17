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