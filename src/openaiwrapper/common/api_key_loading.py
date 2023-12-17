import os
from dotenv import load_dotenv, find_dotenv
from common.logging_define import *

dotenv_path = ""
if __debug__:
    dotenv_path = '.env.local'
else:  # python -O
    dotenv_path = 'env.prod'

key = 'OPENAI_API_KEY'
if key not in os.environ or os.environ.get(key):
    file = find_dotenv(dotenv_path)
    LOG_C(f"Cannot find {file}") if not file else None

    load_dotenv(dotenv_path)
    LOG_C(f"Cannot find OPENAI_API_KEY. Please run in the root folder") if not os.environ.get('OPENAI_API_KEY') else None
