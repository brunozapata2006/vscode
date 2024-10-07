#La división de higiene está trabajando en un control de stock para productos
#sanitarios. Debemos realizar la carga de 5 (cinco) productos de prevención de
#contagio, de cada una debe obtener los siguientes datos:
#1. El tipo (validar "barbijo", "jabón" o "alcohol")
#2. El precio: (validar entre 100 y 300)
#3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las
#1000 unidades)
#4. La marca y el Fabricante.
#Se debe informar lo siguiente:
#A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
#B. Del ítem con más unidades, el fabricante.
#C. Cuántas unidades de jabones hay en total.

barbijo_mas_caro = 0
cantidad_barbijos = 0
fabricante_de_barbijos_caros = ""

item_con_mas_unidades = 0
fabricante_con_mas_items = ""

unidades_jabon = 0


for i in range (1,6):

    #destaco el tipo ya sea barbijo jabon o alcoho, y pido el producto con el input
    tipo = str(input("ingrese un tipo de producto valido: "))

    while tipo not in ("barbijo", "jabon", "alcohol"):
        tipo = input("Ingrese nuevamente un producto valido (barbijo, jabon o alcohol): ")

    #aca se ingresa el precio de los productos, siendo el minimo 100 y maximo 300
    precio = int(input("ingrese un valor valido: "))

    while not (99 < precio < 301):
        precio = int(input("Ingrese nuevamente un valor valido: "))

    #en esta linea ingresamos una cantidad de unidades, siendo el minimo 1 y el maximo 1000
    cantidad_de_unidades = int(input("ingrese una cantidad valida: "))
    
    while not ( 0 < cantidad_de_unidades < 1001):
        cantidad_de_unidades = int(input("Ingrese nuevamente una cantidad valida: "))

    #aca son solo strings pidiendo una marca
    marca = str(input("ingrese una marca: "))
    fabricante = str(input("ingrese un fabricante: "))

    #parte de barbijos PUNTO A
    if tipo == "barbijo":
        if precio > barbijo_mas_caro:
            barbijo_mas_caro = precio
            cantidad_barbijos = cantidad_de_unidades
            fabricante_de_barbijos_caros = fabricante            

    #parte de items con mas unidades PUNTO B
    if cantidad_de_unidades > item_con_mas_unidades:
        item_con_mas_unidades = cantidad_de_unidades
        fabricante_con_mas_items = fabricante

    #parte de cuántas unidades de jabones hay en total PUNTO C
    if tipo == "jabon":
        if cantidad_de_unidades > unidades_jabon:
            unidades_jabon = cantidad_de_unidades





#PUNTO A
print(f"el mas caro de los barbijos, su cantidad de barbijos es: {cantidad_barbijos} unidades", 
f"y su fabricante: {fabricante_de_barbijos_caros}")

#PUNTO B
print(f"El fabricante con mas unidades es: {fabricante_con_mas_items}," f"Sus unidades son: {item_con_mas_unidades}")

#PUNTO C
print(f"La cantidad de jabones es: {unidades_jabon}")





