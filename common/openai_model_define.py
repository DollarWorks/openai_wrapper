from enum import Enum

class Encoding(Enum):
    CL100K_BASE = "cl100k_base"
    P50K_BASE = "p50k_base"
    R50K_BASE = "r50k_base"

class Model(Enum):
    GPT4 = "gpt-4"
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    TEXT_EMBEDDING_ADA_002 = "text-embedding-ada-002"
    TEXT_DAVINCI_002 =  "text-davinci-002"
    TEXT_DAVINCI_003 = "text-davinci-003"
    GPT4_TURBO = 'gpt-4-1106-preview'
