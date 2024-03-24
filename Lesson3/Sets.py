#mi_set = set([1,2,3,4,5])
#print(2 in mi_set)

# otro_set = {1,2,3}
# print(type(otro_set))
# print(otro_set)

#print(mi_set[0]) no son suscribibles ni modificables


s1 = {1,2,3}
s1.add(4)
s1.remove(3)
s1.discard(6) #no tira error si descartas un elemento q no existe
s1.pop() #elimina un valor aleatorio si se deja sin parametros
s1.clear()#elimina todo el contenido set
# s2 = {3,4,5}
# s3 = s1.union(s2)
print(s1)

#Une los siguientes sets en uno solo, llamado 
#mi_set_3:
#{1, 2, "tres", "cuatro"}
#{"tres", 4, 5} 

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5} 
mi_set_3 = mi_set_1.union(mi_set_2)

#Elimina un elemento al azar del siguiente set, utilizando métodos de sets.
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.pop()

#Agrega el nombre Damián al siguiente set, utilizando métodos de sets:
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")