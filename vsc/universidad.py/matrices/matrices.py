matriz_1 = [[4,1,-2],
            [1,2,6],
            ]

matriz_2 = [[2,1],
            [2,1],
            [2,3],
]

def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int) -> list:
    """_summary_ : Iniciamos una matriz vacia dependiendo de las filas y columnas que ingresemos

    Args:
        cantidad_filas (int): Ingresamos la cantidad de filas como enteros
        cantidad_columnas (int): Ingresamos la cantidad de columnas como enteros

    Returns:
        list: Retorna una lista con la cantidad de filas y columnas ingresadas, para hacer una matriz
    """
    matriz = []
    for _ in range(cantidad_filas):
        fila = [0] * cantidad_columnas

        matriz += [fila]
    
    return matriz

def devolver_lista(lista:list) -> bool:
    """_summary_ : Es para saber si lo que ingresa el usuario es una lista.

    Args:
        lista (list): Recibe el parametro lista 

    Returns:
        bool: Retorna un resultado, siendo este True cuando es una lista y False cuando NO
    """
    resultado = False
    if type(lista) == list:
        resultado = True
    return resultado

def validar_suma(matriz_1 : list, matriz_2 : list)-> bool:
    """_summary_ : Validamos si las matricez se pueden sumar entre si sabiendo  las filas y columnas de la misma.

    Args:
        matriz_1 (list): Recibe de parametros el valor de la matriz 1
        matriz_2 (list): Recibe de parametros el valor de la matriz 2

    Returns:
        bool : Retorna el valor de posiblidad, para saber si se pueden sumar
    """
    posibilidad = False
    if (len(matriz_1)) == (len(matriz_2)) and (len(matriz_1[0])) == (len(matriz_2[0])):
        posibilidad = True
    return posibilidad


def sumar_matrices(matriz_1 : list, matriz_2 : list) -> list:
    """_summary_ : Suma las matrices 

    Args:
        matriz_1 (list): Recibe el parametro de la primer matriz
        matriz_2 (list): Recibe el parametro de la segunda matriz

    Returns:
        list : devuelve la suma de las matrices en una lista
    """
    if devolver_lista(matriz_1) == True and devolver_lista(matriz_2) == True:
        suma_posible = validar_suma(matriz_1,matriz_2)
        if suma_posible == True:
            matriz_3 = inicializar_matriz(len(matriz_1),len(matriz_1[0]))
            for i in range(len(matriz_1)):
                for j in range(len(matriz_1[i])):
                    matriz_3[i][j] = matriz_1[i][j] + matriz_2[i][j]
                
            return matriz_3
    
def producto_matriz(matriz_1: list, matriz_2:list, producto:int)-> list:
    """_summary_ : Multiplica una matriz por un escalar (numero entero)

    Args:
        matriz_1 (list): Se ingresa el valor de la matriz 1
        matriz_2 (list): Se ingresa el valor de la matriz 2
        producto (int): Se ingresa el prodcuto q va a multiplicar a las matricez

    Returns:
        list : retorna una lista de las matrices multiplicadas
    """
    if devolver_lista(matriz_1) == True and devolver_lista(matriz_2) == True:
        suma_posible = validar_suma(matriz_1,matriz_2)
        if suma_posible == True:
            matriz_3 = inicializar_matriz(len(matriz_1),len(matriz_1[0]))
            for i in range(len(matriz_1)):
                for j in range(len(matriz_1[i])):
                    matriz_3[i][j] = matriz_1[i][j] * matriz_2[i][j]
                
            return matriz_3

def matriz_opuesta(matriz_1: list)-> list:
    """_summary_ : Se da vuelta los signos de la matriz

    Args:
        matriz_1 (list): Se ingresa la matriz que desea cambiar los signos

    Returns:
        list : Retorna la matriz opuesta.
    """
    if devolver_lista(matriz_1) == True:
        matriz_opuesta = inicializar_matriz(len(matriz_1),len(matriz_1[0]))
        for i in range(len(matriz_1)):
            for j in range(len(matriz_1[i])):
                matriz_opuesta[i][j] = matriz_1[i][j] * -1
                
        return matriz_opuesta
    
def matriz_transpuesta(matriz: list)-> list:
    """_summary: La funcion crea una matriz transpuesta haciendo un intercambio de columnas y filas

    Args:
        matriz (list): Recibe la matriz que quiere ser transpuesta

    Returns:
        list : Retorna la matriz transpuesta ya resuelta
    """
    if devolver_lista(matriz) == True:
        matriz_transpuesta = inicializar_matriz(len(matriz),len(matriz[0]))
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                matriz_transpuesta[j][i] = matriz[i][j] 

        return matriz_transpuesta
    
def posibilidad_multiplicar(matriz_a:list, matriz_b:list)-> bool:
    """_summary_
        Funcion para saber si se puede multiplicar matrices, leyendo las filas y las columnas de la misma.

    Args:
        matriz_a (list): Se ingresa la matriz a
        matriz_b (list): Se ingresa la matriz b

    Returns:
        La posibilidad de si se puede multiplicar
    """
    posibilidad = False
    if len(matriz_a) == len(matriz_b[0]):
        posibilidad = True
    
    return posibilidad


def multiplicar_matrices(matriz_a: list, matriz_b : list) -> list:
    """_summary_ : Sirve para multiplicar matricez, 

    Args:
        matriz_a (list): Se ingresa el valor de la matriz A
        matriz_b (list): Se ingresa el valor de la matriz B

    Returns:
        Retorna una LISTA con los valores multiplicados de la matriz A y B
    """
    if devolver_lista(matriz_a) == True and devolver_lista(matriz_b) == True:
        if posibilidad_multiplicar(matriz_a,matriz_b) == True:
            multiplicar_matriz = inicializar_matriz(len(matriz_a),len(matriz_b[0]))
            for i in range(len(matriz_a)):
                for j in range(len(matriz_b[0])):
                    for k in range(len(matriz_b)):
                        multiplicar_matriz[i][j] += matriz_a[i][k] * matriz_b[k][j]

    return multiplicar_matriz


def mostrar_matriz(matriz:list):
    """Muestra una matriz

    Args:
        matriz (list): Se ingresa la matriz que desea mostrarse
    
    retorno : none
    """
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]}", end=" ")
        print("")

m = (multiplicar_matrices(matriz_1,matriz_2))
print(m)


