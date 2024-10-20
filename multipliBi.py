from sumaBin import *
from negación import*
#from DeciToBin import *

def multiBi(numBi1, numBi2):

    #Ininiamos valores
        #Iniciar con el valor de A con 0
    regisA = ["0" for i in range(len(numBi1))]
    regisA = "".join(regisA)
    regisQ = numBi1
    regisM = numBi2
    bitQm1 = "0"
    contador = len(numBi1)
    #empezamos ciclo          NOTA: los desplazamientos se hacen a la DERECHA 
    for i in range(len(numBi1)):
        aux = bitQm1
        comprobación = regisQ[-1] + aux
        if (comprobación == "01"):
            regisA = sumaBinaria(regisA,regisM) #suma A <-- A + M
            #dezplazar
            bitQm1 = regisQ[-1]
            regisQ = regisQ[:-1]
            regisQ = regisA[-1] + regisQ #Agrega al Inicio
            regisA = regisA[:-1]# Elimina el ultimo carácter
            regisA = "1" + regisA if regisA[0] == "1" else "0" + regisA #rellenar A
            # regisA = "0" + regisA
        elif (comprobación == "10"): #caso resta y desplazar. Llamar al negado para opera
            #resta A <-- A - M (se necesita el negado de M)
            negaM = nega(regisM)
            regisA = sumaBinaria(regisA,negaM) #Pasa de lista a cadena
            #dezplazar
            bitQm1 = regisQ[-1]
            regisQ = regisQ[:-1]
            regisQ = regisA[-1] + regisQ #Agrega al Inicio
            regisA = regisA[:-1]# Elimina el ultimo carácter
            regisA = "1" + regisA if regisA[0] == "1" else "0" + regisA #rellenar A
        else:           #Caso directo a desplazar
            #dezplazar
            bitQm1 = regisQ[-1]
            regisQ = regisQ[:-1]
            regisQ = regisA[-1] + regisQ #Agrega al Inicio
            regisA = regisA[:-1]# Elimina el ultimo carácter
            regisA = "1" + regisA if regisA[0] == "1" else "0" + regisA #rellenar A
        
        contador -= 1
        
    respuesta = regisA + regisQ
    return respuesta
    


#Pruebas

# resultado = multiBi(numPrueba1,numPrueba2)
# print (f"El producto de {a} en bi es {numPrueba1} con {b} es {numPrueba2} :\n")
# print(f"{resultado}")