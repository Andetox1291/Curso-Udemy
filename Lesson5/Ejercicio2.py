def palabras(string):
    lista = []
    for letra in string:
        if letra not in lista:
            lista.append(letra)
    lista.sort()
    return lista

print(palabras('entretenido'))