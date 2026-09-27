#EJERCICIO 1: Generador de Formateadores con Transformación

def crear_formateador(prefijo, fn_transformacion):
    def formatear(texto):
        transformado = fn_transformacion(texto)
        return f"{prefijo}{transformado}"
    return formatear


formateador_mayus = crear_formateador(">> ", lambda t: t.upper())
formateador_invertido = crear_formateador("[REV] ", lambda t: t[::-1])

print(formateador_mayus("hola mundo"))
print(formateador_invertido("python"))