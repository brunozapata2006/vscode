import math

def ingresar_lados(mensaje : str) -> int:
    """que hace la funcion: nose

    parametros:
        mensaje (str): 

    Return:
        int: 
    """
    lado = int(input(mensaje))
    return lado

def calcular_diagonal(lado_a : int|float, lado_b : int|float) -> int|float:
    diagonal = math.sqrt((lado_a**2) + (lado_b**2))
    return diagonal

def calcular_angulos (valor_a, valor_b):
    hipotenusa = calcular_diagonal(valor_a, valor_b)
    angulo_1 = math.asin(valor_a / hipotenusa)
    angulo_2 = math.acos(valor_b / hipotenusa)
    angulo_1 = math.degrees(angulo_1)
    angulo_2 = math.degrees(angulo_2)
    angulo_3 = 90
    return angulo_1, angulo_2, angulo_3

def calcular_area_triangulo(lado_a, lado_b):
    resultado = (lado_a * lado_b) / 2
    return resultado

def calcular_perimetro_triangulo(lado_a, lado_b):
    perimetro_triangulo = calcular_diagonal(lado_a, lado_b)
    return perimetro_triangulo

def calcular_area_rectangulo(lado_a,lado_b):
    area_cuadradito = (lado_a*lado_b)
    return area_cuadradito

def calcular_perimetro_rectangulo(lado_a,lado_b):
    perimetro= 2 * (lado_a+lado_b)
    return perimetro

def relacion_de_aspecto_rectangulo(lado_a,lado_b):
    relacion = (lado_a/lado_b)
    return relacion

def diagonal_de_cuadrado(lado_a):
    diagonal_cuadrado =  lado_a * math.sqrt(2)
    return diagonal_cuadrado

def calcular_area_cuadrado(lado_a):
    area_cuadrado = lado_a * lado_a
    return area_cuadrado

def calcular_perimetro_cuadrado(lado_a):
    perimetro_cuadrado = (lado_a * 4)
    return perimetro_cuadrado
