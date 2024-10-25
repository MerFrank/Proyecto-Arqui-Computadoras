from sumaBin import *
from resta import *
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
    for i in range((len(numBi1))):
        
        if (regisM[0] == regisA[0]):
            #Desplazamiento
            regisA = regisA[1:] #Fuera el pirmer elemento
            regisA = regisA + regisQ[0] #Pasamos el primer elemento de Q
            regisQ = regisQ[1:]
            #Resta
            resulSuma = restaBinaria(regisA,regisM)
            if regisA[0] == resulSuma[0] or all(c in '0' for c in resulSuma):
                regisA = resulSuma
                regisQ = regisQ + "1"
            if regisA[0] != resulSuma[0] and not all(c in '0' for c in resulSuma):
                regisQ = regisQ + "0"
        else:
            #Desplazamiento
            regisA = regisA[1:] #Fuera el pirmer elemento
            regisA = regisA + regisQ[0] #Pasamos el primer elemento de Q
            regisQ = regisQ[1:]
            resulSuma = sumaBinaria(regisA,regisM)
            if regisA[0] == resulSuma[0] or all(c in '0' for c in resulSuma):
                regisA = resulSuma
                regisQ = regisQ + "1"
            
            if regisA[0] != resulSuma[0] and not all(c in '0' for c in resulSuma):
                regisQ = regisQ + "0"
        
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