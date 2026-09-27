#EJERCICIO 5: Conversor de Divisas con Margen: 

def crear_conversor(tasa, margen_lambda):
    def convertir(monto):
        convertido = monto * tasa
        margen = margen_lambda(convertido)
        return round(convertido + margen, 2)
    return convertir

usd_a_eur = crear_conversor(0.92, lambda c: c * 0.02)
print(usd_a_eur(100))
print(usd_a_eur(500))