import os
from openai import OpenAI
from speech_to_text.speech_define import *
from common.logging_define import *


def transcript_audio_to_json(client: OpenAI, input_filepath: str, model: str = SpeechModel.WHISPER_1.value):
    audio_file = open(input_filepath, 'rb')
    transcript = client.audio.transcriptions.create(
        model = model,
        file = audio_file
    )
    return transcript


def transcript_audio_to_text(client: OpenAI, input_filepath: str, model: str = SpeechModel.WHISPER_1.value):
    try:
        _check_file(input_filepath)

        audio_file = open(input_filepath, 'rb')
        transcript = client.audio.transcriptions.create(
            model = model,
            file = audio_file,
            response_format="text"
        )
        return transcript

    except ValueError as e:
        LOG_D(f"check input file failed")


def _check_file(file_path: str):
    file_extension = file_path.split('.')[-1].lower()

    if file_extension not in [media_type.value for media_type in MediaType]:
        raise ValueError(f"The file extension is not support: {file_path}")

    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)

    if file_size_mb > 25:
        raise ValueError(f"The file size is over 25MB: {file_size_mb}")
