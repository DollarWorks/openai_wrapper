import pytest
import os
import asyncio
from openai_api.text_generation_api import *
from common.openai_model_define import Model

def test_chat_completion():
    model = Model.GPT_3_5_TURBO.value
    client = OpenAI()
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]
    
    response = fetch_chat_completion(client, model, messages)
    assert response.choices[0] is not None