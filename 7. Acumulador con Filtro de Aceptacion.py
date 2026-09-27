#EJERCICIO 7: Acumulador con Filtro de Aceptación:
def crear_acumulador_validado(criterio_lambda):
    total = 0
    def acumular(valor):
        nonlocal total
        if criterio_lambda(valor):
            total += valor
        return total
    return acumular

acumulador_positivos = crear_acumulador_validado(lambda v: v > 0)
print(acumulador_positivos(10))
print(acumulador_positivos(-5))
print(acumulador_positivos(20))