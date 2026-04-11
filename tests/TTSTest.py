# TTSTest
# Tests relating to edge_tts and general TTS functionality. 
# This test:
# Creates a sample TTS with edge_tts, a random UK voice is chosen from the avalible list 
# Builds a radio effect ontop it with pydub
# Speaks it using pydub.playback

import asyncio
import os
import tempfile
import threading
import random

import edge_tts
from pydub import AudioSegment
from pydub.effects import compress_dynamic_range, normalize
from pydub.playback import play
from pydub.generators import WhiteNoise

import asyncio
import edge_tts


async def get_en_gb_voices():
    voices = await edge_tts.list_voices()
    
    en_gb_voices = [
        v["ShortName"]
        for v in voices
        if v["Locale"].startswith("en-GB")
    ]

    return en_gb_voices

TTSVoicesUK = asyncio.run(get_en_gb_voices())

def radioEffect(audiosegment):
        # build a radio effect over the tts
        radio = audiosegment.high_pass_filter(300)
        radio = radio.low_pass_filter(2700)
        radio = normalize(radio)
        radio = compress_dynamic_range(
            radio,
            threshold=-25.0,
            ratio=6.0,
            attack=5,
            release=50
        )
        radio = radio + 8
        noise = WhiteNoise().to_audio_segment(duration=len(radio)) - 30
        radio = radio.overlay(noise)

        radio = radio.low_pass_filter(2600)
        return radio

def _tts_worker(text: str):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
        tmp_path = tmp_file.name

    try:
        communicate = edge_tts.Communicate(text, random.choice(TTSVoicesUK))
        asyncio.run(communicate.save(tmp_path))
        audio = AudioSegment.from_file(tmp_path)

        radio = radioEffect(audio)

        play(radio)
    except Exception as e:
        print(f"TTS playback failed: {e}")
    finally:
        try:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)
        except Exception:
            pass


def tts(text: str):
    thread = threading.Thread(target=_tts_worker, args=(text,), daemon=False)
    thread.start()
    return thread



if __name__ == "__main__":
    t = tts("Speedbird one two three, reducing speed to one eighty knots, descending to 3000 feet, QNH one zero one three, squawking one two three four.")
    t.join()