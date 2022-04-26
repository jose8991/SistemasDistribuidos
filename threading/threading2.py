import threading
import os
  
def tarea1():
    print("Tarea 1 asignada al hilo: {}".format(threading.current_thread().name))
    print("ID de la tarea en ejecución del proceso 1: {}".format(os.getpid()))
  
def tarea2():
    print("Tarea 2 asignada al hilo: {}".format(threading.current_thread().name))
    print("ID de la tarea en ejecución del proceso 2: {}".format(os.getpid()))
  
if __name__ == "__main__":
  
    # imprimir el ID del proceso actual
    print("ID del proceso que ejecuta el programa principal: {}".format(os.getpid()))
  
    # imprimir el nombre del hilo principal
    print("Nombre del hilo principal: {}".format(threading.current_thread().name))
  
    # creando hilos
    t1 = threading.Thread(target=tarea1, name='t1')
    t2 = threading.Thread(target=tarea2, name='t2')  
  
    # iniciando hilos
    t1.start()
    t2.start()
  
    # esperarando hasta que terminen todos los hilos
    t1.join()
    t2.join()