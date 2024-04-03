archivo = open('Lesson6\\prueba.txt')

# # print(archivo.read())
# una_linea = archivo.readline()
# print(una_linea.upper())  # se pueden usar metodos de string
# una_linea = archivo.readline()
# print(una_linea.rstrip())
# una_linea = archivo.readline()
# print(una_linea)

# for l in archivo:
#     print("Aqui dice: " + l)

todas = archivo.readlines()  # genera una lista por cada linea
print(todas)  # se pueden usar los metodos de lista
# usar este metodo solo para archivos pequeños
archivo.close()

"""Práctica Abrir y Manipular Archivos 1

Abre el archivo texto.txt e imprime su contenido.

Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código"""

archivo = open('Lesson6\\texto.txt')
print(archivo.read())
archivo.close()

"""Práctica Abrir y Manipular Archivos 2

Imprime la primera línea del archivo texto.txt

No olvides abrir el archivo y cerrarlo luego de ejecutar tu código.

Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código"""

archivo = open('Lesson6\\texto.txt')
print(archivo.readline())
archivo.close()

"""Práctica Abrir y Manipular Archivos 3

Abre el archivo texto.txt e imprime únicamente la segunda línea."""

archivo = open('Lesson6\\texto.txt')
todas = archivo.readlines()
print(todas[1])
archivo.close()
