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
    load_dotenv(dotenv_path)
    if os.environ.get(key):
        LOG_C("Critial: Cannot find OPENAI_API_KEY. Please run in the root folder") 

client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY')
)


stream = client.chat.completions.create(
    model=Encoding.CL100K_BASE.value,
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for part in stream:
    print(part.choices[0].delta.content or "")
