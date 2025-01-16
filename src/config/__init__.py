from src.config.parser._EnvParser import EnvParser
from src.config.preprocess._ConfigPreProcess import ConfigPreProcessor

preprocessor = ConfigPreProcessor()
envparser = EnvParser(preprocessor)

CONFIG = {
    'envs': envparser.all
}

__all__ = ['CONFIG']