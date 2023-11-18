from openai import OpenAI
from typing import List, Dict
# from openai_api.api_key_loading import *
import json

def fetch_chat_completion(client: OpenAI, model: str, messages: List[Dict[str, str]] ):
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response

# from common.openai_model_define  import *

# model = Model.GPT_3_5_TURBO.value
# client = OpenAI()
# messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#     {"role": "user", "content": "Where was it played?"}
# ]

# response = fetch_chat_completion(client, model, messages)
# print(response.choices[0])
