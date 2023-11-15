from openai import OpenAI
from dotenv import load_dotenv
import os
import logging

LOG_E = logging.error
LOG_D = logging.debug
LOG_C = logging.critical
LOG_W = logging.warning

if __debug__:
    dotenv_path='.env.local'
else:
    dotenv_path='env.prod'

if 'OPENAI_API_KEY' not in os.environ:
    load_dotenv(dotenv_path)
LOG_E(f"OEPNAI Key is not find from local environment. Checked path: {dotenv_path}") if 'OPENAI_API_KEY' not in os.environ else None


client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY')
)

stream = client.chat.completions.create(
    model="cl100k_base",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for part in stream:
    print(part.choices[0].delta.content or "")
