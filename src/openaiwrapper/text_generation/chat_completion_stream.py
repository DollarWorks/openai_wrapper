from ..common.api_key_loading import *
from openai import OpenAI
from fastapi import HTTPException
import time

openai_model = "gpt-3.5-turbo"
max_responses = 1
temperature = 0.7
max_tokens = 512

error503 = "OpenAI server is busy, try again later"

openai = OpenAI()
start_time = time.time()

def fetch_chat_completion_stream(prompt: str):
    try:
        response = openai.chat.completions.create(
            model=openai_model,
            temperature=temperature,
            max_tokens=max_tokens,
            n=max_responses,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            messages=[
                {"role": "system", "content": "You are a knowledgeable assistant."},
                {"role": "user", "content": prompt},
            ],
            stream=True,
        )
    except Exception as e:
        print("Error in creating campaigns from openAI:", str(e))
        raise HTTPException(503, error503)

    try:
        for chunk in response:
            chunk_message = chunk.choices[0].delta.content or ""
            yield chunk_message

    except Exception as e:
        print("OpenAI Response (Streaming) Error: " + str(e))
        raise HTTPException(503, error503)
