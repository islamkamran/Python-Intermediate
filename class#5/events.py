import threading

my_event = threading.Event()

def my_fun():
    print("Waiting for event to trigger")
    my_event.wait()
    print("performing action XYZ")

t1 = threading.Thread(target=my_fun)
t1.start()

x = input("do you want to trigger the event y/n?")
if x == 'y':
    my_event.set()
