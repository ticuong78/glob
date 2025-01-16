import os
import dotenv as de

from versatile_globber.config.base._Parser import Parser
from versatile_globber.config.base._PreProcess import PreProcessor

from versatile_globber.env import AVAILABLE_ENVS
from versatile_globber.ext import AVAILABLE_EXTS

de.load_dotenv()

class EnvParser(Parser):
    @property
    def all(self):
        object = self._preprocessor.preprocess(self._parse())
        object['EXTENSIONS'] = AVAILABLE_EXTS

        return object

    def __init__(self, preprocessor: PreProcessor):
        self._preprocessor = preprocessor

    def _parse(self):
        envs = dict([(env, os.getenv(env)) for env in AVAILABLE_ENVS])

        return envs