from text_generation.chat_completion import *
from openai import OpenAI
import json

client = OpenAI()


# openai test cases
def test_chat_completion():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who won the world series in 2020?"},
        {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
        {"role": "user", "content": "Where was it played?"}
    ]

    response = fetch_chat_completion(client, messages)
    assert response.choices[0] is not None
    assert response.model is not None


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
            "content": "you are helpful assistant designed to output JSON"
        },
        {
            "role": "user",
            "content": prompt
        }]

    try:
        response = fetch_chat_completion_json(client, messages)
        print(json.dumps(response.choices[0].message.content, indent=4))
    except Exception:
        assert False, "An exception was raised"
