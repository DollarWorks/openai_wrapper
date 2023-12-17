from src.openaiwrapper.speech_to_text.wrapper import *

client = OpenAI()

expect = "Here's to the crazy ones, the misfits, the rebels, the troublemakers, the round pegs in the square holes, the ones who see things differently. They're not fond of rules and they have no respect for the status quo. You can quote them, disagree with them, glorify or vilify them, about the only thing you can't do is ignore them, because they change things, they push the human race forward. While some may see them as the crazy ones, we see genius, because the people who are crazy enough to think they can change the world, are the ones who do."


def test_transcript_audio_to_json():
    result = transcript_audio_to_json(client, input_filepath="./input/thinkdifferent.mp4")

    log_d(result.text)
    assert result.text == expect


def test_transcript_audio_to_text():
    result = transcript_audio_to_text(client, input_filepath="./input/thinkdifferent.mp4")
    log_d(result)
    assert result.rstrip() == expect

