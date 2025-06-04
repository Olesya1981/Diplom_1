from praktikum.database import Database

class TestDatabase:

    # Проверяем, что создаётся объект класса Database в котором есть доступные булки и ингредиенты
    def test_database_creation(self):
        database = Database()
        assert len(database.buns) == 3 and len(database.ingredients) == 6

    def test_available_buns(self):
        database = Database()
        assert database.buns == database.available_buns()

    def test_available_ingredients(self):
        database = Database()
        assert database.ingredients == database.available_ingredients()