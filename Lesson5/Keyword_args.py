def suma(**kwargs):
    suma = total = 0
    for clave, valor in kwargs.items():
        suma += valor
        print(f"{clave} = {valor}")

    return suma

def prueba(num1, num2, *args, **kwargs):
    print(f'el primer valor es {num1}')
    print(f'el segundo valor es {num2}')

    for arg in args:
        print(f"arg = {arg}")
    
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")


args = [100,200,300,400]
kwargs = {'x':'uno','y':'dos','z':'tres'}

prueba(15,50,*args,**kwargs)

"""Práctica sobre Argumentos Indefinidos (**kwargs) 1

Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado."""

def cantidad_atributos(**kwargs):
    total = 0
    for clave in kwargs.items():
        total += 1
    return total

"""Práctica sobre Argumentos Indefinidos (**kwargs) 2

Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo."""

def lista_atributos(**kwargs):
    n_lista = []
    for clave, valor in kwargs.items():
        n_lista.append(valor)
    return n_lista

res = lista_atributos(**kwargs)
print(res)

"""Práctica sobre Argumentos Indefinidos (**kwargs) 3

Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:

    Características de {nombre}:
    {nombre_argumento}: {valor_argumento}
    {nombre_argumento}: {valor_argumento}
    etc...

Por ejemplo:

describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:

    Características de María:
    color_ojos: azules
    color_pelo: rubio"""

def describir_persona(nombre, **kwargs):
    print(f'Características de {nombre}')
    for nom, val in kwargs.items():
        print(f'{nom}: {val}')

describir_persona("María", color_ojos="azules", color_pelo="rubio")
