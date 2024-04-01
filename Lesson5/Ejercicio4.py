def contar_primos(num):
    cont = 0
    
    for i in range(2, num+1):
        
        for j in range(2, i):
            
            if i % j == 0:
               break
        else:
                print(f"{i} es primo")
                cont += 1
    return cont

def num_primos(numero):
    primos = [2]
    iteracion = 3

    if numero < 2:
        return 0
    
    while iteracion <= numero:
       
        for n in range(3,iteracion,2):
            
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    
    print(primos)
    return len(primos)

print(contar_primos(10))
print(num_primos(50))