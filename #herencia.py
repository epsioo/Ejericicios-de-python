#herencia se explica es como se aplica la herencia de clases entre distintas clases y el cual se pasa
# de una clase a otra haciendo que sea herencia multiple
class Animal:
    def comiendo(self):
        print("comiendo")

class Perro(Animal):
    def pasear(self):
        print("paseando")

perro = Perro()
perro.comiendo

class Javier(Perro):
    def programando(self):
        print("programando")

javi = Javier()
javi.comiendo