mi_texto = "Esta es una prueba"
resultado = mi_texto.index("a", 5, 12)
#resultado = mi_texto.rindex("a")
print(resultado)

palabra = "ordenador"
busca = palabra.index("n")
print(busca)

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.index("práctica")
print(resultado) 

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.rindex("práctica")
print(resultado)