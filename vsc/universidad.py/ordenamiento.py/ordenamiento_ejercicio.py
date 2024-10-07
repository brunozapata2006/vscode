#1- Realizar una función que ordene una lista de entero en orden ascendente o
# descendente dependiendo de un parámetro que se le envíe, la función debe retornar
# la cantidad de cambios que se realizaron.

#lista = [5,3,4,1,2]

def ordenar_lista_enteros(lista : list, orden : bool = True):

    contador_cambios = 0

    for i in range(len(lista)):
        valor_minimo = lista[i]
        indice_minimo = i

        for j in range(i + 1, len(lista)):
            if orden == True:
                if lista[j] < orden:
                    valor_minimo = lista[j]
                    indice_minimo = j
                else:
                    if lista[j] > orden:
                        valor_minimo = lista[j]
                        indice_minimo = j

        contador_cambios += 1
        aux = lista[i]
        lista[i] = valor_minimo
        lista[indice_minimo] = aux

    return contador_cambios


# 2- Realizar una función que ordene una lista de nombres de la A-Z o viceversa
# dependiendo de un parámetro que se le envíe, la función debe retornar la cantidad
# de cambios que se realizaron.

listaNombres = ["ana", "maria", "julieta", "roberto", "pbel","hw"]

def ordenar_lista_nombres(lista : list, orden : bool = True):
    contador_cambios = 0

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            #print(lista[i][0], lista[j][0], f"es menor? {lista[i][0] < lista[j][0]}")
            if orden == True:
                if lista[i][0] < lista[j][0]:
                    valor_minimo = lista[j]
                    indice_minimo = j
                else:
                    if lista[j][0] > lista[i][0]:
                        valor_minimo = lista[j]
                        indice_minimo = j

        contador_cambios += 1
        aux = lista[i]
        lista[i] = valor_minimo
        lista[indice_minimo] = aux

    return contador_cambios

# 3- Similar a la función anterior, se debe realizar otra que ordene una lista de
# nombres por su largo, de manera ascendente o descendente, la función debe
# retornar la cantidad de cambios que se realizaron

def ordenar_nombres_largo(lista : list, orden : bool = True):
    contador_cambios = 0

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            #print(lista[i][0], lista[j][0], f"es menor? {lista[i][0] < lista[j][0]}")
            if orden == True:
                if len(lista[i][0]) < len(lista[j][0]):
                    valor_minimo = len(lista[j])
                    indice_minimo = j
                else:
                    if len(lista[i][0]) > len(lista[j][0]):
                        valor_minimo = len(lista[j])
                        indice_minimo = j

        contador_cambios += 1
        aux = lista[i]
        lista[i] = valor_minimo
        lista[indice_minimo] = aux

    return contador_cambios

print(ordenar_nombres_largo(listaNombres))

