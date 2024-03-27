from random import *

aleatorio = randint(0,50)
aleatorio2 = uniform(1,5)
aleatorio2 = round(uniform(1,5),1)
aleatorio3 = random()

colores = ['rojo','azul','verde','amarillo']
aleatorio4 = choice(colores)

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)
print(aleatorio)
print(aleatorio2)
print(aleatorio3)
print(aleatorio4)

print("\n\nPráctica Random 1")

# Implementa la función randint() de la librería random que te permita obtener un número entero del 1 al 10, y almacena dicho valor en una variable llamada aleatorio
aleatorio = randint(1,10)

print("\n\nPráctica Random 2")

# Implementa la función random() de la librería random que te permita obtener un número decimal entre 0 y 1, y almacena dicho valor en una variable llamada aleatorio

aleatorio = random()

print("\n\nPráctica Random 3")

# Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de nombres a continuación, y almacena el nombre escogido en una variable llamada sorteo.
nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)