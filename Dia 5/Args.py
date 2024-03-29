def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total
    """
    OOOOOOORR
    return sum(args)
    """
print(suma(5,6,5,6,1,7,5))

"""Práctica sobre Argumentos Indefinidos (*args) 1

Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.


Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9)"""

def suma_cuadrados(*args):
    total = 0
    for n in args:
        total += n**2
    return total

"""Práctica sobre Argumentos Indefinidos (*args) 2

Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos)."""

def suma_absolutos(*args):
    lista = []
    total = 0
    for arg in args:
        absoluto = abs(arg)
        total += absoluto
    return total

print(suma_absolutos(1,-5,6,-10,8))

"""Práctica sobre Argumentos Indefinidos (*args) 3

Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.

La función debe devolver el siguiente mensaje:

"{nombre}, la suma de tus números es {suma_numeros}" """

def numeros_persona(nombre:str, *args):
    suma_numeros = 0
    for n in args:
        suma_numeros += n
    return f'{nombre}, la suma de tus números es {suma_numeros}'