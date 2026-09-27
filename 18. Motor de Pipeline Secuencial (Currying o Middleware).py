#EJERCICIO 18: Motor de Pipeline Secuencial (Currying / Middleware)

def crear_pipeline(*funciones_transformacion):
    def pipeline(dato_inicial):
        resultado = dato_inicial
        for funcion in funciones_transformacion:
            resultado = funcion(resultado)
        return resultado
    return pipeline


procesar_pipeline = crear_pipeline(
    lambda x: x + 1,
    lambda x: x * 2,
    lambda x: x - 3
)
print(procesar_pipeline(5))