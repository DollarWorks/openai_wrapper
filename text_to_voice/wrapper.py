from pathlib import Path
from openai import OpenAI
from common.api_key_loading import *
from constant import *

def text_to_audio(client: OpenAI, 
                  intput: str, 
                  output_path: str = ".",
                  voice = VoiceType.ALLOY.value,
                  model = AudioModel.TTS_1.value):
    response = client.audio.speech.create(
        model=model, 
        vocice=voice,
        input=input
    )

    response.stream_to_file(output_path)