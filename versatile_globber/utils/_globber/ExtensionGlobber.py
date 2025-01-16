import os
import glob

from os import PathLike
from pathlib import Path
from typing import List, Union

from versatile_globber.utils._base._Globber import Globber

class ExtensionGlobber(Globber):
    def __init__(self, paths: List[Union[Path, PathLike, str]], extensions: List[str]):
        self._paths = paths
        self._extensions = extensions

    @property
    def all(self) -> List[Union[Path, PathLike, str]]:
        return self._globs(self._paths, self._extensions)

    def _glob(self, path: Union[Path, PathLike, str], extension: str) -> Union[Path, PathLike, str]:
        return glob.glob(str(path) + f"/*{extension}")
    
    def _globs(self, paths: List[Union[Path, PathLike, str]], extensions: List) -> List[Union[Path, PathLike, str]]:
        files = []

        for extension in extensions:
            for path in paths:
                files += self._glob(path, extension)
                print(self._glob(path, extension))

        return files