from enum import Enum


class AudioType(Enum):
    MP3 = "mp3"
    OPUS = "opus"  # For internet streaming and communication, low latency.
    AAC = "aac"  # For digital audio compression, preferred by YouTube, Android, iOS.
    FLAC = "FLAC"  # For lossless audio compression, favored by audio enthusiasts for archiving.


class AudioModel(Enum):
    TTS_1 = "tts-1"
    TTS_1_HD = "tts-1-hd"


class VoiceType(Enum):
    ALLOY = "alloy"
    ECHO = "ECHO"
    ONYX = "onyx"
    NOVA = "nova"
    SHIMMER = "shimmer"
