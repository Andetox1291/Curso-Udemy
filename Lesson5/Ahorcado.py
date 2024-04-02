from random import choice

lista_palabras: list[str] = ['guitarra', 'bentana', 'cocina', 'estrella',
                             'película', 'biblioteca', 'caramelo', 'elefante', 'teclado', 'cultura']
lista_incorrectas: list[str] = []
lista_correctas: list[str] = []
intentos = 6
aciertos = 0
juego_terminado = False


def elegir_palabra(lista_palabras) -> str:
    palabra_random: str = choice(lista_palabras)
    letras_unicas = len(set(palabra_random))

    return palabra_random, letras_unicas


def pedir_letra() -> str:
    guess = ''
    esValida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not esValida:
        guess = input('Elige una letra\n>>>').lower()
        if guess in abecedario and len(guess) == 1:
            esValida = True
        else:
            print('No has elegido una letra correcta')

    return guess


def mostrar_guiones(guess) -> None:
    lista_oculta = []

    for letra in guess:
        if letra in lista_correctas:
            lista_oculta.append(letra)
        else:
            lista_oculta.append('_')

    print(' '.join(lista_oculta))


def loop(guess, palabra_random, vidas, coincidencias) -> None:
    fin = False

    if guess in palabra_random:
        print('Acertaste una letra.')
        lista_correctas.append(guess)
        coincidencias += 1
        print(f'Letras correctas: {lista_correctas}')
    else:
        lista_incorrectas.append(guess)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_random)

    return vidas, fin, coincidencias


def perder() -> bool:
    print("Te has quedado sin vidas")
    print("La palabra era " + palabra)
    return True


def ganar(palabra_random) -> bool:
    mostrar_guiones(palabra_random)
    print("Felicidades, ganaste!!")

    return True


palabra, letras_unicas = elegir_palabra(lista_palabras)

while not juego_terminado:
    print("\n" + '*' * 20 + '\n')
    mostrar_guiones(palabra)
    print("\n")
    print(f'Letras incorrectas: {lista_incorrectas}')
    print(f'Vidas: {intentos}')
    print("\n" + '*' * 20 + '\n')

    guess = pedir_letra()
    intentos, terminado, aciertos = loop(
        guess, palabra, intentos, aciertos)

    juego_terminado = terminado
