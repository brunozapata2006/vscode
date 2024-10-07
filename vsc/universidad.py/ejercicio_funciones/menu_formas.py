from funciones import *
import math
lado_a = None
lado_b = None
hipotenusa = None
opcion_3 = False
opcion_4 = False
opcion_5 = False
while(True):

    opcion = int(input("Ingrese una opcion: "))
    
    match opcion:
        case 1:
            lado_a = ingresar_lados("Ingrese el lado a: ")
        case 2:
            lado_b = ingresar_lados("Ingrese el lado b: ")
        case 3:
            opcion_3 = True
            diagonal = calcular_diagonal(lado_a, lado_b)
            angulo = calcular_angulos(lado_a, lado_b)
            area = calcular_area_triangulo(lado_a, lado_b)
            perimetro = calcular_perimetro_triangulo(lado_a, lado_b)
        case 4:
            opcion_4 = True
            area_rectangulo = calcular_area_rectangulo (lado_a,lado_b)
            perimetro_rectangulo = calcular_perimetro_rectangulo (lado_a,lado_b)
            relacion_aspecto = relacion_de_aspecto_rectangulo (lado_a,lado_b)
        case 5:
            opcion_5 = True
            diagonal_cuadrado = diagonal_de_cuadrado(lado_a)
            area_cuadrado = calcular_area_cuadrado(lado_a)
            perimetro_cuadrado = calcular_perimetro_cuadrado(lado_a)
        case 6:
            if opcion_3 == True:
                print(f"Hipotenusa de rectangulo: {diagonal}")
                print(f"Angulo de rectangulo: {angulo}")
                print(f"Area de rectangulo: {area}")
                print(f"Perimetro de rectangulo: {perimetro}")
            else:   
                print('porfavor realice los calculos del caso "triangulo rectangulo"')
    
            if opcion_4 == True:
                print(f"Area de rectangulo: {area_rectangulo}")
                print(f"Perimetro de rectangulo: {perimetro_rectangulo}")
                print(f"Relacion de aspecto: {relacion_aspecto}")
            else:
                print('Por favor realice los calculos del caso "rectangulo" ')

            if opcion_5 == True:
                print(f"diagonal del cuadrado: {diagonal_cuadrado}")
                print(f"area del cuadrado: {area_cuadrado}")
                print(f"el perimetro del cuadrado es: {perimetro_cuadrado}")

            else:
                print('porfavor realice los calculos del caso "cuadrado"')
                
        case 7:
            print("Borrando datos guardados. . .")
            opcion_3 = False
            opcion_4 = False
            opcion_5 = False
        case 8:
            print("Saliendo. . .")
            break
