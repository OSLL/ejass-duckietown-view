from typing import List, Optional
import os
import yaml

CAMERA_CONFIG: Optional[List[str]] = None
DEFAULT_PATH = '/cameras.yaml'


def get_config() -> List[str]:
    print(os.getcwd())
    global CAMERA_CONFIG
    if CAMERA_CONFIG is not None:
        return CAMERA_CONFIG
    with open(os.getcwd() + DEFAULT_PATH) as file:
        CAMERA_CONFIG = yaml.safe_load(file)['cameras']
    return CAMERA_CONFIG
