"""opcreader project (sample executable)
See https://github.com/dmahugh/python-exe-sample
"""
import importlib_resources as _resources

from .opc import get_content_types, get_relationships

__version__ = "0.5.0"

# Read a setting from the config file
config_file = _resources.path("reader", "config.json")
# this file is currently not used, but the above line is included as an example
# of how to get access to local files that are included in the package.

__all__ = [
    "get_content_types",
    "get_relationships",
    "viewer"
]