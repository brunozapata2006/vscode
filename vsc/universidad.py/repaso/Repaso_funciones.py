
# 1. Escribir una función que calcule el área de un rectángulo. La función recibe la base y
# la altura y retorna el área.

# base = int(input("ingrese la base: "))
# altura = int(input("ingrese la altura: "))

# def calcular_area_rectangulo(base: int | float, altura: int | float) -> int | float:

#     """
#     ¿que hace?:

#     ¿que recibe?:

#     ¿que retorna?:
#         int | float: _description_
#     """    

#     area = base * altura

#     return area

# print(calcular_area_rectangulo(base, altura))


#radio_ingresado = int(input("ingrese el radio: "))

#2. Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.

# def calcular_circulo(radio: int | float) -> int | float:
#     return 3.14 * radio ** 2

# radio_final = (calcular_circulo(radio_ingresado))
# print (f"el radio es: ", (radio_final))

#3. Crea una función que verifique si un número dado es par o impar. 
#La función debe imprimir un mensaje indicando si el número es par o impar.

# numero = int(input("ingrese un numero: "))
# def numero_par_impar(numero: int) -> int:

#     if numero % 2:
#         numeros_impares = numero
#         print(f"su numero es impar, y es: {numero}")
#     else:
#         print(f"su numero es par, y es: {numero}")


# numero_par_impar(numero)

#4. Crea una función que verifique si un número dado es par o impar. 
#La función retorna True si el número es par, False en caso contrario.

# numero = int(input("ingrese un numero: "))
# def numero_par_impar(numero: int) -> int:

#     if numero % 2:
#         numeros = numero
#         print(False)
#     else:
#         print(True)


# numero_par_impar(numero)

#5. Define una función que encuentre el máximo de tres números. 
#La función debe aceptar tres argumentos y devolver el número más grande.


# def numero_mas_grande(i1: int, i2: int, i3: int) -> int:
#     maximo = i1

#     if i2 > maximo and i2 > i3:
#         print(f"el numero: {i2}, es el mas grade")
#     elif i3 > i2 and i3 > maximo:
#         print(f"el numero: {i3}, es el mas grade")
#     else:
#         print(f"el numero: {maximo}, es el mas grade")

# numero_maximo = numero_mas_grande(-2, 1, 2)

# 6. Diseña una función que calcule la potencia de un número. 
# La función debe recibir la base y el exponente como argumentos y devolver el resultado.


# base = int(input("ingrese la base: "))
# exponente = int(input("ingrese el exponente: "))

# def Calcular_potencia(base: int, exponente: int) -> int:
#     return base ** exponente

# print(Calcular_potencia(base, exponente))


# 7. Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

#numero_ingresado = int(input("ingrese un numero: "))
# def verificar_primo(numero: int) -> bool:

#     if numero < 2:
#         return False
#     for i in range(2, numero):
#         if numero % i == 0:
#             return False

#     return True

# es_primo = verificar_primo(10)

#print(es_primo)

#print(f"el numero ingresado fue {numero_ingresado}, entonces es {es_primo}")

# if es_primo:
#     print(f"el numero {numero_ingresado} es primo")
# else:
#     print(f"el numero {numero_ingresado} no es primo")

#8. Crear una función que (utilizando la función del punto 10), muestre todos los
#números primos comprendidos entre entre la unidad y un número ingresado como
#parámetro. La función retorna la cantidad de números primos encontrados.

# def mostrar_primos(numero_ingresado) -> int:

#     contador_primos = 0
#     for i in range(1, numero_ingresado+1):
#         if verificar_primo(i):
#             contador_primos+=1
    
#     return contador_primos


# print(f"la cantidad de numeros primos encontrados fueron: {mostrar_primos(10)}")

#9. Crear una función que imprima la tabla de multiplicar de un número recibido como
#parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir
#el rango de multiplicación. Por defecto es del 1 al 10.


#10. Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

# def numero_entero():
#     ingrese_numero_entero = int(input("ingrese un numero: "))
#     if ingrese_numero_entero < 1 or ingrese_numero_entero > 999:
#         print(f"error, reingrese nuevamente: {ingrese_numero_entero}")
        
#         return numero_entero()
    
#     return(ingrese_numero_entero)

# print(f"el numero ingresado fue {numero_entero()}")

#11. Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

# def numero_flotante() -> float:
#     ingrese_numero_flotante = float(input("ingrese un numero: "))
#     return ingrese_numero_flotante

# flotante_ingresado = numero_flotante()

# print(f"Su numero flotante es: {flotante_ingresado}")

#12. Crear una función que le solicite al usuario el ingreso de una cadena y la retorne

# def ingrese_str() -> str:
#     ingrese_cadena = str(input("ingrese un texto: "))
#     return ingrese_cadena

# texto = ingrese_str()

# print(f"el texto fue: {texto}")







