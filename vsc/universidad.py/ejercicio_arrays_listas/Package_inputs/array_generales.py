def determinar_pares(lista : list, pares : bool = True) -> list:
    lista_retorno = []

    for i in range(len(lista)):
        if pares:
            if lista[i] % 2 == 0:
                lista_retorno.append(lista[i])
        else:
            if lista[i] % 2 != 0:
                lista_retorno.append(lista[i])
                
    return lista_retorno

def mostrar_lista(lista : list, final : str = "\n", inicio : int = 0, fin : int = None, salto : int = 1):
    if fin == None or fin > len(lista):
        fin = len(lista)
    
    for i in range(inicio, fin, salto):
        print(lista[i], end = final)

def sumar_lista(lista : list) -> int:
    acumulador = 0

    for i in range(len(lista)):
        acumulador += lista[i]
    
    return acumulador

def buscar_valor_maximo(lista : list) -> int:
    maximo = lista[0]

    for i in range(1, len(lista)):
        if maximo < lista[i]:
            maximo = lista[i]

    return maximo 