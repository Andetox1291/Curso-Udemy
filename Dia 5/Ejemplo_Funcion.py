precios_cafe:list = [('Capuchino',1.99), ('Expresso', 1.20), ('Moka', 1.9)]

def cafe_mas_caro(list_precios:list) -> tuple:
    precio_mayor:float = 0
    cafe_caro:str = ''

    for cafe,precio in list_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_caro = cafe
        else:
            pass
        

    return(cafe_caro,precio_mayor)

res = cafe_mas_caro(precios_cafe)
print(res)

cafe,precio = cafe_mas_caro(precios_cafe)

print(f"El cafe mas caro es el {cafe} cuyo precio es de ${precio}")