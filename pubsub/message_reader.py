import threading
import logging
import time

def reader_thread(name):
    i = 1
    s = 5
    while True:
        time.sleep(s)
        print(f'reader_thread({i}): reading message from pubsub lite, then sleep for {s} secomnds.')
        i=i+1

def start_reader():
    t = threading.Thread(target=reader_thread, args=(1,), daemon=True)
    t.start()