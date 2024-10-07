# lista_numeros = [5, 2, 6, 9, 1]

# def calcular_promedio_lista(lista : list) -> list:
#     calculo = 0
#     for i in range(len(lista)):
#         calculo += lista[i]

#     promedio = calculo / len(lista)

#     return promedio

# promedio_numeros = lista_enteros(lista_numeros)

# print(promedio_numeros)

# lista_numeros = [-5, 2, 6, 9, 1]

# def calcular_promedio_positivo(lista : int) -> list:
#     calculo = 0
#     contador_positivos = 0
#     for i in range(len(lista)):
#         if lista[i] > 0:
#             calculo += lista[i]
#             contador_positivo += 1

#     promedio = calculo / contador_positivo

#     return promedio

# promedio_numeros = lista_enteros(lista_numeros)

# print(promedio_numeros)

#Escribir una función que calcule y retorne el producto de todos los elementos de la lista
#que recibe como parámetro.

# def producto_elementos(elementos : list) -> int:
#     resultado = 1
#     for i in range(len(elementos)):
#         resultado *= elementos[i]

#     return resultado

# resultado_elementos = producto_elementos([1,2,4])

# print(resultado_elementos)

# def calcular_valor_maximo(elementos : list) -> int:

#     for i in range(len(elementos)):
#         maximo = elementos[i]
#         if maximo > elementos[i]:
#             maximo = [i]

#     return maximo

# calcular_valor = calcular_valor_maximo([2,4,5,6, 99])

# print(calcular_valor)

# Escribir una función que reciba como parámetros una lista de enteros y muestre la/las
# posiciones en donde se encuentra el valor máximo hallado.

def calcular_valor_maximo(elementos : list) -> int:

    posicion = 0

    for i in range(len(elementos)):
        maximo = elementos[i]
        if maximo > elementos[i]:
            maximo = [i]

    for i in range(len(elementos)):
        posicion = len(elementos)
        if posicion == len(elementos):
            posicion = elementos

    return posicion, maximo

calcular_valor = calcular_valor_maximo([2,3,4,3,5,6,6])

print(f"posicion -> {calcular_valor} <- valor")

# 6. Escribe una función llamada reemplazar_nombres que reciba como parámetros una lista
# de nombres, un nombre a reemplazar y su correspondiente reemplazo. La función debe
# reemplazar cada ocurrencia del nombre a reemplazar en la lista con su correspondiente
# reemplazo y luego retornar la cantidad total de reemplazos realizados.

# def remplazar_nombres(lista : list) -> str:

#     for i in range(len(lista)):
#         ingresar_nombre = input(lista.append)
        
#     return lista

# remplazo = remplazar_nombres([0]*5)

# print(remplazo)

