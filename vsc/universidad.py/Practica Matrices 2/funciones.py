import datetime
registros_mascotas =[
                    ["Luna","12345678", 3, "Perro", "Hembra", 8.5, "01/05/2024", "Vacunación anual"],
                    ["Max", "23456789", 7, "Gato", "Macho", 5.2, "28/04/2024", "Control de pulgas"],
                    ["Kiwi", "34567890", 1, "Dragón", "Hembra", 88000, "02/05/2024", "Recorte de alas"],
                    ["Rocky", "45678901", 5, "Perro", "Macho", 12.1, "30/04/2024", "Revisión dental"],
                    ["Coco", "56789012", 2, "Gato", "Hembra", 4.8, "03/05/2024", "Desparasitación"],
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

lista = []

def mostrar_lista(lista : list, final : str = "\n", inicio : int = 0, fin : int = None, salto : int = 1):
    if fin == None or fin > len(lista):
        fin = len(lista)
    for i in range(inicio, fin, salto):
        print(lista[i], end = final)

def validaciones_mascotas(lista : list):

    nombre = str(input("Ingrese el nombre de la mascota: "))

    texto_dni = str(input("Ingrese su dni: "))
    dni = (len(texto_dni))
    while dni != 8:
        texto_dni = str(input("reingrese su dni: "))
        dni = (len(texto_dni))
    
    edad = int(input("Ingrese la edad de su mascota: "))
    while edad < 0 or edad > 510:
        edad = int(input("reingrese la edad de su mascota: "))

    animal = str(input("Ingrese el animal que ustede posee en su posesion: "))
    while animal == None:
        animal = str(input("reingrese el animal que ustede posee: "))

    sexo = str(input("Ingrese el sexo de su animal: "))
    while sexo not in ("hembra", "macho"):
        sexo = str(input("Ingrese el sexo de su animal: "))

    peso = float(input("ingrese el peso de la mascota en KG: "))
    while peso < 1 or peso > 10000:
        peso = float(input("ingrese el peso de la mascota en KG: "))

    fecha_hoy = datetime.date.today()
    fecha_formato_perzonalizado = fecha_hoy.strftime("%d/%m/%Y")

    historial_medico = str(input("ingrese su historial medico: "))
    
    lista.append([nombre, texto_dni, edad, animal, sexo, peso, fecha_formato_perzonalizado,historial_medico])
    

# El programa debe permitir al veterinario:
# 1. Registrar nuevas mascotas, ingresando todos los datos requeridos.
# 2. Actualizar la información de una mascota en cada nueva visita, manteniendo un
# historial médico completo y actualizado.

def cambiar_valor(lista : list):
    
    indice_i = int(input("elija fila: "))
    columna_j = int(input("elija la columna: "))

    lista[indice_i][columna_j] = input("valor a cambiar: ")
    
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            print (lista[i][j])

#Mostrar información completa de todas las mascotas: Esta función permitirá
#visualizar todos los datos registrados de todas las mascotas atendidas en la
#veterinaria.


def informacion_mascotas(lista : list):

    for i in range(len(lista)):
        mostrar_lista(lista[i], " ║ ")
        print("")



# Mostrar información completa solo de las mascotas que superen el promedio
# de edad: Esta opción mostrará únicamente los datos de las mascotas cuya edad
# supere el promedio de edad de todas las mascotas registradas.

def mayor_promedio_edad(lista :list) -> int | float:
    contador_edad = 0
    mascotas_mayores = []

    for i in range(len(lista)):
        contador_edad += lista[i][2]

    if len(lista) > 0:
        promedio_edad = contador_edad / len(lista)
    
    for i in range(len(lista)):
        if lista[i][2] > promedio_edad:
            mascotas_mayores.append(lista[i][0])

    return mascotas_mayores

def calcular_promedio_peso(lista:list) -> int | float:
    acumulador_peso = 0
    peso_promedio = 0

    for i in range(len(lista)):
        acumulador_peso += lista[i][5]

    if len(lista) > 0:
        peso_promedio = acumulador_peso / len(lista)

    return peso_promedio

valor = mostrar_lista(registros_mascotas)
print(calcular_promedio_peso(valor))