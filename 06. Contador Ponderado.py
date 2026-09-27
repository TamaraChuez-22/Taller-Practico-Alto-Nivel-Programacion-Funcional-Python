# EJERCICIO 6: Contador Ponderado

def crear_contador_paso(fn_paso):
    cuenta = 0
    def contar():
        nonlocal cuenta
        cuenta = fn_paso(cuenta)
        return cuenta
    return contar

contador_de_3 = crear_contador_paso(lambda c: c + 3)
print(contador_de_3())
print(contador_de_3())
print(contador_de_3())
