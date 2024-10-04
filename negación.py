from comp2 import *
# IMPORTANTE AGREGAR UN PUNTO DE CONTRO EN CASO DE QUE SE METAN NUMETOS EN LUGAR DE CADENAS

#Esta funcion regresa la posición de un elemento(predefinido) deseado en una cadena
def PrimerUno(numBi): 
    for bit in range(len(numBi)-1,-1,-1):
        # primer_uno = False
        if (numBi[bit] == "1"):
            # primer_uno = True
            indice = int(bit) 
            return indice #REGRESA UN NUMERO
        
#Busca en una cadena(convetida a lista) y cambiar los 1 por 0 y los 0 por 1. CUIDADO no modifica la cadena original.
def invert(numBi,indice):
    numBi = list(numBi)
    for i in range(indice):
        if(numBi[i] == "1"):
            numBi[i] = "0"
        elif(numBi[i] == "0"):
            numBi[i] = "1"
        else:
            pass
    return ''.join(numBi) #REGRESA UNA CADENA

#Hace el proceso final de la negación 
def nega(numBi):
    if(isinstance(numBi,(int,float))):
        numBi = str(numBi)
    
    indice=PrimerUno(numBi)
    new_cadena= invert(numBi,indice)  
    nega_numBi = new_cadena
    return nega_numBi

#PRUEBAS#
# a = "123405617809" 
# a = "001111" 
# b = "011011"
# c = "0010010"

res1 = nega(binarioPri) 
res2 = nega(binarioSegun) 
# res3 = nega(c)

print(f"el negado de  {a} es: "+res1)
print(f"el negado de  {b} es: "+res2)
# print(res3)
