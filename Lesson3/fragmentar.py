texto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
fragmento = texto[0:10:2]
print(fragmento)

frase = "Controlar la complejidad es la esencia de la programación"
frag = frase[:9]
print(frag)

#Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
#"Nunca confíes en un ordenador que no puedas lanzar por una ventana"

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
frag = frase[8::3]
print(frag)

#Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
#"Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"

frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
frag = frase[::-1]
print(frag)

