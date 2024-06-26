archivo = open('Lesson6\\prueba.txt', 'a')
# archivo.write('Soy el nuevo texto\n')
# archivo.write('Hola mundo')
# archivo.write('''
#               Hola
#               mundo
#               aqui
#               estoy''')
# archivo.writelines(['hola', 'mundo', 'aqui', 'estoy'])
# lista = ['hola', 'mundo', 'aqui', 'estoy']
# for p in lista:
#     archivo.writelines(p + '\n')

archivo.write('bienvenido')
archivo.close()

"""Práctica Crear y Escribir Archivos 1

Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura."""

mi_archivo = open("Lesson6\\mi_archivo.txt", 'w')
mi_archivo.write('Nuevo texto')
mi_archivo.close()
mi_archivo = open('Lesson6\\mi_archivo.txt', 'r')
print(mi_archivo.readline())
mi_archivo.close()


"""Práctica Crear y Escribir Archivos 2

Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura."""

mi_archivo = open("Lesson6\\mi_archivo.txt", "a")
mi_archivo.write("Nuevo inicio de sesión")
mi_archivo.close()
mi_archivo = open("Lesson6\\mi_archivo.txt", "r")
print(mi_archivo.read())


"""Práctica Crear y Escribir Archivos 3

Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

Imprime el contenido completo de "registro.txt" al finalizar.

Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás cerrar el archivo en modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido."""

archivo = open('Lesson6\\registro.txt', 'a')
registro_ultima_sesion = ["Federico", "20/12/2021",
                          "08:17:32 hs", "Sin errores de carga"]
for r in registro_ultima_sesion:
    archivo.writelines(r + '\t')
archivo.close()

archivo = open('Lesson6\\registro.txt', 'r')
print(archivo.read())
