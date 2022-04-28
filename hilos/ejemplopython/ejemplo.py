import threading
import time

def worker():
    print("inicio")
    time.sleep(2)
    print("fin")
#worker()
threads=list()
for i in range(1000000000):
    t=threading.Thread(target=worker)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
