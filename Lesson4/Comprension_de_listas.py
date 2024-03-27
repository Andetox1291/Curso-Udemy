
lista = [n if n*2 > 10 else 'no' for n in range(0,21,2) ] #de contar con un solo if sin else, este se coloca junto al rango
print(lista)

pies = [10,20,30,40,50]

metros = [round(m/3.281,1) for m in pies]

print(metros)