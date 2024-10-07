# El programa debe permitir al usuario ingresar los siguientes datos para 10 alumnos:
# ● Nombre
# ● Edad
# ● DNI
# ● Género (M para masculino, F para femenino, NB para No Binario)
# ● Nota


lista = [
    ["Juan0", "12345678", "m", 18, 8],
    ["Juan1", "12345678", "m", 24, 10],
    ["juan2", "12345678", "m", 52, 4],
    ["juan3", "12345678", "m", 52, 2],
    ["juan4", "12345678", "m", 27, 5],
    ["Juana0", "12345678", "f", 23, 4],
    ["Juana1", "12345678", "f", 19, 10],
    ["Juana2", "12345678", "f", 20, 6],
    ["Juana3", "12345678", "nb", 26, 10],
    ["Juana4", "12345678", "f", 29, 6],
]

def ingreso_datos() -> list:

    cantidad = 0
    alumnos = []

    for _ in range(4):

        dato_nombre = str(input("ingrese su nombre: "))

        dni = str(input("ingrese su dni: "))
        leer_dni = len(dni)
        while leer_dni != 8:
            dni = str(input("Ingrese un dni valido: "))
            leer_dni = len(dni)

        genero = str(input("ingrese su genero: "))
        while genero not in ("m","f","nb"):
            genero = str(input("reingrese un genero valido: "))

        edad = int(input("ingrese su edad: "))
        while 18 > edad or edad > 99:
            edad = int(input("ingrese una edad valida: "))

        nota = int(input("ingrese su nota, no mienta que lo sabemos: "))
        while nota > 10 or nota < 1:
            nota = int(input("Te dije que lo sabemos, reingrese su nota porfavor: "))
        

        alumnos.append([dato_nombre, edad, dni, genero, nota])
        cantidad += 1

    return alumnos



def mostrar_matriz(estudiantes: list) -> list:
    for i in range(len(estudiantes)):
        for j in range(len(estudiantes[i])):
            print(estudiantes[i][j], end=' | ')
        print("")


def promediar_edad(estudiantes:list)-> float | int:
    suma_edad = 0
    for i in range(len(estudiantes)):
        suma_edad += estudiantes[i][3]
    #    if estudiantes == 0:
    #        return estudiantes

    return suma_edad / len(estudiantes)

def nota_promocion(estudiantes:list) -> float | int:
    contador = 0
    for i in range(len(estudiantes)):
        if estudiantes[i][4] > 5:
            contador += 1
            
    return contador

def nota_aprobar(estudiantes:list) -> float | int:
    contador = 0
    for i in range(len(estudiantes)):
        if estudiantes[i][4] > 3 and estudiantes[i][4] < 6:
            contador += 1

    return contador

def nota_desaprobados(estudiantes:list) -> float | int:
    contador = 0
    for i in range(len(estudiantes)):
        if estudiantes[i][4] < 4:
            contador += 1
        #else:
        #    promedio_masculino == 0
        #    return promedio_masculino
    return contador

def promedio_nota_masculino(estudiantes:list) -> float | int:
    promedio_masculinos = 0
    sumar_notas = 0
    for i in range(len(estudiantes)):
        if estudiantes[i][2] == ("m"):
            sumar_notas += estudiantes[i][4]
            promedio_masculinos += 1
        #else:
        #    promedio_masculino == 0
        #    return promedio_masculino

    return sumar_notas / promedio_masculinos


def porcentaje_alumnas_promocionadas(estudiantes:list):
    alumnas_promocionadas = 0
    alumnas = 0
    for i in range(len(estudiantes)):
        if estudiantes[i][2] == "f":
            alumnas += 1
            if estudiantes[i][4] >= 6:
                alumnas_promocionadas += 1
        #else:
        #    alumnas == 0
        #    return alumnas

    return alumnas_promocionadas / alumnas

#datos = ingreso_datos()
promediar = promediar_edad(lista)
nota_promo = nota_promocion(lista)
nota_aprobacion = nota_aprobar(lista)
nota_desaprobador = nota_desaprobados(lista)
promedio_masculino = promedio_nota_masculino(lista)
alumnas_promocionadas = porcentaje_alumnas_promocionadas(lista)


print(f"el promedio de edad es {promediar}")
print(f"la cantidad de gente promocionada es {nota_promo}")
print(f"la cantidad de gente aprobada es {nota_aprobacion}")
print(f"la cantidad de gente desaprobada es {nota_desaprobador}")
print(f"el promedio masculino es {promedio_masculino}")
print(f"la cantidad de alumnas promocionadas es {alumnas_promocionadas}")

    
