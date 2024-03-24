#PUNTO NUMERO 1
texto = input("Ingresa el texto que tu quieras: ")
x,y,z = input("Ingresa tres letras que quieras buscar: ")
new_text = texto.lower()
lista = [x.lower(),y.lower(),z.lower()]
letra1 = new_text.count(lista[0])
letra2 = new_text.count(lista[1])
letra3 = new_text.count(lista[2])
resultado = f"""
La letra {x} aparece en el texto un total de {letra1} veces.
La letra {y} aparece en el texto un total de {letra2} veces.
La letra {z} aparece en el texto un total de {letra3} veces.
"""
print(resultado)

#PUNTO NUMERO 2
lista_txt = new_text.split()
print("El total de palabras en el texto es de: " + str(len(lista_txt)))

#PUNTO NUMERO 3
primera = new_text[0].upper()
ultima = new_text[-1].upper()
resultado = f'El primer caracter del texto es: {primera}. El último caracter del texto es: {ultima}.'
print(resultado)

#PUNTO NUMERO 4
lista_txt.reverse()
print(" ".join(lista_txt))

#PUNTO NUMERO 5
res = 'python' in new_text
dic = {True:"Sí", False:"No"}
print(f"La palabra 'Python' {dic[res]} se encuentra en el texto")