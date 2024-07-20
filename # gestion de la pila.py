# gestion de la pila
pila = []
pila.append(1)
pila.append(2)
pila.append(3)

print(pila)

ultimoelemento = pila.pop()
print(ultimoelemento)
print(pila)
print(pila[-1])
ultimoelemento = pila.pop()
ultimoelemento = pila.pop()

if not pila:
    print("esta vacia")