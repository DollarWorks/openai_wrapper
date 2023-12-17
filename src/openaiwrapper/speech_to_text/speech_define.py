from enum import Enum


class SpeechModel(Enum):
    WHISPER_1 = "whisper-1"


class MediaType(Enum):
    MP3 = "mp3"
    MP4 = "mp4"
    MPEG = "mpeg"
    MPGA = "mpga"
    M4A = "m4a"
    WAV = "wav"
    WEBM = "webm"
