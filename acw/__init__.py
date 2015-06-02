"""
The Awesome Config Wrapper

This is an end-all wrapper around the ConfigParser library, aiming to add
at the minimum the following features:
    - typechecking
    - value defaulting
    - validation
"""

from .config import Config
from .section import ConfigSection
from .types import Type, IntegerType


__all__ = ['Config', 'ConfigSection', 'Type', 'IntegerType']
