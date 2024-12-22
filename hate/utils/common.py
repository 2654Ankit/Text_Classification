import yaml
from ensure import ensure_annotations
from pathlib import Path
import os
from hate.logger import logging
from box import ConfigBox
@ensure_annotations
def read_yaml(path_to_yaml:Path):
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
        return ConfigBox(content)


@ensure_annotations
def create_directories(path_to_dir:list,verbose=True):
    for path in path_to_dir:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logging.info(f"created dir at :{path}")