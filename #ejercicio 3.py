#ejercicio 3
# eliminar los espacios en blanco de un string y devolver la lista de caracteres restantes
#contar en un dicionario cuando se repiten los caracteres de un string
# ordenar las llaves de un diccionario por el valor que tienen y devolver una lista que contienen tuplas {("a",3),("b",2),("c",4),("d",4)}
# en un listado de tuplas, devolver las tuplas que tengan el mayor valor {("a", 3), ("b", 2), ("c", 4)} -> {("c", 4)}
# los caracteres que mas se repiten con 4 repeticiones son:
# C
# D
# juntar los caracteres que más se repiten de un string
from pprint import pprint 


nommbre = " te quiero mucho mi amor mio" 



#lista =[("a ",3),("b  ",2),("c   ",4),("d  ",4)]

#texto_bien = nommbre.replace(" ", "")
def quito_espacios(texto):
    return [char for char in texto if char != " "]


def contar_caracteres(lista):
    char_dict = {}
    for _ in lista:
        if _ in char_dict:
            char_dict[_] +=1
        else:
            char_dict[_] =1
    return char_dict

def ordenar_lista(orden):
    return sorted(
        orden.items(), key=lambda key: key [1],
        reverse=True,
        )

def mayores_tuplas(mayor):
    maximo = mayor [0][1]
    respuesta = {}
    for orden in mayor:
        if maximo > orden [1]:
            break
        respuesta[orden[0]] = orden[1]
    return respuesta
def crea_mensaje(limpio):
    mensaje = "Los que mas se repiten son: \n"
    for  key, valor in limpio.items():
        mensaje += f"-{key} con {valor} repeticiones \n"
    return mensaje

def new_func(mensaje):
    return(mensaje)

ceroup = quito_espacios(nommbre)

print(ceroup)

En_lista=contar_caracteres(ceroup)
pprint(En_lista, width= 1)

ordenados = ordenar_lista(En_lista)
print(ordenados)

mayore_lista = mayores_tuplas(ordenados)
print(mayore_lista)

texto = crea_mensaje(mayore_lista)
print(texto)


#texto_sin_espacios= [(texto.strip(), numero) for texto, numero in lista]
#print(lista)
#print(texto_sin_espacios)
