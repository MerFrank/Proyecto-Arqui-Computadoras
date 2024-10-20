
#Esta funcion regresa la posición de un elemento(predefinido) deseado en una cadena
def PrimerUno(numBi): 
    for bit in range(len(numBi)-1,-1,-1):
        # primer_uno = False
        if (numBi[bit] == "1"):
            # primer_uno = True
            indice = int(bit) 
            return indice #REGRESA UN NUMERO
    indice = 0
    return indice #Este es en caso de que no tenga ningun 1 en la cadena
        
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
    # new_cadena= invert(numBi,indice) if indice != 0 else 
    new_cadena= invert(numBi,indice)  
    nega_numBi = new_cadena
    return nega_numBi

#PRUEBAS#
# a = "00000" 
# a = "001111" 
# b = "011011"
# c = "0010010"

# res1 = nega(a) 
# res2 = nega(binarioSegun) 
# # res3 = nega(c)

# print(f"el negado de  {a} es: "+res1)
# print(f"el negado de  {b} es: "+res2)
# print(res3)
