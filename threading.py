import threading
def worker(num):
    print("worker: %s" % num)
threads = []
for i in range(5):
    #iteracines que hace el for
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    #el punto start inicia el hilo
    t.start()