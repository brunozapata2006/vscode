import random
def mostrar_lista(lista : list, final : str = "\n", inicio : int = 0, fin : int = None, salto : int = 1):
    if fin == None or fin > len(lista):
        fin = len(lista)
    
    for i in range(inicio, fin, salto):
        print(lista[i], end = final)

# # lista = [7, 3, 11, 2, 5, 13]

# lista = []
# for i in range(999):
#     lista.append(random.randint(1,1001))

# mostrar_lista(lista)

# lista_1 = lista.copy()
# lista_2 = lista.copy()
lista_3 = [5,3,4,1,2]
# lista_4 = lista.copy()


# contador_preguntas = 0
# contador_cambios = 0


# for i in range(len(lista_1)):
#     for j in range(i+1, len(lista_1)):
#         contador_preguntas += 1
#         if lista_1[i] > lista_1[j]:
#             contador_cambios += 1
#             aux = lista_1[i]
#             lista_1[i] = lista_1[j]
#             lista_1[j] = aux

            
# print(f"PRIMER ORDENAMIENTO: contador de preguntas: {contador_preguntas}, contador de cambios: {contador_cambios}")

contador_preguntas = 0
contador_cambios = 0

# contador_cambios_aux = 0

# for i in range(len(lista_2)):
#     control = False

#     for j in range(len(lista_2)-1-i):
#         contador_preguntas += 1
#         if lista_2[j] > lista_2[j+1]:
#             control = True
#             contador_cambios += 1
#             aux = lista_2[j]
#             lista_2[j] = lista_2[j+1]
#             lista_2[j+1] = aux
            
#     if not control:
#         break

print(f"SEGUNDO ORDENAMIENTO (BUBBLE SORT): contador de preguntas: {contador_preguntas}, contador de cambios: {contador_cambios}")

contador_preguntas = 0
contador_cambios = 0

for i in range(len(lista_3)):

    valor_minimo = lista_3[i]
    indice_minimo = i

    for j in range(i, len(lista_3)):
        contador_preguntas += 1
        if lista_3[j] < valor_minimo:
            valor_minimo = lista_3[j]
            indice_minimo = j

    contador_cambios += 1
    aux = lista_3[i]
    lista_3[i] = valor_minimo
    lista_3[indice_minimo] = aux

# print(f"TERCER ORDENAMIENTO: contador de preguntas: {contador_preguntas}, contador de cambios: {contador_cambios}")

# contador_preguntas = 0
# contador_cambios = 0

# def quick_sort(lista_a_ordenar : list) -> list:
#     global contador_preguntas
#     global contador_cambios

#     if len(lista_a_ordenar) <= 1:
#         return lista_a_ordenar
#     else:
#         pivote = lista_a_ordenar[0]

#         lista_menores = []
#         lista_mayores = []

#         for i in range(1, len(lista_a_ordenar)):
#             contador_preguntas += 1
#             if lista_a_ordenar[i] < pivote:
#                 lista_menores.append(lista_a_ordenar[i])
#             else:
#                 lista_mayores.append(lista_a_ordenar[i])

#     contador_cambios += 2
#     return quick_sort(lista_menores) + [pivote] + quick_sort(lista_mayores)

# lista_4 = quick_sort(lista_4)

print(f"CUARTO ORDENAMIENTO: contador de preguntas: {contador_preguntas}, contador de cambios: {contador_cambios}")