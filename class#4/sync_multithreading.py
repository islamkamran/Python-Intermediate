# Multi points are accessing a single resource- some want to change it some want to read it.

# We apply the concept of locking in threading lock acquire and lock release

import threading
import time

x = 8192

lock = threading.Lock()

def double():
    # access out side the function scope
    global x,lock
    lock.acquire()
    while x <  16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("reached maximum")
    lock.release()
def halve():
    global x,lock
    lock.acquire()
    while x > 1:
        x/=2
        print(x)
        time.sleep(1)
    print("reached minimum")
    lock.release()

t1 = threading.Thread(target=halve)
t2 = threading.Thread(target=double)

t1.start()
t2.start()
    