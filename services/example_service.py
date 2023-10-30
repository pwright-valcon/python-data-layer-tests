from dao.interfaces.example_dao import ExampleDAO


class ExampleService:
    def __init__(self, example_dao: ExampleDAO):
        self.example_dao = example_dao

    def select_one(self):
        return self.example_dao.select_one()
