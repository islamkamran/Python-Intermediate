import threading
import time

# two threads 1 demon to take data from a text file and other to print the data

path = "text.txt"
text = ""
def read_file():
    global path, text
    while True:
        with open(path,"r") as f:
            text = f.read()
        time.sleep(3)

def print_loop():
    for x in range(30):
        print(text)
        time.sleep(1)


t1 = threading.Thread(target=read_file, daemon=True)
t2 = threading.Thread(target=print_loop)
t1.start()
t2.start()