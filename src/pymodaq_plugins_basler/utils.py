# -*- coding: utf-8 -*-
"""
Created the 31/08/2023

@author: Sebastien Weber
"""
from pathlib import Path

from pymodaq.utils.config import BaseConfig, USER


class Config(BaseConfig):
    """Main class to deal with configuration values for this plugin"""
    config_template_path = Path(__file__).parent.joinpath('resources/config_template.toml')
    config_name = f"config_{__package__.split('pymodaq_plugins_')[1]}"



def bool_hasattr( obj, attr_name):
    try:
        # Try to check if the object has the attribute (node) without raising an exception
        return hasattr(obj, attr_name)
    except Exception as e:
        # Handle any unexpected exceptions
        print(f"Unexpected error: {e}")
        return False
