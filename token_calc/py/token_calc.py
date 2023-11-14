import tiktoken
from enum import Enum
from typing import List

class EncodingName(Enum):
    CL100K_BASE = "cl100k_base"
    P50K_BASE = "p50k_base"
    R50K_BASE = "r50k_base"

class ModelName(Enum):
    GPT4 = "gpt-4"
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    TEXT_EMBEDDING_ADA_002 = "text-embedding-ada-002"
    TEXT_DAVINCI_002 =  "text-davinci-002"
    TEXT_DAVINCI_003 = "text-davinci-003"


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

