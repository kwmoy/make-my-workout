import threading
import time
from pygame import mixer
from gtts import gTTS
from sound_and_wait_helpers import play_words_with_delay





def calc_square(numbers):
    for n in numbers:
        print(f'\n{n} ^ 2 = {n*n}')
        time.sleep(0.1)

def calc_cube(numbers):
    for n in numbers:
        print(f'\n{n} ^ 3 = {n*n*n}')
        time.sleep(0.1)

# start = time.time()
numbers = [2, 3, 5, 8,1,1,1,1]
# start = time.time()
# calc_square(numbers)
# calc_cube(numbers)
# end = time.time()

# print('Execution Time: {}'.format(end-start))
start = time.time()

square_thread = threading.Thread(target=calc_square, args=(numbers,))
cube_thread = threading.Thread(target=calc_cube, args=(numbers,))
# play_words_thread = threading.Thread(target=play_words, args=("Photography",), daemon=True)

square_thread.start()
cube_thread.start()
# play_words_thread.start()

square_thread.join()
cube_thread.join()
# play_words_thread.join()

end = time.time()

print('Execution Time: {}'.format(end-start))
