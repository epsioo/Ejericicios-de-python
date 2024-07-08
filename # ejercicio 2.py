# ejercicio 2
# directamente se puede hacer con dos funciones pero yo le he hecho con una 
def es_palindromo(texto):
    aprobado = "Es Palindromo"
    Suspenso = "No es palindromo"

    texto_bien = texto.replace(" ", "").lower()
    texto_bien_inv = texto_bien[::-1]

    if(texto_bien ==texto_bien_inv):
        return aprobado
    if(texto_bien !=texto_bien_inv):
        return Suspenso



print("Abba", es_palindromo("Abba"))
print("Reconocer", es_palindromo("Reccconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))