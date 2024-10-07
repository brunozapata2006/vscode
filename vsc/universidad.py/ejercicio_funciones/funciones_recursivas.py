# def calcular_factorial(numero):
#     if numero == 0:
#         resultado = 1
#     else:
#         resultado = numero * calcular_factorial(numero - 1)

#     return resultado

# def sumar_naturales(numero: int) -> int:
#     if numero == 1:
#         resultado = 1
#     else:
#         resultado = numero + sumar_naturales(numero - 1)

#     return resultado

# print(sumar_naturales(5))

# def calcular_potencia(base: int, exponente: int) -> int:
#     if exponente == 0:
#         resultado = 1
#     else:
#         resultado = base * (calcular_potencia(base, exponente - 1))

#     return resultado

# print(calcular_potencia(2, 3))

# def sumar_digitos(numero: int) -> int:
#     if numero < 10:
#         print(numero)
#         resultado = numero
#     else:
#         print(numero, numero % 10)
#         resultado = numero % 10 + sumar_digitos(numero // 10)

#     return resultado


# print(sumar_digitos(2204))

def calcular_fibonacci(numero:int)-> int:
    if numero == 0:
        resultado = 0
    elif numero == 1:
        resultado = 1
    else:
        resultado = calcular_fibonacci(numero - 2) + calcular_fibonacci(numero - 1)
    return resultado

print(calcular_fibonacci(6))
