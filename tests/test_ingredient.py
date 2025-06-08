import pytest
from praktikum.ingredient import Ingredient
from conftest import ingredient_fixture
from data import INGREDIENT_FILLING_TYPE, INGREDIENT_FILLING_NAME, INGREDIENT_FILLING_PRICE

class TestIngredient:

    def test_ingredient_init(self):
        ingredient = Ingredient(INGREDIENT_FILLING_TYPE, INGREDIENT_FILLING_NAME, INGREDIENT_FILLING_PRICE)
        assert ((ingredient.type == INGREDIENT_FILLING_TYPE and ingredient.name == INGREDIENT_FILLING_NAME)
                and ingredient.price == INGREDIENT_FILLING_PRICE)

    def test_get_ingredient_type_is_filling_or_sauce(self, ingredient_fixture):
        assert ingredient_fixture.get_type() == INGREDIENT_FILLING_TYPE

    def test_get_ingredient_name(self, ingredient_fixture):
        assert ingredient_fixture.get_name() == INGREDIENT_FILLING_NAME

    def test_get_ingredient_price_is_correct(self, ingredient_fixture):
        assert ingredient_fixture.get_price() == INGREDIENT_FILLING_PRICE