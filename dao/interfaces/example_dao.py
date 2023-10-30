from abc import ABC, abstractmethod


class ExampleDAO(ABC):
    @abstractmethod
    def select_one(self):
        pass
