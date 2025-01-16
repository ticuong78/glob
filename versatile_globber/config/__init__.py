from versatile_globber.config.parser._EnvParser import EnvParser
from versatile_globber.config.preprocess._ConfigPreProcess import ConfigPreProcessor

preprocessor = ConfigPreProcessor()
envparser = EnvParser(preprocessor)

CONFIG = {
    'envs': envparser.all
}

__all__ = ['CONFIG']