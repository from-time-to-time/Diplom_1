import pytest
from praktikum.bun import Bun
from data import UserData

@pytest.mark.parametrize(
    "name",
    [
        UserData.CYRILLIC_BUN_NAME, # Кириллица
        UserData.LATIN_BUN_NAME, # Латиница
        UserData.SYMBOLIC_BUN_NAME # Спецсимволы
    ],
)
def test_parametrized_bun_name(name):
    bun = Bun(name=name, price=UserData.REGULAR_PRICE)
    assert bun.get_name() == name

@pytest.mark.parametrize(
    "price",
    [
        UserData.REGULAR_PRICE, # Обычная
        UserData.LONG_PRICE, # Длинная
        UserData.LESS_THEN_ONE_PRICE # Меньше 1
    ],
)
def test_parametrized_bun_price(price):
    bun = Bun(name=UserData.CYRILLIC_BUN_NAME, price=price)
    assert bun.get_price() == price

def test_bun_price_correct_type():
    bun = Bun(name=UserData.CYRILLIC_BUN_NAME, price=UserData.REGULAR_PRICE)
    assert isinstance(bun.get_price(), float) # Возвращает Float

def test_bun_name_correct_type():
    bun = Bun(name=UserData.CYRILLIC_BUN_NAME, price=UserData.REGULAR_PRICE)
    assert isinstance(bun.get_name(), str) # Возвращает String