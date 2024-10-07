def contar_positividad(lista : list) -> int:
    contador_positivos = 0
    contador_negativos = 0

    for i in range(len(lista)):
        if lista[i] < 0:
            contador_negativos += 1
        elif lista[i] > 0:
            contador_positivos += 1

def verificar_tamanio(lista : list, valor : int, mayor : bool = True):
    contador = 0

    for i in range(len(lista)):
        if mayor:
            if lista[i] > valor:
                contador += 1
        else:
            if lista[i] < valor:
                contador += 1

    return contador
