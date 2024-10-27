import os
from DeciToBin import *
from negación import *
from sumaBin import *
from resta import *
from multipliBi import *
from divisionBi import *
from Com2toDeci import *

def pedir_numero_entero():
    while True:
        try:
            # Pedir al usuario un valor y convertirlo en entero
            numero = int(input("Por favor, ingresa un número entero: "))
            return numero
        except ValueError:
            # Si no es un número entero, mostrar un mensaje de error
            print("Error: No es un número entero válido. Intenta de nuevo.")

def menu():
    print("Ingrese dos números enteros que desea convertir en binario")
    num1 = pedir_numero_entero()
    num2 = pedir_numero_entero()
    # if not num1 or not num2: # Si está vacía, pedir un nuevo valor al usuario
    #     num1 = pedir_numero_entero()
    #     num2 = pedir_numero_entero()
    # else:
    #     #Si ya contiene valor
    #     print(f"El primer número es {num1} y el segúndo número es {num2}")
    #     respuesta = input("¿Deseas seguir usando este valor? (S/n): ").strip().lower()
    #     if respuesta == "n":
    #         num1 = pedir_numero_entero()
    #         num2 = pedir_numero_entero()

    PrimerBi =DecBin(num1)
    print(f" El primer binario es: {PrimerBi}")
    SegunBi =DecBin(num2)
    print(f" El segundo binario es: {SegunBi}")
    print("\n \n")
    print("¿Qué operación desea realizar?")
    print("(1) Suma  (2) Resta  (3) Multiplicación (4) División")
    opcion = int(input("Elija una opción :"))

    if (opcion == 1):
        respuesta = sumaBinaria(PrimerBi,SegunBi)
        print(f"La repuesta es: {respuesta}")
        aux= com2Deci(respuesta)
        print(f"En decimal es: {aux}")

    if (opcion == 2):
        respuesta = restaBinaria(PrimerBi,SegunBi)
        print(f"La repuesta es: {respuesta}")
        aux= com2Deci(respuesta)
        print(f"En decimal es: {aux}")

    if (opcion == 3):
        respuesta = multiBi(PrimerBi,SegunBi)
        print(f"La repuesta es: {respuesta}")
        aux= com2Deci(respuesta)
        print(f"En decimal es: {aux}")

    if (opcion == 4):
        resto, cociente = divi(PrimerBi,SegunBi)
        print(f"El resto de : {resto} y el cociente es {cociente}")
        cociDeci= com2Deci(cociente)
        print(f"el cociente es : {cociDeci}")
        resDeci= com2Deci(resto)
        print(f"el resto es : {resDeci}")


print("\nCalculadora de números binarios\n")
control = True
# Inicializamos las variables fuera del ciclo
while control:
    
    # num1 = None
    # num2 = None
    menu()
    op = input("¿Desea continuar? (S) Salir,  (C) Continuar ").strip().lower()
    if op == "s":
        control = False
    else:
        os.system("clear")
        