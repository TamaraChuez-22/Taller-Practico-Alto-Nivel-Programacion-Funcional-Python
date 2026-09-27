#EJERCICIO 9: Limitador de Tasa Inteligente (Rate Limiter con Reset)

def crear_limitador_avanzado(max_intentos, fn_alerta):
    intentos = 0
    def ejecutar():
        nonlocal intentos
        intentos += 1
        if intentos > max_intentos:
            fn_alerta(intentos)
            return False
        return True
    def reset():
        nonlocal intentos
        intentos = 0
    ejecutar.reset = reset
    return ejecutar

limitador = crear_limitador_avanzado(2, lambda n: print(f"ALERTA: límite superado (intento {n})"))
print(limitador())
print(limitador())
print(limitador())
limitador.reset()
print(limitador())