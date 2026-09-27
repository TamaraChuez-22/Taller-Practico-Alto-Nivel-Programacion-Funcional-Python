#EJERCICIO 11: Pipeline de Mapeo y Filtrado Combinado

def procesar_coleccion(lista, fn_predicado, fn_transformacion):
    return list(map(fn_transformacion, filter(fn_predicado, lista)))

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = procesar_coleccion(numeros, lambda x: x % 2 == 0, lambda x: x ** 2)
print(resultado)