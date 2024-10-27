from sumaBin import *
from negación import*

def divi(numBi1, numBi2):
    #dividendo
    regisM = numBi2
    #divisor 
    regisQ = numBi1
    contador = len(numBi1)
    #Rellenar registro A
    if (regisQ[0] == "0"):
        regisA = ["0" for i in range(len(numBi1))]
    else:
        regisA = ["1" for i in range(len(numBi1))]
    regisA = "".join(regisA)
    print("\n División \n")
    print(f"El dividdendo es: {regisM}")
    print(f"El divisor es: {regisQ}")
    print(f"El registro Q0 es:; {regisQ[0]}")
    print(f"El registro A sera {regisA}")
    print(f"El contador empieza en: {contador}")
    for i in range((len(numBi1))):
        print(f"Contador {contador}")
        print(f"A: {regisA}, Q: {regisQ}, M: {regisM}")
        print(f"El signo de M es {regisM[0]} y el signo de A es {regisA[0]}")
        print("Desplazamiento de: A, Q")
        if (regisM[0] == regisA[0]):
            #Desplazamiento
            regisA = regisA[1:] #Fuera el pirmer elemento
            regisA = regisA + regisQ[0] #Pasamos el primer elemento de Q
            regisQ = regisQ[1:]
            print(f"A: {regisA}, Q: {regisQ}")
            #Resta
            print("resta A <-- A - M")
            NegaRegisM = nega(regisM)
            resulSuma = sumaBinaria(regisA,NegaRegisM)
            if regisA[0] == resulSuma[0] or all(c in '0' for c in resulSuma):
                regisA = resulSuma
                regisQ = regisQ + "1"
                print(f"Q0 <--- 1")
            if regisA[0] != resulSuma[0] and not all(c in '0' for c in resulSuma):
                regisQ = regisQ + "0"
                print(f"Q0 <--- 0")
            print(f"A: {regisA}, Q: {regisQ}")
        else:
            #Desplazamiento
            regisA = regisA[1:] #Fuera el pirmer elemento
            regisA = regisA + regisQ[0] #Pasamos el primer elemento de Q
            regisQ = regisQ[1:]
            #Suma
            print("suma A <-- A + M")
            resulSuma = sumaBinaria(regisA,regisM)
            if regisA[0] == resulSuma[0] or all(c in '0' for c in resulSuma):
                regisA = resulSuma
                regisQ = regisQ + "1"
            if regisA[0] != resulSuma[0] and not all(c in '0' for c in resulSuma):
                regisQ = regisQ + "0"
            print(f"A: {regisA}, Q: {regisQ}")
        
        contador -= 1
    
    if (numBi1[0] != numBi2[0]):
        #EL CONCIENTE SE NIEGA
        cociente = nega(regisQ)
        resto = regisA
        return resto, cociente #Regresan como tupla
    else:
        resto = regisA
        cociente = regisQ
        return resto, cociente #Regresan como tupla