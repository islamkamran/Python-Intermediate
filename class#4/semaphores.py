import threading
import time

# limit the access to the resources like only five to the resource

semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print(f'{thread_number} is accessing')
    semaphore.acquire()
    print(f'{thread_number} was granted accesss')
    time.sleep(10)
    print(f'{thread_number} is now releasing')


for thread_number in range(1,11):
    t = threading.Thread(target=access, args=(thread_number,))
    t.start()
    time.sleep(1)