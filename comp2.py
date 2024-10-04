from DeciToBin import *

def complemento(num1, num2):
    #num1 sera siempre el numero más largo 
    
    #Convertir número decimal en binario, este es una cadena
    numBi1 = DecBin(num1)
    numBi2 = DecBin(num2)
    #Sacamos la distancia de los números binarios 
    disNum1 = len(numBi1)
    disNum2 = len(numBi2)
        #Caso donde el num2 es el más grande o largo
    if ( disNum2 > disNum1 ):
        diferencia = disNum2 - disNum1
        listCom2 = []
        for i in range(diferencia +1): #+1 por el bit del signo
            listCom2.append("0")
            numBi1 = list(numBi1)
            numBi2 = list(numBi2)
        numBi1 = list(numBi1)
        numBi2 = list(numBi2)
        #Agregamos el bit del signo al número más grande
        numBi2.insert(0,"0")#OJO#
        #Agragamos los bits faltantes al número más pequeño
        numBi1 = listCom2 + numBi1
        numBi1 = "".join(numBi1)
        numBi2 = "".join(numBi2)
        # Regresamos ambas cadenas como una tupla
        return numBi1, numBi2 
    
    else:
        #Caso donde el num1 es el más grande o largo
        diferencia = disNum1 - disNum2
        #Crear una lista para poder rellenar los 0 faltantes
        #igualando los bits o la longitud de los números
        listCom2 = []
        for i in range(diferencia +1): #+1 por el bit del signo
            listCom2.append("0")
        
        #Covertir los números binarios para poder manipularlos
        numBi1 = list(numBi1)
        numBi2 = list(numBi2)
        #Agregamos el bit del signo al número más grande
        numBi1.insert(0,"0")#OJO#
        #Agragamos los bits faltantes al número más pequeño
        numBi2 = listCom2 + numBi2
        #Regresamos ambos números binarios de lista a cadena
        numBi1 = "".join(numBi1)
        numBi2 = "".join(numBi2)

        return numBi1, numBi2 # Regresamos ambas cadenas como una tupla
        #tupla es like una lista pero inmutable e innalterable 


#PRUEBAS

binarioPri, binarioSegun = complemento(a,b)
print(f"el com2 de {a}  es : " + binarioPri)
print(f"el com2 de {b}  es : " + binarioSegun)