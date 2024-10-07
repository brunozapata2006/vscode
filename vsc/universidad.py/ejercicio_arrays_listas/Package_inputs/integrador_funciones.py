# from Package_Inputs.inputs import * 
import Package_Arrays.inputs as PI
import Package_Arrays.Especificas as PAE
import Package_Arrays.array_Generales as PAG

'''
Realizar un menú de opciones en donde el usuario pueda realizar las siguientes
operaciones:
a. Pedir el ingreso de 10 números enteros entre -1000 y 1000.
b. Mostrar la cantidad de números positivos y negativos.
c. Mostrar la sumatoria de los números pares.
d. Informar el mayor de los números impares.
e. Listar todos los números ingresados.
f. Listar todos los números pares.
g. Listar los números de las posiciones impares.
h. Salir
Notas:
● Solo se podrá ingresar a las opciones b a g, siempre y cuando el usuario haya
ingresado los datos solicitados.
● Todas las opciones deberán ser programadas en funciones: habrá funciones
específicas (por ejemplo para determinar si un número es positivo o negativo)
y funciones de nivel general (por ejemplo una función que liste los números
pares). Tener en cuenta las características de la programación funcional.
● Las funciones específicas deberán estar en el módulo “Especificas.py”,
mientras que las generales en el módulo “Array_Generales.py”. Todos estos
módulos deben estar integrados en el paquete Package_Arrays.
● Utilizar las funciones input del paquete Package_Input.
Consejo: Primero realizar el desarrollo de las funciones y probarlas. Luego, armar
los módulos y paquetes.'''

lista = [0] * 10

while(True):

    respuesta = input('''Ingrese una opción.
a. Pedir el ingreso de 10 números enteros entre -1000 y 1000.
b. Mostrar la cantidad de números positivos y negativos.
c. Mostrar la sumatoria de los números pares.
d. Informar el mayor de los números impares.
e. Listar todos los números ingresados.
f. Listar todos los números pares.
g. Listar los números de las posiciones impares.
h. Salir
''')
    
    match respuesta:
        case 'a':
            for i in range(len(lista)):
                numero_ingresado = PI.pedir_entero("Ingrese un numero entre -1000 y 1000 ", "ERROR: Ingrese un numero entre -1000 y 1000 ", -1000, 1000)
                lista[i] = numero_ingresado

            lista_pares = PAG.determinar_pares(lista, True)
            lista_impares = PAG.determinar_pares(lista, False)
        case 'b':
            contador_positivos = PAE.verificar_tamanio(lista, 0, True)
            contador_negativos = PAE.verificar_tamanio(lista, 0, False)
            print(contador_positivos)
            print(contador_negativos)
        case 'c':
            sumatoria_pares = PAG.sumar_lista(lista_pares)
            print(sumatoria_pares)
        case 'd':
            maximo_impar = PAG.buscar_valor_maximo(lista_impares)
            print(maximo_impar)
        case 'e':
            PAG.mostrar_lista(lista, " ║ ")
        case 'f':
            PAG.mostrar_lista(lista_pares, " ║ ")
        case 'g':
            PAG.mostrar_lista(lista, " ║ ", inicio = 1, salto = 2)
        case 'h':
            break