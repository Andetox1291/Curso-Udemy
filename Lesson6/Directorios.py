import os
from pathlib import Path

# ruta = 'C:\\Users\\Stand\\OneDrive\\Documentos\\Programacion\\Python\\Curso Udemy\\Lesson6\\prueba.txt'
# cambio = os.chdir('C:\\Users\\Stand\\Desktop\\tempo')
# nueva_carp = os.makedirs('C:\\Users\\Stand\\Desktop\\tempo\\otra')
# archivo = open('otro_texto.txt')
# print(archivo)

# elemento = os.path.basename(ruta)
# elemento2 = os.path.dirname(ruta)
# elemento3 = os.path.split(ruta)

# os.rmdir('C:\\Users\\Stand\\Desktop\\tempo\\otra')

# otro_archivo = open('C:\\Users\\Stand\\Desktop\\tempo\\otro_texto.txt', 'r')

# print(otro_archivo.read())

# carpeta = Path('C:/Users/Stand/Desktop/tempo')
# archivo = carpeta / 'otro_texto.txt'

carpeta = Path('C:/Users/Stand/Desktop/tempo') / 'otro_texto.txt'

mi_archivo = open(carpeta)
print(mi_archivo.read())
