lista = ['a','b','c']
indice = 0

for item in lista:
    print(indice, item)
    indice += 1
#No es la mejor manera de usar enumeradores
    
for item in enumerate(lista):
    print(item)

#Crea Tuples para enumerar cada item de una lista, podemos agregar el indice al for de la sig manera
for indice, item in enumerate(lista):
    print(indice, item)

#podemos usarlo fuera de loops
mis_tuples = list(enumerate(lista))
print(mis_tuples)

print("\n\nPráctica Enumerador 1")

# Imprime en pantalla frases como la siguiente:

# '{nombre} se encuentra en el índice {indice}'

# Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido mediante enumerate().

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# Puedes modificar la línea print() otorgada como ejemplo, pero las frases entregadas deberán ser iguales.
# Tip: utiliza loops!

for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}') 

print("\n\nPráctica Enumerador 2")

# Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".

# Llama a la lista obtenida con el nombre de variable lista_indices .

lista_indices = list(enumerate("Python"))
print(lista_indices)


print("\n\nPráctica Enumerador 3")


# Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

# Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos de los siguientes elementos:

#     Loops

#     Condicionales if

#     El método enumerate()

#     Métodos de strings o indexad

for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice)