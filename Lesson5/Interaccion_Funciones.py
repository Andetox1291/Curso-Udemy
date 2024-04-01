from random import shuffle, randint, choice

# Lista inicial
palitos:list[str] = ['-','--','---','----']

# Mezclar Palitos
def mezclar_lista(lista:list[str]) -> list[str]:
    shuffle(lista)
    return lista

# Pedir intento
def probar_suerte() -> None:
    intento = ''
    
    while intento not in ['1','2','3','4']:
        intento = input("Elige un número del 1 al 4\n>>>")
    
    return int(intento)

# Comprobar intento
def checar_intento(lista, intento):
    if lista[intento-1] == '-':
        print("A lavar los platos.")
    else:
        print("Esta vez te has salvado")
    
    print(f"Te ha tocado {lista[intento-1]}")

# palitos_mezclados = mezclar_lista(palitos)
# seleccion = probar_suerte()
# checar_intento(palitos_mezclados, seleccion)


"""Práctica sobre Interacción entre Funciones 1

Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

    La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

    Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.

Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

Si la suma es menor o igual a 6:

    "La suma de tus dados es {suma_dados}. Lamentable"

Si la suma es mayor a 6 y menor a 10:

    "La suma de tus dados es {suma_dados}. Tienes buenas chances"

Si la suma es mayor o igual a 10:

    "La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6."""

def lanzar_dados():
    rand1 = randint(1,7)
    rand2 = randint(1,7)

    return rand1, rand2

def evaluar_jugada(n1, n2) -> str:
    suma_dados = n1 + n2

    if suma_dados <= 6:
        return(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados > 6 and suma_dados < 10:
        return(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    elif suma_dados >= 10:
        return(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

n1, n2 = lanzar_dados()
print(f"Tus dos numeros son {n1} y {n2}")
print(evaluar_jugada(n1, n2))


"""Práctica sobre Interacción entre Funciones 2

Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.

Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo."""

def reducir_lista(lista):
    mas_alto = 0
    lista_unica = []

    for num in lista:
        if num not in lista_unica:
            lista_unica.append(num)
        if num > mas_alto:
            mas_alto = num  
        
    lista_unica.remove(mas_alto)
    # lista_unica.sort()
    return lista_unica

def promedio(lista):
    suma = 0
    promedio = 0
    
    for n in lista:
        suma += n

    promedio = suma / len(lista)
    return promedio


lista_numeros = [1,2,15,7,2]
res = reducir_lista(lista_numeros)
print("%.2f" % promedio(res))

"""Práctica sobre Interacción entre Funciones 3

Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).

    Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).

    Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.

Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia."""

def lanzar_moneda():
    lista = [0,1]
    res = choice(lista)

    if res == 0:
        return "Cara"
    else:
        return "Cruz"

def probar_suerte(moneda, lista):
    if moneda == 'Cara':
        print("La lista se autodestruirá.")
        for n in lista:
            del lista[0:]
        return lista
    else:
        print("La lista fue salvada.")
        return lista

lista_numeros = [10,2,3,4,5,6,7,8,9,1]

moneda = lanzar_moneda()
print(probar_suerte(moneda,lista_numeros))