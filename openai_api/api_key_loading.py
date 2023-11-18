import os
from openai import OpenAI
from dotenv import load_dotenv
from common.logging_define import *
from common.openai_model_define import Encoding

dotenv_path = ""
if __debug__:
    dotenv_path='.env.local'
else:  # python -O
    dotenv_path='env.prod'

key = 'OPENAI_API_KEY'
if key not in os.environ or os.environ.get(key):
    LOG_C(f"") if not os.path.exists(dotenv_path) else None

    load_dotenv(dotenv_path)
    LOG_C("Cannot find OPENAI_API_KEY. Please run in the root folder")  if not os.environ.get('OPENAI_API_KEY') else None
