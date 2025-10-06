import pytest
from praktikum.bun import Bun

@pytest.mark.parametrize(
    "name, price",
    [
        ("Белая булочка", 20.99),
        ("Ржаная булочка", 999999.99), # Длинная цена
        ("Tasty bun", 2.99), # Латиница
        ("Булочка 100%", 0.99) # Спецсимволы в имени
    ],
)
def test_parametrized_bun(name, price):
    bun = Bun(name=name, price=price)
    assert bun.get_name() == name
    assert bun.get_price() == price

def test_getters_types_are_correct():
    bun = Bun(name="Сдобная", price=10.0)
    assert isinstance(bun.get_name(), str) # Возвращает String
    assert isinstance(bun.get_price(), float) # Возвращает Float