from sumaBin import *
from negación import*

def multiBi(numBi1, numBi2):
    #Ininiamos valores
        #Iniciar con el valor de A con 0   REVISAR SI ESTO CAMIBIA CON EL SIGNO NEGATIGO
    regisA = ["0" for i in range(len(numBi1))]
    contador = len(numBi1)
    regisQ = numBi1
    regisM = numBi2
    bitQm1 = ["0"]
    #empezamos ciclo          NOTA: los desplazamientos se hacen a la DERECHA 
    for i in range(len(numBi1)):
        comprobación = str(numBi1[-1] + bitQm1)
                            #caso suma y desplazar
        if (comprobación == "01"):
            #suma A <-- A + M
            regisA = sumaBinaria(regisA,regisM)
            #dezplazar
            bitQm1[0] = regisQ[-1]
            regisQ = regisQ[:-1]
            regisQ = regisA[-1] + regisQ #Agrega al Inicio
            regisA = regisA[:-1]# Elimina el primer carácter
            regisA = "1" + regisA if regisA[0] == "1" else "0" + regisA #rellenar A
                        #caso resta y desplazar. Llamar al negado para opera
        elif (comprobación == "10"):
            #resta A <-- A - M (se necesita el negado de M)
            negaM = nega(regisM)
            regisA = sumaBinaria(regisA,negaM)
            #dezplazar
            bitQm1[0] = regisQ[-1]
            regisQ = regisQ[:-1]
            regisQ = regisA[-1] + regisQ #Agrega al Inicio
            regisA = regisA[:-1]# Elimina el primer carácter
            regisA = "1" + regisA if regisA[0] == "1" else "0" + regisA #rellenar A
        else:           #Caso directo a desplazar
            #dezplazar
            bitQm1[0] = regisQ[-1]
            regisQ = regisQ[:-1]
            regisQ = regisA[-1] + regisQ #Agrega al Inicio
            regisA = regisA[:-1]# Elimina el primer carácter
            regisA = "1" + regisA if regisA[0] == "1" else "0" + regisA #rellenar A
        contador -= 1
        respuesta = regisA + regisQ
        return respuesta