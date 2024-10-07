def pedir_entero(mensaje : str, mensaje_error : str, minimo : int | bool = False, maximo : int | bool = False) -> int:

    retorno = int(input(mensaje))

    while (minimo != False and retorno < minimo) or (maximo != False and retorno > maximo):
        retorno = int(input(mensaje_error))

    return retorno