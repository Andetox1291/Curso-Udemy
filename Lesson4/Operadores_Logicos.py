texto:str = "esta frase es breve"


# mi_bool:bool = (4 < 5) and (5 == 2 + 3)
# mi_bool:bool = 10 == 10 or 3 == 3
# mi_bool:bool = ('frase' in texto) or ('python' in texto)
mi_bool:bool = not ('a' == 'a')
print(mi_bool)

# Práctica Operadores Lógicos 1

# Crea tres variables (num1 ,  num2 y num3):

#     Dentro de num1, almacena el valor 36

#     Dentro de num2, almacena el resultado de la operación 72/2

#     Dentro de num3, almacena el valor 48

# Verifica si num1 es mayor que num2, y menor que num3. Almacena el resultado de dicha comparación en una variable llamada mi_bool.
num1 = 36
num2 = 72/2
num3 = 48

mi_bool = (num1 > num2) and (num1 < num3)

# Práctica Operadores Lógicos 2

# Crea tres variables (num1 ,  num2 y num3):

#     Dentro de num1, almacena el valor 36

#     Dentro de num2, almacena el resultado de la operación 72/2

#     Dentro de num3, almacena el valor 48

# Verifica si num1 es mayor que num2, o menor que num3. Almacena el resultado de dicha comparación en una variable llamada mi_bool.

num1 = 36
num2 = 72/2
num3 = 48

mi_bool = (num1 > num2) or (num1 < num3)

# Práctica Operadores Lógicos 3

# Verifica si las palabras almacenadas en las siguientes variables:

#     palabra1 = "éxito", y

#     palabra2 = "tecnología" 

# no se encuentran en la frase a continuación, y almacena el resultado de esta comprobación (un booleano) en una variable llamada mi_bool:

# "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"

frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = "éxito"
palabra2 = "tecnología"

mi_bool = palabra1 and palabra2 not in frase

print(mi_bool)