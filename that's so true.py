import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("Made it out alive, but I think I lost it", 0.03),
        ("Said that I was fine, said it from the coffin", 0.04),
        ("Remember how I died when you started walking?", 0.04),
        ("That's my life, that's my life", 0.05),
        ("\nI'll put up a fight, taking out my earrings", 0.06),
        ("Don't you know the vibe? Don't you know the feeling?", 0.04),
        ("You should spend the night, catch me on your ceiling", 0.05),
        ("That's your prize, that's your prize Well", 0.05)
    ]
    delays = [0.3, 2.2, 3.3, 5.3, 7.6, 9.0, 10.2, 15.3]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
