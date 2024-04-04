from pathlib import Path
import os


def bienvenida(directorio, num_recetas) -> None:
    print(f"""
    Bienvenido!
    La carpeta de recetas se encuentra en: {directorio}
    Tienes un total de {num_recetas} recetas.
    """)


def menu() -> int:
    eleccion: int = 0
    while eleccion not in range(1, 7):
        menu = """
        [1] Leer receta
        [2] Crear nueva receta
        [3] Crear nueva categoría
        [4] Eliminar receta
        [5] Eliminar categoría
        [6] Salir
        """
        print(menu)
        eleccion = input("Ingresa tu selección\n>>>")
        os.system('cls')

        if eleccion < 1 and eleccion > 6:
            print("Elegiste una opción inválida")
        else:
            return eleccion


def ejecucion(eleccion):
    while eleccion != 6:
        match(eleccion):
            case 1:
                leer_receta()
            case 2:
                crear_receta()
            case 3:
                crear_categoria()
            case 4:
                eliminar_receta()
            case 5:
                eliminar_categoria()
            case 6:
                salir()


def leer_receta(archivo) -> str:
    F = open(archivo, 'r')
    lectura = F.read()
    F.close()
    return lectura


def crear_receta(direccion) -> None:
    F = open(direccion, 'w')
    F.close()


def crear_categoria():
    base = Path.home()
    guia = Path(base, "Recetas")


def eliminar_receta() -> None:
    base = Path.home()
    guia = Path(base, "Recetas")


def eliminar_categoria() -> None:
    base = Path.home()
    guia = Path(base, "Recetas")


def salir():
    os._exit(0)


bienvenida('XD', '2')
menu()
