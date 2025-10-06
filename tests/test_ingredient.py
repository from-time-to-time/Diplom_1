import pytest
from praktikum.ingredient import Ingredient


@pytest.mark.parametrize(
    "ingredient_type,name,price",
    [
        ("FILLING", "Cheese", 9.99),
        ("SAUCE", "Ketchup 100% natural", 49.5), # Спецсимвол в названии
        ("FILLING", "Курица", 1234.56), # Кириллица
        ("FILLING", "Beef", 123456789.56),  # Большая цена
    ],
)
def test_parametrized_ingredient(ingredient_type, name, price):
    ing = Ingredient(ingredient_type, name, price)

    assert ing.get_type() == ingredient_type
    assert ing.get_name() == name
    assert ing.get_price() == price

def test_getters_types_are_correct():
    ing = Ingredient("FILLING", "Cheese", 9.99)
    assert isinstance(ing.get_type(), str)
    assert isinstance(ing.get_name(), str)
    assert isinstance(ing.get_price(), float)