"""
Crea un programa que reciba un número del 1 al 20 introducido por el usuario y compruebe si está
dentro de la siguiente lista: [6,14,11,3,2,1,15,19]. Implementa una función que se asegure que el
número introducido por el usuario está en el rango indicado y otra que compruebe si está dentro
de la lista. Trata de crear las funciones de forma que puedan ser reutilizadas lo máximo posible en
otros programas

"""


# Devuelve True o False determinando que valor se encuentra entre el mínimo y el máximo.
def estaEnRango(valor, minimo, maximo):
    for num in range (minimo, maximo):
        if num == valor:
            flag = True
            break
        else:
            flag = False

    if flag:
        return True
    else:
        return False

# Devuelve True o False determinando si el valor está en la lista.
def estaEnLista(valor, lista):
    if valor in lista:
        return True
    else:
        return False


minimo=0
maximo=20
lista = [6,14,11,3,2,1,15,19]

try:
    usu_num = int(input ("Introduce un número: ")) 


    if estaEnRango(usu_num, minimo, maximo):
        print("El número está en el rango")
    else:
        print("El número no está en el rango")

    if estaEnLista(usu_num, lista):
        print("El número está en la lista")
    else:
        print("El número no está en la lista")

except ValueError:
    print("Debes introducir un número")