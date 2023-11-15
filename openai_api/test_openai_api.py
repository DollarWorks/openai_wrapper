import pytest
from openai_api import *
import os

def test_load_env():
    load_dotenv('.env.dev')
    assert os.environ.get('OPENAI_API_KEY')
