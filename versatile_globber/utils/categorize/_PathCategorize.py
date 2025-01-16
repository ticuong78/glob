import os

from os import PathLike
from pathlib import Path
from typing import List, Union
from versatile_globber.utils.base._Categorizer import Categorizer

class PathCategorize(Categorizer):
    def categorize(self, paths: List[Union[PathLike, Path, str]]):
        dirs = []
        exes = []

        for path in paths:
            splitext = os.path.splitext(path)[1] # has extension -> file

            if splitext:
                exes.append(path)
            else:
                dirs.append(path)

        return dirs, exes