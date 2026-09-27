#EJERCICIO 16: Validador Compuesto de Reglas de Negocio

def crear_validador_múltiple(*lambdas_criterios):
    def validar(objeto):
        return all(criterio(objeto) for criterio in lambdas_criterios)
    return validar

validador = crear_validador_múltiple(
    lambda x: x > 0,
    lambda x: x % 2 == 0,
    lambda x: x < 100
)
print(validador(50))
print(validador(-4))
print(validador(150))