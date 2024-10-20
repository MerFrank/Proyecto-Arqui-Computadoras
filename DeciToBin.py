from negación import *
def DecBin(numDeci):
    if not isinstance (numDeci,int) or isinstance(numDeci,bool):
        return "Error: Variable no valida"
    
    limite = 8
    numNega = False

    if (numDeci < 0 ):
        numDeci = abs(numDeci)
        numNega = True
    
    temBi = bin(numDeci)[2:]
    longitudBin = len(temBi)
    if (longitudBin >= limite):
        return f"El número supera el limite de los {limite} bits"
    else:
        difencia = limite - longitudBin
        listaAux = []
        for i in range(difencia):
            listaAux.append("0")
        cadeAux = "".join(listaAux)
        numBiario = cadeAux + temBi
        if (numNega):
            numBiario = nega(numBiario)
        return numBiario



#PRUEBAS

# a = 3
# b = True
# c = 12
# d = 7
# numPrueba1 = DecBin(a)
# numPrueba2= DecBin(b)
# logn1 = len(numPrueba1)
# logn2 = len(numPrueba2)
# print(f"{a} en binarios es: "+numPrueba1 + f" de longitud {logn1}")
# print(f"{b} en binarios es: "+numPrueba2 + f" de longitud {logn2}")
# res3 = DecBin(c)
# res4 = DecBin(d)

# logn3 = len(res3)
# logn4 = len(res4)
# print(f"{a} en binarios es: "+res1 + f" de longitud {logn1}")
# print(f"{b} en binarios es: "+res2 + f" de longitud {logn2}")
# print(f"{c} en binarios es: "+res3 + f" de longitud {logn3}")
# print(f"{d} en binarios es: "+res4 + f" de longitud {logn4}")