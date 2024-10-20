def binDec(cadena):
    if len(cadena) >=1:
         return int(cadena[0]) * (2 ** (len(cadena) - 1)) + binDec(cadena[1:])
    else:
        return 0


def com2Deci(cadenaC2):

    if not all(c in '01' for c in cadenaC2) or len(cadenaC2) < 1:
        return ("Error: La cadena debe contener solo '0' y '1' y tener al menos un elemento.")

    bitSigno = cadenaC2[0]
    cadenaValor = cadenaC2[1:]
    if (bitSigno == "0"):
        numDeci = binDec(cadenaValor)
        return numDeci
    else: 
        n = (len(cadenaC2) -1)
        limiteSuper = pow(-2,n)
        if (limiteSuper >= 0):
            limiteSuper = limiteSuper * -1
        
        deciParcial = binDec(cadenaValor)
        numDeci = limiteSuper + deciParcial
        return numDeci



# 12
# numPos = "00001100"
# numNega= "11110100"
#3
# numPos = "00000011"
# numNega= "11111101"
#4
# numPos = "00000100"
# numNega= "11111100"
# 5 bites 3 y 4
#3
# numPos = "111111101"
# numNega= "10000001"
#4
# numPos = "00000100"
# numNega= "11111100"
# res1 = com2Deci(numPos)
# res2 = com2Deci(numNega)
# print(f"el número {numPos} en decimal es: {res1}")
# print(f"el número {numNega} en decimal es: {res2}")

# if not all(c in '01' for c in cadena):
#         return "Error: La cadena debe contener solo '0' o '1'"
