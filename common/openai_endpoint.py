from enum import Enum

OPENAI_HOST = 'https://api.openai.com'

class Endpoint(Enum):
      CHAT_COMPLETION = '/v1/chat/completions'  # model 2023-
      COMPLETION = '/v1/completions'  #model 2020-2022, 2023
