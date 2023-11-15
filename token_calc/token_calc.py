import tiktoken
from enum import Enum
from typing import List
from ..common import openai_model_define


def num_tokens_from_string(string: str, encoding_name: EncodingName) -> int:
    encoding = tiktoken.get_encoding(encoding_name.value)
    num_tokens = len(encoding.encode(string))
    return num_tokens


def encode_text_to_token(string: str, encoding_name: EncodingName) -> List[int]:
    encoding = tiktoken.get_encoding(encoding_name.value)
    return encoding.encode(string)


def decode_token_to_text(tokens: List[int], encoding_name: EncodingName) -> str:
    encoding = tiktoken.get_encoding(encoding_name.value)
    return encoding.decode(tokens)

