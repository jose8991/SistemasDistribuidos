from jsonrpclib import Server
from os import system
import time

def main():
    conn = Server('http://localhost:5000')

    operation = 1
    while (operation != 7) :
        system("cls")
        print ("----------------------------------")
        print("eliga la operación que quiere hacer")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potenciación")
        print("6. Logaritmo")
        print("7. Salir")
        option = input("\n\nElija una Opcion:")
        op = int(option)
        if (op  < 7 and op  > 0):
            print ("Digite numero 1: ")
            Number1=int(input())
            print ("Digite numero 2: ")
            Number2=int(input())

            if(op  == 1):
                result = conn.sum(Number1, Number2)
            elif(op  == 2):
                result = conn.rest(Number1, Number2)
            elif(op  == 3):
                result = conn.mult(Number1, Number2)
            elif(op  == 4):
                result = conn.div(Number1, Number2)
            elif(op  == 5):
                result = conn.pot(Number1, Number2)
            elif(op  == 6):
                result = conn.log(Number1, Number2)

            print('La respuesta de la operación es: ', result)
            
            stop= int(input("¿Desea continuar haciendo operaciones? 1. Si 2.No \n"))
            if(stop == 2):
                op  = 7
        elif(op  > 7 or op  < 1):
            print('Escriba una opción valida')
            time.sleep(2)

if __name__ == '__main__':
    main()