from conftest import *
from random import choice

class TestBurger:

    def test_burger_contains_buns_and_ingredients(self):
        burger = Burger()
        assert burger.bun == None and burger.ingredients == []

    def test_set_buns(self, burger_fixture, bun_mock):
        burger_fixture.set_buns(bun_mock)
        assert burger_fixture.bun.name == BUN_NAME

    def test_add_ingredient_to_list_is_success(self, burger_fixture, ingredient_filling_mock):
        burger_fixture.add_ingredient(ingredient_filling_mock)
        assert burger_fixture.ingredients[0].name == INGREDIENT_FILLING_NAME

    def test_remove_ingredient_from_list_success(self, burger_fixture, ingredient_filling_mock):
        burger_fixture.add_ingredient(ingredient_filling_mock)
        burger_fixture.remove_ingredient(0)
        assert len(burger_fixture.ingredients) == 0

    def test_move_ingredient_in_list_success(self, burger_fixture, ingredient_sauce_mock, ingredient_filling_mock):
        burger_fixture.add_ingredient(ingredient_filling_mock)
        burger_fixture.add_ingredient(ingredient_sauce_mock)
        burger_fixture.move_ingredient(0, 1)
        assert burger_fixture.ingredients[0].name == INGREDIENT_SAUCE_NAME

    def test_get_burger_price_is_success(self, burger_fixture, bun_mock, ingredient_filling_mock):
        burger_fixture.set_buns(bun_mock)
        burger_fixture.add_ingredient(ingredient_filling_mock)
        assert burger_fixture.get_price()

    # Проверка корректности подсчёта цены бургера с количеством ингредиентов от 0 до 4
    @pytest.mark.parametrize('number_of_ingredients', [0, 1, 2, 3, 4])
    def test_get_burger_price_is_correct(self, number_of_ingredients, burger_fixture, bun_mock,
                                         ingredient_sauce_mock, ingredient_filling_mock):
        burger_fixture.set_buns(bun_mock)
        for _ in range(number_of_ingredients):
            burger_fixture.add_ingredient(choice([ingredient_sauce_mock, ingredient_filling_mock]))
        price = BUN_PRICE * 2 + sum(map(lambda x: x.get_price(), burger_fixture.ingredients))
        assert price == burger_fixture.get_price()

    def test_get_receipt_with_burger_ingredients(self, burger_fixture, bun_mock, ingredient_filling_mock,
                                                 ingredient_sauce_mock):
        burger_fixture.set_buns(bun_mock)
        burger_fixture.add_ingredient(ingredient_filling_mock)
        burger_fixture.add_ingredient(ingredient_sauce_mock)
        assert burger_fixture.get_receipt() == RECEIPT