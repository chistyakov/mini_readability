import os
from types import MappingProxyType

import yaml


def get_config():
    config_path = os.environ.get("PARSE_CONFIG_PATH", "config.yaml")
    with open(config_path, "r") as f:
        return MappingProxyType(yaml.load(f))
