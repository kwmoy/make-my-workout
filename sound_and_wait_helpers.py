import math
import threading

from gtts import gTTS
from pygame import mixer

from exercise_objects import Exercise
import time

from exercises import EXERCISES
from sounds_map import SoundPath, LANG


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
    def play_words_with_delay(words, delay=1):
        time.sleep(delay)
        tts = gTTS(words, lang='en')
        tts.save(SoundPath.custom_words)
        mixer.init()
        mixer.music.load(SoundPath.custom_words)
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            time.sleep(1)


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


# def play_words_and_wait(wait_time: int, words: str):
#
#     # Thread active
#     start = time.time()
#
#     play_words_thread = threading.Thread(target=play_words_with_delay, args=(words,))
#     wait_thread = threading.Thread(target=wait_active_time, args=(wait_time,))
#
#     play_words_thread.start()
#     wait_thread.start()
#
#     play_words_thread.join()
#     wait_thread.join()
#
#     end = time.time()
#     print('Execution Time: {}'.format(end - start))
#     return 1


def thread_with_wait(wait_time: int, thread_2):
    # Thread active
    start = time.time()

    wait_thread = threading.Thread(target=BaseOperations.wait_active_time, args=(wait_time,))

    wait_thread.start()
    thread_2.start()

    wait_thread.join()
    thread_2.join()

    end = time.time()
    print('Execution Time: {}'.format(end - start))
    return 1


def _get_exercise_introduction(exercise_name):
    return f"The next exercise is {exercise_name}, get ready!"


def rest_and_introduce_exercise(rest_time, exercise_name):
    exercise_intro = _get_exercise_introduction(exercise_name)
    thread_with_wait(rest_time, threading.Thread(
        target=ComboOperations.beep_and_play_words_after_time, args=(1, exercise_intro, 5)
    )
                     )


def rest_and_say_words(rest_time, words):
    thread_with_wait(rest_time, threading.Thread(
        target=ComboOperations.beep_and_play_words_after_time, args=(1, words, 0)
    )
                     )

def run_active_exercise(active_time):

    thread_with_wait(active_time, threading.Thread(
        target=ComboOperations.beep_and_play_words_after_time,
        args=(2, "Halfway there!", math.floor(active_time/2))
    )
                     )


mixer.init()
