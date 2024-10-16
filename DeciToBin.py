
def DecBin(numDeci):
    limite = 8

    if (numDeci < 0 ):
        numDeci = abs(numDeci)
    
    temBi = bin(numDeci)[2:]
    longitudBin = len(temBi)
    if (longitudBin > (limite -1)):
        return "El número supera el limite de los 8 bits"
    else:
        difencia = (limite -1 ) - longitudBin
        listaAux = []
        for i in range(difencia):
            listaAux.append("0")
        cadeAux = "".join(listaAux)
        numBiario = cadeAux + temBi
        return numBiario




#PRUEBAS

a = 3
b = 4
c = -4
d = 7
res1 = DecBin(a)
res2 = DecBin(b)
res3 = DecBin(c)
res4 = DecBin(d)

logn1 = len(res1)
logn2 = len(res2)
logn3 = len(res3)
logn4 = len(res4)
print(f"{a} en binarios es: "+res1 + f" de longitud {logn1}")
print(f"{b} en binarios es: "+res2 + f" de longitud {logn2}")
print(f"{c} en binarios es: "+res3 + f" de longitud {logn3}")
print(f"{d} en binarios es: "+res4 + f" de longitud {logn4}")