from repaso_arrays import *

opcion_2 = False
opcion_3 = False
opcion_4 = False
opcion_5 = False
opcion_6 = False

while (True):

    respuesta = int(input("ingrese lo que desee: "))
    lista = [0]*7

    match respuesta:
        case 1:
            cargando_datos = cargar_ingresos(lista)
        case 2:
            opcion_2 = True
            dia_mas_ingresado = determinar_dia_mas_ingresado(lista)
        case 3:
            opcion_3 = True
            dia_menos_ingresado = determinar_dia_menos_ingresos(lista)
        case 4:
            opcion_4 = True
            total = calcular_total(lista,0,7)
        case 5:
            opcion_5 = True
            promedio = calcular_promedio(lista,0,4)
            promedio = calcular_promedio(lista,5,6)
        case 6:
            opcion_6 = True
            variacion = calcular_variacion(lista)
        case 7:
            if opcion_2 == True:
                print(dia_mas_ingresado)
            if opcion_3 == True:
                print(dia_menos_ingresado)
            if opcion_4 == True:
                print(total)
            if opcion_5 == True:
                print(promedio)
            if opcion_6 == True:
                print(variacion)
            else:
                print("no ingreso nada...")
        case 8:
            break