#EJERCICIO 13:	Ejecutor Repetitivo con Estado Accesible 

def ejecutar_y_rastrear(fn_tarea, n):
    historial = []
    for _ in range(n):
        historial.append(fn_tarea())
    def obtener_historial():
        return historial
    return obtener_historial

import random
random.seed(42)
rastreador = ejecutar_y_rastrear(lambda: random.randint(1, 6), 5)
print(rastreador())