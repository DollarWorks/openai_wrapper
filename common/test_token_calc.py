from token_calc import *

def test_num_tokens_from_string():
    tokens = num_tokens_from_string("Hello world", EncodingName.CL100K_BASE)
    assert tokens == 2

def test_encode_text_to_token():
    ret = encode_text_to_token("Hello world", EncodingName.CL100K_BASE)
    assert ret == [9906, 1917]

def test_decode_token_to_text():
    tokens = [9906, 1917]
    ret = decode_token_to_text(tokens, EncodingName.CL100K_BASE)
    assert ret == "Hello world"
