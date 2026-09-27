#EJERCICIO 10: Interruptor Múltiple (Máquina de Estados Ligera)

def crear_conmutador(lista_estados):
    indice = 0
    def conmutar():
        nonlocal indice
        estado_actual = lista_estados[indice]
        indice = (indice + 1) % len(lista_estados)
        return estado_actual
    return conmutar

semaforo = crear_conmutador(["ROJO", "AMARILLO", "VERDE"])
for _ in range(4):
    print(semaforo())