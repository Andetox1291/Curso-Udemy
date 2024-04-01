def num_mayor(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        mayor = num1
    elif num2 > num1 and num2 > num3:
        mayor = num2
    else:
        mayor = num3
    return mayor

def num_menor(num1,num2,num3):
    if num1 < num2 and num1 < num3:
        menor = num1
    elif num2 < num1 and num2 < num3:
        menor = num2
    else:
        menor = num3
    return menor

def num_intermedio(num1,num2,num3):
    if num1 > num2 and num1 < num3 :
        intermedio = num1
    elif num2 > num1 and num2 < num3:
        intermedio = num2
    else:
        intermedio = num3
    return intermedio

def devolver_distintos(num1, num2, num3):
    suma = num1+num2+num3
    mayor = num_mayor(num1,num2,num3)
    menor = num_menor(num1,num2,num3)
    intermedio = num_intermedio(num1,num2,num3)

    if suma > 15:
        return mayor
    elif suma < 10:
        return menor
    elif suma in range(10,16):
        return intermedio



res = devolver_distintos(6,2,3)

print(res)