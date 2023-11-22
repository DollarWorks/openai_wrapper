import logging
import json

LOG_E = logging.error
LOG_C = logging.critical
LOG_W = logging.warning


logging.basicConfig(level=logging.DEBUG)

def print_json_d(json_str: str, message: str = ""):
    json_data = json.load(json_str)
    pretty = json.dumps(json_data)
    LOG_D(f"{message}\n{pretty}\n")


def LOG_D(*args):
    message = " ".join(map(str, args))  # Concatenate all arguments into a single string
    logging.debug(f"\n[DEBUG]:\n{message}\n")