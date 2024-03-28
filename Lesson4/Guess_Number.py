from random import randint

nombre:str = input("¿Cual es tu nombre? \n>>>")
vidas:int = 8
num_aleatorio:int = randint(1,100)
intentos = 0

print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo {vidas} intentos para adivinar cuál crees que es el número")

while vidas > 0: 
    print(F"Tienes {vidas} vidas.\n")
    num_user:int = int(input("Ingresa un número. \n>>>"))
    if (num_user > 100 or num_user < 1):
            print("El número que elegiste está prohibido.")
            vidas -= 1
            intentos += 1
    elif (num_user < num_aleatorio):
          print("INCORRECTO. El número que ingresaste es MENOR al número secreto.")
          vidas -= 1
          intentos += 1
    elif (num_user > num_aleatorio):
            print("INCORRECTO. El número que ingresaste es MAYOR al número secreto.")
            vidas -= 1
            intentos += 1
    elif (num_user == num_aleatorio):
           print(f"CORRECTO. SOLO TE TOMÓ {intentos} INTENTOS.")
           break
    
    if(vidas == 0):
           print("PERDISTE. TE QUEDASTE SIN VIDAS.")
           breakpoint
