nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65,29,42]
ciudades = ['Lima', 'CDMX', 'Madrid']

combinados = list(zip(nombres,edades, ciudades))

for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")


print("\n\nPráctica Zip 1")

# Muestra en pantalla frases como la del siguiente ejemplo:

# La capital de Alemania es Berlín

# Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

combo = list(zip(capitales, paises))

for cap, pais in combo:
    print(f"La capital de {pais} es {cap}")

print("\n\nPráctica Zip 2")

# Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.

marcas =  ["Nike", "Gucci", "New Era"]
productos = ["Tenis", "Camisa", "Gorra"]

mi_zip = list(zip(marcas,productos))

print("\n\nPráctica Zip ")
# Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:

#     uno / um / one

#     dos / dois / two

#     tres / três / three

#     cuatro / quatro / four

#     cinco / cinco / five

# El resultado deberá seguir la estructura:

# [('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ] 

esp = [ "uno" , "dos" , "tres", "cuatro", "cinco"]
port = ["um", "dois", "três", "quatro", "cinco"]
eng = ["one", "two", "three", "four", "five"]


zip_idiomas = zip(esp,port,eng)
numeros = list(zip_idiomas)
print(numeros)