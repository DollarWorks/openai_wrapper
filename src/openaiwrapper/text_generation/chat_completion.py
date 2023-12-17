from openai import OpenAI
from typing import List, Dict
from common.openai_model_define import *


def fetch_chat_completion(client: OpenAI,
                          messages: List[Dict[str, str]],
                          model: str = Model.GPT_3_5_TURBO.value):
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response


# response.choices[0].message.
def fetch_chat_completion_json(client: OpenAI,
                               messages: List[Dict[str, str]],
                               model: str = Model.GPT_3_5_TURBO_1106.value):
    response = client.chat.completions.create(
        model=model,
        response_format={"type": "json_object"},
        messages=messages
    )
    return response
