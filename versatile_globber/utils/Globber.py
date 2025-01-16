from abc import ABC, abstractmethod

class Globber(ABC):
    @property
    @abstractmethod
    def all(self):
        pass

    @abstractmethod
    def _globs(self):
        pass