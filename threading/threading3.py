import threading
  
# variable global  x
x = 0
  
def incremento():
    """
    función para incrementar la variable global x
    """
    global x
    x += 1
  
def tareadelHilo():
    """
    tarea por hilo.
    llama a la función de incremento 100000 veces.
    """
    for _ in range(100000):
        incremento()
  
def tareaPrincipal():
    global x
    # establecer la variable global x como 0
    x = 0
  
    # creando hilos
    t1 = threading.Thread(target=tareadelHilo)

    t2 = threading.Thread(target=tareadelHilo)

  
    # iniciando hilos
    t1.start()
    t2.start()
  
    # esperar hasta que los hilos terminen su trabajo
    t1.join()
    t2.join()
  
if __name__ == "__main__":
    for i in range(10):
        tareaPrincipal()
        print("Iteración {0}: x = {1}".format(i,x))