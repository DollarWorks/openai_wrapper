from src.openaiwrapper.text_to_voice.wrapper import *
from src.openaiwrapper.common.openai_model_define import AudioModel, VoiceType
import os
from openai import OpenAI

client = OpenAI()


folder_path = "./output"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)


def test_tts_1():
    input = "Hello world! This is a stream test"

    convert_text_to_audio(client, input, output_filepath='./output/test1.mp3')
    assert os.path.exists("./output/test1.mp3")


def test_tts_1_hd():
    input = "Hello world! This is a stream test"
    convert_text_to_audio(client, input,
                          output_filepath='./output/test2.mp3',
                          voice=VoiceType.NOVA.value,
                          model=AudioModel.TTS_1_HD.value)
    assert os.path.exists("./output/test2.mp3")

