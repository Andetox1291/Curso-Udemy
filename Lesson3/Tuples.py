mi_tuple = (1,2,(10,20),4)

mi_tuple = list(mi_tuple)

mi_tuple = tuple(mi_tuple)

print(type(mi_tuple))


t = (1,2,3,1)

#x,y,z = t

print(t.index(2))

#utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla, y muestra el resultado (integer) en pantalla:

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

#Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

#Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d

mi_tupla = (1, 2, 3, 4) 
a , b, c, d = mi_tupla