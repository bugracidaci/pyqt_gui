
from pydub import AudioSegment
from pydub.playback import play

audio=AudioSegment.from_wav("kamerayayaklas.wav","wav")
play(audio)
