import pytest
import os
from openai_api.text_generation_api import *
from common.openai_model_define import Model



client = OpenAI()

# openai test cases
def test_chat_completion():
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]

    response = fetch_chat_completion(client, messages)
    assert response.choices[0] is not None
    assert response.model is not None


# deeplearning.ai prompt enginnering
# https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/2/guidelines
#
# Principle 1: Write clear and specific instructions
#
# Tactic 1: Use delimiters to clearly indicate distinct parts of the input
#   -- Delimiters can be anything like: ```, """, < >, <tag> </tag>
#

def test_chat_completion_deeplearningai_tactic_1():
    text = f"""
    You should express what you want a model to do by \
    providing instructions that are as clear and \
    specific as you can possibly make them. \
    This will guide the model towards the desired output, \
    and reduce the chances of receiving irrelevant \
    or incorrect responses. Don't confuse writing a \
    clear prompt with writing a short prompt. \
    In many cases, longer prompts provide more clarity \
    and context for the model, which can lead to \
    more detailed and relevant outputs.
    """

    prompt = f""" 
    Summarize the text delimited by triple backticks \
    into a single sentence.
    ```{text}```
    """

    messages = [{"role": "user", "content": prompt}]
    response = fetch_chat_completion(client, messages)
    print(response)


# Tactic 2: Ask for a structured output
#   -- JSON, HTML
#
def test_chat_completion_json_deeplearningai_tactic_2():
    prompt = f"""
    Generate a list of three made-up book titles along \
    with their authors and genres. \
    Provide them in JSON format with the following keys: \
    book_id, title, author, genre.
    """

    messages = [{
        "role": "user",
        "content": prompt
    }]

    try:
        response = fetch_chat_completion_json(client, messages)
    except Exception:
        assert False, "An excpetion was raised"

    print(json.dumps(response.choices[0].message.content, indent=4))


def test_chat_completion_json_openaidoc():
    prompt = f"""
    Generate a list of three made-up book titles along \
    with their authors and genres. \
    Provide them with the following keys: \
    book_id, title, author, genre.
    """

    messages = [
        { 
            "role": "system",
            "content": "you are helpful assisstant designed to output JSON"
        }, 
        {
            "role": "user",
            "content": prompt
        }]

    try:
        response = fetch_chat_completion_json(client, messages)
    except Exception:
        assert False, "An excpetion was raised"

    print(json.dumps(response.choices[0].message.content, indent=4))


# Tactic 3: Ask the model to check whether conditions are satisfied
# Tactic 4: "Few-shot" prompting
#
#
# Principle 2: Give the model time to “think”
# 

