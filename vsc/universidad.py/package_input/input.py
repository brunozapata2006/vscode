# def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int)-> int|None:

#     while reintentos != 0:
#         valor = int(input(mensaje))
#         if minimo < valor < maximo:
#             return valor
#         else:  
#             print(mensaje_error)
#             reintentos -= 1
#             if reintentos == 0:
#                 print("error, numeros maximos alcanzados")
#             pass
    
    
# resultado = get_int("ingrese un valor: ","Error, ingrese un valor valido: ", 1, 105, 3)

# print(resultado)

# def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int)-> float|None:

#     while reintentos != 0:
#         valor = float(input(mensaje))
#         if minimo < valor < maximo:
#             return valor
#         else:  
#             print(mensaje_error)
#             reintentos -= 1
#             if reintentos == 0:
#                 print("error, numeros maximos alcanzados")
#             pass    
    
# resultado = get_float("ingrese un valor: ","Error, ingrese un valor valido: ", minimo=0.4, maximo=100.0, reintentos=3)

# print(resultado)


# def get_string(mensaje:str, mensaje_error:str, min_longitud:int, max_longitud:int, reintentos:int) -> str | None:
    
#     mensaje_contador = input(mensaje)
#     contador_longitud = len(mensaje_contador)

#     while contador_longitud > max_longitud or contador_longitud < min_longitud:
#         reintentos -= 1
#         error = input(mensaje_error)
#         if reintentos == 0:
#             error = "Su texto supero el limite"
#             return error
#     else:
#         mensaje_contador = mensaje_contador
#         contador_longitud = mensaje_contador
#         return contador_longitud
        
  
# texto = get_string("Ingrese su nombre y apellido: ", "Error, reingrese devuelta: ", 4, 15, 1)

# print(texto)
