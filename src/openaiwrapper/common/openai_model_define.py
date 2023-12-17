from enum import Enum


class Encoding(Enum):
    CL100K_BASE = "cl100k_base"
    P50K_BASE = "p50k_base"
    R50K_BASE = "r50k_base"


class Model(Enum):
    # 2023-, gpt-4 (and gpt-4 turbo), gpt-3.5-turbo
    GPT4 = "gpt-4"
    GPT4_TURBO = 'gpt-4-1106-preview'  # support JSON repsone
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_1106 = "gpt-3.5-turbo-1106"  # support JSON response

    # 2023, babbage-002, davinci-002
    TEXT_EMBEDDING_ADA_002 = "text-embedding-ada-002"

    # 2020-2022
    # text-davinci-003, text-davinci-002, davinci, curie, babbage, ada
    TEXT_DAVINCI_003 = "text-davinci-003"
    TEXT_DAVINCI_002 = "text-davinci-002"
