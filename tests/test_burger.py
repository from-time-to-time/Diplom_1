import pytest
from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

from data import UserData
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

def test_set_buns_sets_bun():
    burger = Burger()
    bun = Bun(UserData.CYRILLIC_BUN_NAME, UserData.REGULAR_PRICE)

    burger.set_buns(bun)

    assert burger.bun is bun

def test_add_ingredient_appends():
    burger = Burger()
    ing = Ingredient(INGREDIENT_TYPE_SAUCE, UserData.KETCHUP_ING_NAME, UserData.REGULAR_PRICE)

    burger.add_ingredient(ing)
    assert burger.ingredients == [ing]


def test_remove_ingredient_by_index():
    burger = Burger()
    ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, UserData.KETCHUP_ING_NAME, UserData.REGULAR_PRICE)
    ing2 = Ingredient(INGREDIENT_TYPE_FILLING, UserData.BEEF_ING_NAME, UserData.REGULAR_PRICE)
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)

    burger.remove_ingredient(0)

    assert burger.ingredients == [ing2]

@pytest.mark.parametrize(
    "ingredients, index, new_index, expected_ingredients",
    [
        ([UserData.CHEESE_ING_NAME, UserData.TOMATO_ING_NAME, UserData.ONION_ING_NAME], 0, 2, [UserData.TOMATO_ING_NAME, UserData.ONION_ING_NAME, UserData.CHEESE_ING_NAME]), # из начала в конец
        ([UserData.CHEESE_ING_NAME, UserData.TOMATO_ING_NAME, UserData.ONION_ING_NAME], 2, 0, [UserData.ONION_ING_NAME, UserData.CHEESE_ING_NAME, UserData.TOMATO_ING_NAME]), # из конца в начало
        ([UserData.CHEESE_ING_NAME, UserData.TOMATO_ING_NAME, UserData.ONION_ING_NAME, UserData.CUCUMBER_ING_NAME], 1, 2, [UserData.CHEESE_ING_NAME, UserData.ONION_ING_NAME, UserData.TOMATO_ING_NAME, UserData.CUCUMBER_ING_NAME]), # внутренняя перестановка 1
        ([UserData.CHEESE_ING_NAME, UserData.TOMATO_ING_NAME, UserData.ONION_ING_NAME, UserData.CUCUMBER_ING_NAME], 2, 1, [UserData.CHEESE_ING_NAME, UserData.ONION_ING_NAME, UserData.TOMATO_ING_NAME, UserData.CUCUMBER_ING_NAME]), # внутренняя перестановка 2
    ],
)
def test_move_ingredient_various_positions(ingredients, index, new_index, expected_ingredients):
    burger = Burger()
    burger.set_buns(Bun(UserData.CYRILLIC_BUN_NAME, UserData.REGULAR_PRICE))
    for name in ingredients:
        ing = Ingredient(INGREDIENT_TYPE_FILLING, name, UserData.REGULAR_PRICE)
        burger.add_ingredient(ing)

    burger.move_ingredient(index, new_index)

    new_order_list = []
    for ing in burger.ingredients:
        new_order_list.append(ing.get_name())

    assert new_order_list == expected_ingredients

@pytest.mark.parametrize(
    "bun_price, ingredient_prices, expected_total",
    [
        (50.0, [], 100.0), # Ингредиенты отсутствуют
        (30.0, [10.0], 70.0), # Один ингредиент
        (10.0, [5.0, 10.99, 9.01], 45.0), # Несколько ингредиентов
        (99999.99, [1.0, 2.0], 200002.98), # Большая цена
    ],
)
def test_get_price(bun_price, ingredient_prices, expected_total):
    burger = Burger()

    bun = Mock()
    bun.get_price.return_value = bun_price
    bun.get_name.return_value = UserData.CYRILLIC_BUN_NAME
    burger.set_buns(bun)

    for index, price in enumerate(ingredient_prices):
        ing = Mock()
        ing.get_price.return_value = price
        ing.get_name.return_value = f"ing{index}"
        ing.get_type.return_value = INGREDIENT_TYPE_FILLING
        burger.add_ingredient(ing)

    total = burger.get_price()
    assert total == expected_total

def test_get_receipt_correct_formatting():
    burger = Burger()
    bun = Bun(UserData.CYRILLIC_BUN_NAME, UserData.REGULAR_PRICE)
    burger.set_buns(bun)

    ing1 = Ingredient(INGREDIENT_TYPE_SAUCE, UserData.KETCHUP_ING_NAME, UserData.REGULAR_PRICE)
    ing2 = Ingredient(INGREDIENT_TYPE_FILLING, UserData.BEEF_ING_NAME, UserData.REGULAR_PRICE)
    burger.add_ingredient(ing1)
    burger.add_ingredient(ing2)

    expected_price = burger.get_price()
    expected_receipt = (
        f"(==== {UserData.CYRILLIC_BUN_NAME} ====)\n"
        f"= {INGREDIENT_TYPE_SAUCE.lower()} {UserData.KETCHUP_ING_NAME} =\n"
        f"= {INGREDIENT_TYPE_FILLING.lower()} {UserData.BEEF_ING_NAME} =\n"
        f"(==== {UserData.CYRILLIC_BUN_NAME} ====)\n"
        "\n"
        f"Price: {expected_price}"
    )

    assert burger.get_receipt() == expected_receipt
