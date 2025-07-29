import json
import logging

def load_config(path):
    with open(path, "r") as file:
        logging.info(f"config path is {path}")
        return json.load(file)
