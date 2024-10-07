lista = [0]*7  
def cargar_ingresos(lista_ingresos :list)-> int :
    for i in range(len(lista_ingresos)):
        lista_ingresos[i] = int(input("ingrese el importe ganado: "))

    return lista_ingresos

print(cargar_ingresos(lista))


def determinar_dia_mas_ingresado(lista_ingresos:list)-> int:
    maximo = None
    indice_maximo = None
    for i in range(len(lista_ingresos)):
        if maximo == None or lista_ingresos[i] > maximo:
            maximo = lista_ingresos[i]
            indice_maximo = i
    
    return indice_maximo
print(determinar_dia_mas_ingresado(lista)) 


def determinar_dia_menos_ingresos(lista_ingresos:list)-> int:
    minimo = None
    indice_minimo = None
    for i in range(len(lista_ingresos)):
        if minimo == None or lista_ingresos[i] < minimo:
            minimo = lista_ingresos[i]
            indice_minimo = i 
    
    return indice_minimo


#print(determinar_dia_menos_ingresos(lista_ingresos))

# ● Calcular el total de ingresos en la semana.

def calcular_total(lista_ingresos: list, inicio: int, fin: int) -> int | float:
    total = 0
    for i in range(len(lista_ingresos)):
        if i >= inicio and i <= fin:
            total += lista_ingresos[i]

    return total


# # ● Calcular el promedio de ingresos en la semana.

def calcular_promedio(lista_ingresos: list, inicio: int, fin: int) -> int | float:
    total = calcular_total(lista_ingresos,inicio,fin)
    promedio = total / ((fin + 1) - inicio)

    return promedio

#print(calcular_promedio(lista_ingresos,0,6))
#print(calcular_promedio(lista_ingresos, 0, 4))
#print(calcular_promedio(lista_ingresos, 5, 6))

# ● Calcular el día con la mayor variación en los ingresos respecto al día
# anterior.

def calcular_variacion(lista_ingresos: list):
    bandera_variacion = 0
    indice_diferencia_mas_grande = 0
    for i in range(1, len(lista_ingresos)):
        diferencia = lista_ingresos[i] - lista_ingresos[i-1]
        if bandera_variacion == 0:
            diferencia_mas_grande = diferencia
            indice_diferencia_mas_grande = i
            bandera_variacion = 1
        elif diferencia > diferencia_mas_grande:
            diferencia_mas_grande = diferencia
            indice_diferencia_mas_grande = i

    return indice_diferencia_mas_grande

#print(calcular_variacion(lista_ingresos))
