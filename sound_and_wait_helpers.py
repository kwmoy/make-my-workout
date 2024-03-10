import math
import os
import threading

from gtts import gTTS
from pygame import mixer

import time

from sounds_map import SoundPath


class BaseOperations:
    @staticmethod
    def wait_active_time(active_time: int):
        time.sleep(active_time)
        time.sleep(0.1)
        print("done waiting")
        pass

    @staticmethod
    def play_sound(path):
        mixer.music.load(path)
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(0.25)

    @staticmethod
    def write_text_to_mp3(audio, lgg="en"):
        tts = gTTS(text=audio, lang=lgg)
        audio_text = BaseOperations.convert_text_to_mp3_filename(audio)
        tts.save(f"{audio_text}.mp3")
        return None

    @staticmethod
    def play_words(words):
        words_mp3_path = BaseOperations.convert_text_to_mp3_filename(words)
        if os.path.exists(words_mp3_path):
            BaseOperations.play_sound(words_mp3_path)
        else:
            tts = gTTS(words, lang="en")
            tts.save(SoundPath.custom_words)
            mixer.init()
            mixer.music.load(SoundPath.custom_words)
            mixer.music.play()
            while mixer.music.get_busy():  # wait for music to finish playing
                time.sleep(1)

    @staticmethod
    def convert_text_to_mp3_filename(text):
        sounds_path = "sounds/"
        return (
            sounds_path
            + text.lower().replace(" ", "_").replace("-", "_")
            + ".mp3"
        )

    @staticmethod
    def play_words_with_delay(words, delay=1):
        time.sleep(delay)
        if isinstance(words, list):
            for word in words:
                BaseOperations.play_words(word)
        else:
            BaseOperations.play_words(words)


class ComboOperations:
    @staticmethod
    def play_words_after_time(words, wait_time=1):
        BaseOperations.wait_active_time(wait_time)
        BaseOperations.play_words_with_delay(words)
        pass

    @staticmethod
    def beep_and_play_words_after_time(num_beeps, words, wait_time=1):
        for i in range(num_beeps):
            BaseOperations.play_sound(SoundPath.ding)
        ComboOperations.play_words_after_time(words, wait_time)


def thread_with_wait(wait_time: int, thread_2):
    # Thread active
    start = time.time()

    wait_thread = threading.Thread(
        target=BaseOperations.wait_active_time, args=(wait_time,)
    )

    wait_thread.start()
    thread_2.start()

    wait_thread.join()
    thread_2.join()

    end = time.time()
    print("Execution Time: {}".format(end - start))
    return 1


def _get_exercise_introduction(exercise_name):
    return ["The next exercise is", exercise_name, "get ready"]


def rest_and_introduce_exercise(rest_time, exercise_name):
    exercise_intro = _get_exercise_introduction(exercise_name)
    thread_with_wait(
        rest_time,
        threading.Thread(
            target=ComboOperations.beep_and_play_words_after_time,
            args=(1, exercise_intro, 5),
        ),
    )


def rest_and_say_words(rest_time, words):
    thread_with_wait(
        rest_time,
        threading.Thread(
            target=ComboOperations.beep_and_play_words_after_time,
            args=(1, words, 0),
        ),
    )


def run_active_exercise(active_time):
    thread_with_wait(
        active_time,
        threading.Thread(
            target=ComboOperations.beep_and_play_words_after_time,
            args=(2, "Halfway there", math.floor(active_time / 2)),
        ),
    )


mixer.init()
