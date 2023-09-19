import threading

def hello():
    for x in range(50):
        print("Hello!")

t1 = threading.Thread(target=hello)
t1.start()

#do not go to the last statement before the finishing the thread so thread.join
t1.join()

print("this is end")