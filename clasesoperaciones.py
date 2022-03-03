from cmath import log 

class Intermediario:
    def Operacion(n1,n2):
        while True:
            print("1. PARA SUMAR")
            print("2. PARA RESTAR")
            print("3. PARA MULTIPLICAR")
            print("4. PARA DIVIDIR")
            print("5. PARA POTENCIAR")
            print("6. PARA LOGARITMAR")
            print("0. PARA SALIR")
            valor = int(input("INGRESE EL VALOR: "))
            if valor == 1:
                suma = n1 + n2
                return suma
            elif valor == 2:
                resta = n1 - n2
                return resta
            elif valor == 3:
                multi = n1 * n2
                return multi
            elif valor == 4:
                div = n1 / n2
                return div
            elif valor == 5:
                return pow(n1,n2)
            elif valor == 6:
                return log(n1,n2)
            elif valor == 0:
                break
    

resultado = Intermediario.Operacion(5,3)
print(resultado)