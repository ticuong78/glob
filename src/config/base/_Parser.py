from os import PathLike
from typing import Union
from pathlib import Path
from abc import ABC, abstractmethod

class Parser(ABC):
    @abstractmethod
    def _parse(self):
        pass