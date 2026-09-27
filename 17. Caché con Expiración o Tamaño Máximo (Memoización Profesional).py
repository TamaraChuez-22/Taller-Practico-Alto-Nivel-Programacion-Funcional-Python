#EJERCICIO 17: Caché con Expiración o Tamaño Máximo (Memoización Profesional)

import time


def memoizar_avanzado(fn_costosa, max_items):
    cache = {}
    orden_insercion = []

    def memoizada(*args):
        if args in cache:
            return cache[args]
        resultado = fn_costosa(*args)
        if len(orden_insercion) >= max_items:
            clave_mas_antigua = orden_insercion.pop(0)
            del cache[clave_mas_antigua]
        cache[args] = resultado
        orden_insercion.append(args)
        return resultado

    return memoizada


def cuadrado_lento(n):
    time.sleep(0.05)
    return n ** 2

cuadrado_memo = memoizar_avanzado(cuadrado_lento, max_items=2)
print(cuadrado_memo(4))  # calcula
print(cuadrado_memo(4))  # desde caché (instantáneo)
print(cuadrado_memo(5))  # calcula, caché: {4,5}
print(cuadrado_memo(6))  # calcula, descarta 4 -> caché: {5,6}
print(cuadrado_memo(4))  # recalcula porque 4 ya no está