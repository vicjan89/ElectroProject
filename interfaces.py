from abc import ABC, abstractmethod


class Storage(ABC):

    def __init__(self, path: str):
        self.path = path

    @abstractmethod
    def read(self):
        ...

    @abstractmethod
    def write(self, text: str):
        ...
