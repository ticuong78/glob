from os import PathLike
from pathlib import Path
from typing import List, Union
from abc import ABC, abstractmethod

class Categorizer(ABC):
    @abstractmethod
    def categorize(self, paths: List[Union[PathLike, Path, str]]):
        pass