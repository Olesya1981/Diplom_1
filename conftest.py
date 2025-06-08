from unittest.mock import Mock
from data import *
import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger

@pytest.fixture
def bun_fixture():
    return Bun(BUN_NAME, BUN_PRICE)

@pytest.fixture
def ingredient_fixture():
    return Ingredient(INGREDIENT_FILLING_TYPE, INGREDIENT_FILLING_NAME, INGREDIENT_FILLING_PRICE)

@pytest.fixture
def burger_fixture():
    return Burger()

@pytest.fixture
def bun_mock():
    mock_bun = Mock()
    mock_bun.name = BUN_NAME
    mock_bun.get_name.return_value = BUN_NAME
    mock_bun.get_price.return_value = BUN_PRICE
    return mock_bun

@pytest.fixture
def ingredient_filling_mock():
    mock_ingredient = Mock()
    mock_ingredient.name = INGREDIENT_FILLING_NAME
    mock_ingredient.get_name.return_value = INGREDIENT_FILLING_NAME
    mock_ingredient.get_type.return_value = INGREDIENT_FILLING_TYPE
    mock_ingredient.get_price.return_value = INGREDIENT_FILLING_PRICE
    return mock_ingredient

@pytest.fixture
def ingredient_sauce_mock():
    mock_ingredient = Mock()
    mock_ingredient.name = INGREDIENT_SAUCE_NAME
    mock_ingredient.get_name.return_value = INGREDIENT_SAUCE_NAME
    mock_ingredient.get_type.return_value = INGREDIENT_SAUCE_TYPE
    mock_ingredient.get_price.return_value = INGREDIENT_SAUCE_PRICE
    return mock_ingredient