from openai import OpenAI
from dotenv import load_dotenv
import os
import logging

LOG_E = logging.error
LOG_D = logging.debug
LOG_C = logging.critical
LOG_W = logging.warning

def load_env(dotenv_path='.env'):
    if 'OPENAI_API_KEY' not in os.environ:
        load_dotenv(dotenv_path)
    LOG_E(f"OEPNAI Key is not find from local environment. Checked path: {dotenv_path}") if 'OPENAI_API_KEY' not in os.environ else None

