from abc import ABC, abstractmethod


class AbstractBuddy(ABC):

    @abstractmethod
    def generate_response(self):
        pass
