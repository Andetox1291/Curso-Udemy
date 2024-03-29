def chequear_3_cifras(numero) -> bool:
    return numero in range(100,1000)

def chequear_cifras(lista) -> list[int]:
    lst3 = []
    for n in lista:
        if n in range (100,1000):
            lst3.append(n)
        else: 
            pass
    return lst3


resultado = chequear_3_cifras(686)
res = chequear_cifras([55,999,600])
print(res)

"""Práctica Funciones Dinámicas 1

Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.

No invoques la función, solo es necesario definirla."""

def todos_positivos(lista_num):
    positivos = 0
    negativos = 0

    for n in lista_num:
        if n > 0:
            positivos += 1
        elif n < 0:
            negativos += 1
    
    if negativos >= 1:
        return False
    else:
        return True

lista_numeros = [10,20,34,55]

print(todos_positivos(lista_numeros))

"""Práctica Funciones Dinámicas 2

Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma."""

def suma_menores(lista:list[int]) -> int:
    suma:int = 0

    for n in lista:
        if n > 0 and n < 1000:
            suma += n

    return suma

lista_numeros = [1000, 0, 1, 2, 3]

print(suma_menores(lista_numeros))

"""Práctica Funciones Dinámicas 3

Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta."""

def cantidad_pares(lista:list[int]) -> int:
    pares:int = 0
    for n in lista:
        if n % 2 == 0:
            pares += 1
    return pares

lista_numeros:list[int] = [2,4,6,7,8,9,10]

print(cantidad_pares(lista_numeros))