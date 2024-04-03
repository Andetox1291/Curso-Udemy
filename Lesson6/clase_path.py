from pathlib import Path


base = Path.home()
guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
guia2 = guia.with_name("La_Pedrera.txt")
print(guia.parent.parent.parent)
print(guia2)

guia = Path(Path.home(), "Europa")

for txt in Path(guia).glob('**/*.txt'):
    print(txt)


guia = Path("Europa", "España", "Barcelona", "Sagrada_Familia.txt")
en_europa = guia.relative_to(Path("Europa"))
en_spain = guia.relative_to(Path("Europa", "España"))
print(en_europa)
print(en_spain)


"""Práctica Path 1

Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.

Recuerda importar Path del módulo pathlib, y utilizar el método home() """

ruta_base = Path.home()

"""Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:
    
    Curso Python
        -> Dia 6
            -> practicas_path.py

Almacena el directorio obtenido en la variable ruta. No olvides importar Path."""


guia = Path("Curso Python", "Día 6", "practicas_path.py")
ruta = guia.relative_to(Path("Curso Python", "Día 6"))

"""Práctica Path 3

Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:

Almacena el directorio obtenido en la variable ruta. No olvides importar Path, y de concatenar el objeto Path que refiere a la carpeta base del usuario."""


base = Path.home()
ruta = Path(base, "Curso Python", "Día 6", "practicas_path.py")
