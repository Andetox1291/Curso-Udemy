texto = "Este es el texto de Andres"
resultado = texto.split()
print(resultado);

a = "aprender"
b = "python"
c = "es"
d = "genial"
e = "-".join([a,b,c,d])
print(e)

texto2 = "Este es el texto de Andres"
resultado2 = texto2.find("e")
print(resultado2);

texto3 = "Este es el texto de Andres"
resultado3 = texto3.replace("e", "x")
print(resultado3);

#Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
res = frase.upper()
print(res)

#Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.

lista_palabras = ["La","legibilidad","cuenta."]
e = " ".join(lista_palabras)
print(e)

#Reemplaza en la siguiente frase:
#"Si la implementación es difícil de explicar, puede que sea una mala idea."
#los siguientes pares de palabras:
#   "difícil" --> "fácil"
#  "mala" --> "buena"
#y muestra en pantalla la frase con ambas palabras modificadas.

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
frase2 = frase.replace("difícil", "fácil")
frase3 = frase2.replace("mala", "buena")

print(frase3)
