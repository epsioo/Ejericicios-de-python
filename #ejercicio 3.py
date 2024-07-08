#ejercicio 3
# eliminar los espacios en blanco de un string y devolver la lista de caracteres restantes
#contar en un dicionario cuando se repiten los caracteres de un string
# ordenar las llaves de un diccionario por el valor que tienen y devolver una lista que contienen tuplas {("a",3),("b",2),("c",4),("d",4)}
# en un listado de tuplas, devolver las tuplas que tengan el mayor valor {("a", 3), ("b", 2), ("c", 4)} -> {("c", 4)}
# los caracteres que mas se repiten con 4 repeticiones son:
# C
# D
# juntar los caracteres que más se repiten de un string 


nommbre = " te quiero mucho mi amor" 

lista =[("a ",3),("b  ",2),("c   ",4),("d  ",4)]


texto_sin_espacios= [(texto.strip(), numero) for texto, numero in lista]
print(lista)
print(texto_sin_espacios)