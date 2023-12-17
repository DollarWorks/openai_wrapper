from ..common.api_key_loading import *
from audio_define import *
from openai import OpenAI


def convert_text_to_audio(client: OpenAI,
                          input: str,
                          output_filepath: str = "test.mp3",
                          voice=VoiceType.ALLOY.value,
                          model=AudioModel.TTS_1.value):
    response = client.audio.speech.create(
        model=model,
        voice=voice,
        input=input
    )

    response.stream_to_file(output_filepath)
