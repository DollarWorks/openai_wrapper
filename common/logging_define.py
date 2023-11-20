import logging
import json

LOG_E = logging.error
LOG_D = logging.debug
LOG_C = logging.critical
LOG_W = logging.warning


logging.basicConfig(level=logging.DEBUG)

def print_json_d(json_str: str, message: str = "", indent: int =4):
    json_obj = json.dumps(json_str, indent)
    LOG_D(f"{message}\n{json_str}\n")

