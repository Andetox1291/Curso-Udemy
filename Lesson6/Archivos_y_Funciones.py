# Práctica Archivos y Funciones 1

# Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).

def abrir_leer(archivo) -> str:
    F = open(archivo, 'r')
    lectura = F.read()
    F.close()
    return lectura


# Práctica Archivos y Funciones 2

# Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"

def sobrescribir(archivo) -> None:
    F = open(archivo, 'w')
    F.write('contenido eliminado')
    F.close()

# Práctica Archivos y Funciones 3

# Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.


def registro_error(archivo) -> None:
    F = open(archivo, 'a')
    F.write('se ha registrado un error de ejecución')
    F.close()
