import pytest
from praktikum.ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE
from data import UserData

@pytest.mark.parametrize(
    "ingredient_type",
    [
        INGREDIENT_TYPE_FILLING,
        INGREDIENT_TYPE_SAUCE
    ],
)
def test_parametrized_ingredient_type(ingredient_type):
    ing = Ingredient(ingredient_type, UserData.KETCHUP_ING_NAME, UserData.REGULAR_PRICE)
    assert ing.get_type() == ingredient_type

@pytest.mark.parametrize(
    "name",
    [
        UserData.CHEESE_ING_NAME,
        UserData.KETCHUP_NATURAL_ING_NAME, # Спецсимвол в названии
        UserData.RUSSIAN_SPEAKING_CHICKEN_ING_NAME # Кириллица
    ]
)
def test_parametrized_ingredient_name(name):
    ing = Ingredient(INGREDIENT_TYPE_FILLING, name, UserData.REGULAR_PRICE)
    assert ing.get_name() == name

@pytest.mark.parametrize(
    "price",
    [
        UserData.REGULAR_PRICE, # Обычная
        UserData.LONG_PRICE, # Длинная
        UserData.LESS_THEN_ONE_PRICE # Меньше 1
    ],
)
def test_parametrized_ingredient_price(price):
    ing = Ingredient(INGREDIENT_TYPE_FILLING, UserData.BEEF_ING_NAME, price)
    assert ing.get_price() == price

def test_ing_type_type_is_correct():
    ing = Ingredient(INGREDIENT_TYPE_FILLING, UserData.BEEF_ING_NAME, UserData.REGULAR_PRICE)
    assert isinstance(ing.get_type(), str)

def test_name_type_is_correct():
    ing = Ingredient(INGREDIENT_TYPE_FILLING, UserData.BEEF_ING_NAME, UserData.REGULAR_PRICE)
    assert isinstance(ing.get_name(), str)

def test_price_type_is_correct():
    ing = Ingredient(INGREDIENT_TYPE_FILLING, UserData.BEEF_ING_NAME, UserData.REGULAR_PRICE)
    assert isinstance(ing.get_price(), float)