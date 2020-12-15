import requests
from random import randint
import re

# these library for loading animation
import itertools
import threading
import time
import sys

words_link = 'https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa-no-swears-medium.txt'
# loading animation 
done = False

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

def find_all(word, f):
    return [m.start() for m in re.finditer(f, word)]


t = threading.Thread(target=animate)
t.start()



words = requests.get(words_link).content.decode()
words = words.split('\n')[:-1] # [:-1] : the last value is '' we use [:-1] to delete that
time.sleep(10)
done = True


random_word = words[randint(0, len(words) - 1)]

find = ['_' for i in random_word]
while True:
    guess = input('I pick word now your turn to guess a letter: ')

    if guess in random_word:
        aa = find_all(random_word, guess)
        for i in aa:
            find[i] = guess
        print("nice: " + " ".join(find))
    else:
        print("nah: " + " ".join(find))
    if not '_' in find:
        print('gg')
        exit()

