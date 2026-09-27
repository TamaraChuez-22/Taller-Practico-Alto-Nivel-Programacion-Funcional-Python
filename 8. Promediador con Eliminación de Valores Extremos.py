#EJERCICIO 8: Promediador con Eliminación de Valores Extremos

def crear_promediador_filtrado(filtro_ruido_lambda):
    datos = []
    def agregar(valor):
        datos.append(valor)
        datos_filtrados = [d for d in datos if not filtro_ruido_lambda(d)]
        if not datos_filtrados:
            return 0
        return round(sum(datos_filtrados) / len(datos_filtrados), 2)
    return agregar

promediador = crear_promediador_filtrado(lambda v: v > 100)  # valores > 100 son ruido
print(promediador(10))
print(promediador(20))
print(promediador(500))
print(promediador(30))