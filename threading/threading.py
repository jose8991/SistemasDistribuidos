import threading
  
def imprimir_cubo(num):
    """
    Función para imprimir el cubo de un número
    """
    print("Cubo: {}".format(num * num * num))
  
def imprimir_cuadrado(num):
    """
    Función para imprimir el cuadrado de un número
    """
    print("Cuadrado: {}".format(num * num))
  
if __name__ == "__main__":
    # creando hilos
    t1 = threading.Thread(target=imprimir_cuadrado, args=(10,))
    t2 = threading.Thread(target=imprimir_cubo, args=(10,))
  
    # inicializando hilo 1
    t1.start()
    # inicializando hilo 2
    t2.start()
  
    # espererando hasta que el subproceso 1 se ejecute por completo
    t1.join()
    # esperendo hasta que el subproceso 2 se ejecute por completo
    t2.join()
  
    # ambos hilos fueron ejecutados completamente
    print("!Hecho¡")