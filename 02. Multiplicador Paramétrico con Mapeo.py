#EJERCICIO 2: Multiplicador Paramétrico con Mapeo

def crear_operador(factor, operacion_lambda):
    def operar(valor):
        return operacion_lambda(valor, factor)
    return operar

duplicar = crear_operador(2, lambda v, f: v * f)
potencia = crear_operador(3, lambda v, f: v ** f)
print(duplicar(5))
print(potencia(2))
