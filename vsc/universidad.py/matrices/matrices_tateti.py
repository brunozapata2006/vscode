import random
def mostrar_matriz(matriz: list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j],end=' | ')
        print('')

        
def inicializar_matriz(cantidad_filas:int, cantidad_columnas:int) -> list:
    matriz = []
    for _ in range(cantidad_filas):
        fila = [0] * cantidad_columnas
        matriz += [fila]

    return matriz

def cara_cruz() -> str:
    resultado = random.choice(["cara", "cruz"])
    return resultado

def cargar_matriz_aleatoriamente(matriz : list, juega: int):
    if juega == 1:
        fila = int(input("indice de fila = "))
        columna = int(input("indice de columna = "))
        while matriz[fila] [columna ] != 0:
            fila = int(input("indice de fila = "))
            columna = int(input("indice de columna = "))
        dato = "X"
        matriz [fila][columna] = dato
    else:
        fila = random.choice([0, 1, 2])
        columna = random.choice([0, 1, 2])
        while matriz[fila] [columna ] != 0:
            fila = random.choice([0, 1, 2])
            columna = random.choice([0, 1, 2])
        dato = "O"
        matriz [fila][columna] = dato
    mostrar_matriz(matriz)

def verificar_matriz(matriz: list) -> bool:
    ganador = False
    for i in range(len(matriz)):
        for x in range(len(matriz [0])):
            if matriz[i][x] == matriz[i][x-1] and matriz[i][x] == matriz[i][x-2] and matriz[i][x] == "X":
                ganador = True
            elif matriz[x][i] == matriz[x-1][i] and matriz[x][i] == matriz[x-2][i] and matriz[x][i] == "X":
                ganador = True
            elif matriz[x][i] == matriz[i][x] and matriz[x-1][i-1] == matriz[i-1][x-1] and matriz[x-2][i-2] == matriz[i-2][x-2] and matriz[i][x] == "X":
                ganador = True
    return ganador
    

def jugar_tateti():
    matriz_nueva = inicializar_matriz(3,3)
    eleccion = input("Eleji cara o cruz: ")
    resultado = cara_cruz()
    if eleccion == resultado :
        acierto = 1
        print("Empieza jugador")
        cargar_matriz_aleatoriamente(matriz_nueva, acierto)
    else:
        acierto = 0
        print("Empieza el bot")
        cargar_matriz_aleatoriamente(matriz_nueva, acierto)

    while True:
        if verificar_matriz(matriz_nueva) == True:
            print("Ganaste")
            break
        elif acierto == 1:
            acierto = 0
            cargar_matriz_aleatoriamente(matriz_nueva, 0)
            print("  ")
        else:
            acierto = 1
            cargar_matriz_aleatoriamente(matriz_nueva, 1)
            print("  ")
        
jugar_tateti()