from abc import ABC, abstractmethod

class Globber(ABC):
    @abstractmethod
    def _glob(self):
        pass