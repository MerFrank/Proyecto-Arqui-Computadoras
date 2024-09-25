#SOLO FUNCIONA CON NÚMEROS ENTEROS

def DecBin(numDeci):
    if(numDeci == 0):
        return ""
    else:
        residuo = numDeci % 2
        numBi = str(residuo) 
        return DecBin(numDeci // 2) + numBi 
        #REGRESA UNA CADENA


# Hola, la variable numBi es por pura salud mental de saber
# que el resultado se esta guardando en una variable.
# Se puede quitar esa variable y poner el str(residuo)  
# en el return despúes de la llamada a la function

#PRUEBAS

a = 20
b = 5
res1 = DecBin(a)
res2 = DecBin(b)
print("20 en binarios es: "+res1)
print("5 en binarios es: "+res2)