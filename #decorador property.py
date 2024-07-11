#decorador property
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre       # aqui le vamos a dar un variable a la instancia self para que se le añada la variable de nombre
    
    def set_nombre(self, nombre):
        if nonbre.strip():
            self.__nombre = nombre
        return

    def get_nombre(self):
        return self.__nombre


perro1 = Perro(" ")
print(perro1)