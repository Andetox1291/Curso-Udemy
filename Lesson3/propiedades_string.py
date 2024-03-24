nombre = "Carina"
#nombre[0] = "K"
print(nombre) #no pueden ser cambiados pq los strings son inmutables

n1 = "Kari"
n2 = "na"
print(n1+n2)# son concatenables
print(n1*5) #tambien son multiplicables

poema = """Mil pequeños peces blancos
como si hirviera
el color del agua""" #con tres comillas puedo imprimir un bloque de texto
#print("agua" in poema) puedo ver si una palabra aparece en el string
print(poema)
print(len(poema)) #podemos ver cuantos caracteres hay con la propiedad len()

#Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla. Por suerte, conoces que los strings son multiplicables y puedes realizar esta actividad de forma simple y elegante.
txt = "Repetición"
print(txt*15)

#Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.

#Tierra mojada,
#mis recuerdos de viaje
#entre las lluvias

txt = """Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""

print("agua" not in txt)

#Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista.

txt = "electroencefalografista"

print(len(txt))