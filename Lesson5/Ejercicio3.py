def repetido(*args):
    contador = 0
    for num in args:
        if args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False


print(repetido(5,6,1,0,0,9,3,5))