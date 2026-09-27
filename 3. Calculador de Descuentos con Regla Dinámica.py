# EJERCICIO 3: Calculador de Descuentos con Regla Dinámica

def crear_descuento_dinamico(regla_condicional_lambda):
    DESCUENTO_FIJO = 0.20  # 20%, prefijado dentro del closure
    def calcular(precio):
        if regla_condicional_lambda(precio):
            return round(precio * (1 - DESCUENTO_FIJO), 2)
        return precio
    return calcular


descuento_mayoristas = crear_descuento_dinamico(lambda precio: precio > 100)
print(descuento_mayoristas(150))
print(descuento_mayoristas(50))