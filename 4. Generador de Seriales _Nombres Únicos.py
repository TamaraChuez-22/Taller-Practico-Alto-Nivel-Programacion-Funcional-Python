#EJERCICIO 4: Generador de Seriales / Nombres Únicos: 
def crear_generador_sufijos(patron_lambda):
    contador = 0
    def generar(nombre_archivo):
        nonlocal contador
        contador += 1
        sufijo = patron_lambda(contador)
        if "." in nombre_archivo:
            nombre, ext = nombre_archivo.rsplit(".", 1)
            return f"{nombre}{sufijo}.{ext}"
        return f"{nombre_archivo}{sufijo}"
    return generar

generador = crear_generador_sufijos(lambda n: f"_v{n}")
print(generador("informe.pdf"))
print(generador("informe.pdf"))
print(generador("datos"))