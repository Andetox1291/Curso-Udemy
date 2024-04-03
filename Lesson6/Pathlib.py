from pathlib import Path, PureWindowsPath

carpeta = Path(
    "C:/Users/Stand/OneDrive/Documentos/Programacion/Python/Curso Udemy/Lesson6/prueba.txt")

# print(carpeta.read_text())
# print(carpeta.name)
# print(carpeta.suffix)
# print(carpeta.stem)

ruta_win = PureWindowsPath(carpeta)
print(ruta_win)

if not carpeta.exists():
    print('Este archivo no existe')
else:
    print('Genial, sí existe')
