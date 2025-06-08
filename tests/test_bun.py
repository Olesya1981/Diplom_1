import pytest
from praktikum.bun import Bun
from conftest import bun_fixture
from data import BUN_NAME, BUN_PRICE

class TestBuns:

    def test_create_bun_with_name_and_price(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        assert bun.name == BUN_NAME and bun.price == BUN_PRICE

    # В классе Bun отсутствует проверка передаваемых при инициализации значений, объект создаётся и с пустым именем, и
    # со строковым параметром в цене. Поэтому следующий тест проверяет, что объект не будет создан только с одним из
    # параметров.
    @pytest.mark.parametrize(('key', 'value'), [('name', BUN_NAME), ('price', BUN_PRICE)])
    def test_fail_to_create_bun_without_name_or_price(self, key, value):
        try:
            bun = Bun(key = value)
        except TypeError:
            pass
        assert 'bun' not in locals()

    def test_get_bun_name(self, bun_fixture):
        assert bun_fixture.get_name() == BUN_NAME

    def test_get_bun_price(self, bun_fixture):
        assert bun_fixture.get_price() == BUN_PRICE
