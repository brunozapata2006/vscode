# """Ejercicio 03: Define una función que encuentre el máximo de tres números. La función
# debe aceptar tres argumentos y devolver el número más grande.
#---------------------------------------------------------------------------------
#     -¿Para que sirve? Para Devolver el numero mas grande encontrado

#     - ¿que parametros acepta?:
#                           Numero 1 -> int (ingresa un valor)
#                           Numero 2 -> int (ingresa un valor)
#                           Numero 3 -> int (ingresa un valor)
#
#     - ¿que devuele? devuelve el numero mas grande
#---------------------------------------------------------------------------------

# def numero_mas_grande(i1, i2, i3: int) -> int:
#     numero_mas_grande = i1

#     if i2 > numero_mas_grande and i2 > i3:
#         numero_mas_grande = i2
#     elif i3 > numero_mas_grande:
#         numero_mas_grande = i3
#     return numero_mas_grande

# numero_maximo = numero_mas_grande(6, 12, 9)
# print(f"el numero mas grande fue:", numero_maximo)

#---------------------------------------------------------------------------------
#Ejercicio 02: Crea una función que verifique si un número dado es par o impar. La función
#debe imprimir un mensaje indicando si el número es par o impar

#     -¿Para que sirve? Para Devolver si el numero es par o impar

#     - ¿que parametros acepta?:
#                            -Numero 1 -> int
#                            -Numero 2 -> int
#     - ¿que retorna? none

# def numero_par_impar(numeros: int) -> int:

#     for i in range(1):
#         numeros = int(input("ingrese un numero: "))
#         if numeros % 2:
#             numeros_impares = numeros
#             print("su numero no es par")
#         else:
#             print("su numero es par")

# numero_par_impar(numeros=0)

#---------------------------------------------------------------------------------

#ercicio 01: Escribe una función que calcule el área de un círculo. La función debe recibir
#el radio como parámetro y devolver el área.

    # -¿Para que sirve? Para calcular el area final y el radio
    # - ¿que parametros acepta? Acepta int (enteros) y float (numeros con ,)
    # - ¿que devuele? devuelve un return que miestra el area final y el radio

# radio_ingresado = float(input("ingrese un radio: "))
# def calculo_area(radio: float) -> float: 
#     return 3.14 * radio ** 2


# area_final = calculo_area(radio_ingresado)
# print(f"el area final es {area_final}", f"y su radio es {radio_ingresado}")

#---------------------------------------------------------------------------------

# Ejercicio 04: Diseña una función que calcule la potencia de un número. La función debe
# recibir la base y el exponente como argumentos y devolver el resultado.

#     -¿Para que sirve? Para dar el resultado de la base y exponente pedido

#     - ¿qu- ie parametros acepta? 
#                           ngresa un numero 1 -> float
#                           - ingresa un numero 2 -> float
#     - ¿que devuele? devuelve un return dando el resultado de la base multiplicado con su exponente ingresado

# ingrese_la_base = float(input("ingrese un numero: "))

# ingrese_exponente = float(input("ingrese un exponente: "))

# def calcular_potencias(resultado : int) -> float:

#     resultado = ingrese_la_base ** ingrese_exponente
#     return resultado

# exponente = calcular_potencias(resultado=0)

# print(f"El resultado es: {exponente}")
