from praktikum.database import Database

def test_ingredients_returns_list(db: Database):
    ingredients = db.available_ingredients()
    assert isinstance(ingredients, list)

def test_buns_returns_list(db: Database):
    buns = db.available_buns()
    assert isinstance(buns, list)

def test_ingredients_not_empty(db: Database):
    ingredients = db.available_ingredients()
    assert len(ingredients) > 0

def test_buns_not_empty(db: Database):
    buns = db.available_buns()
    assert len(buns) > 0

def test_buns_valid_price(db: Database):
    buns = db.available_buns()

    for bun in buns:
        assert bun.get_price() > 0.0

def test_ingredients_valid_price(db: Database):
    ingredients = db.available_ingredients()

    for ingredient in ingredients:
        assert ingredient.get_price() > 0.0