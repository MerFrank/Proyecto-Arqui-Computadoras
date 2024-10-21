from negación import *

def restaBinaria(numBi1, numBi2):
    
    num1 = numBi1   
    num2 = numBi2
    num2 = nega(num2)
    #Proceso de suma
    resultado = ""
    resLista = list(resultado)
    acarreo = 0
    for i in range(len(num1)-1,-1,-1):
        # sumas de 1 con 1
        if (num1[i] == "1" and num2[i] == "1"):
            if (acarreo == 0):
                acarreo = 1
                resLista.append("0")
            else:
                resLista.append("1")
        elif( (num1[i] == "1" and num2[i] == "0") or (num1[i] == "0" and num2[i] == "1") ):
            if (acarreo == 0):
                resLista.append("1")
            else:
                resLista.append("0")
        else:#Este es el caso de la suma de 0 + 0
            if (acarreo == 0):
                resLista.append("0")
            else:
                acarreo = 0
                resLista.append("1")

    resultado = ''.join(resLista[::-1])
    return resultado #Regresa una cadena