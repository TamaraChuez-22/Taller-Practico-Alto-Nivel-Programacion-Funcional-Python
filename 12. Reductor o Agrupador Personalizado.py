#EJERCICIO 12:

def agrupar_por(lista, fn_clave):
    grupos = {}
    for elemento in lista:
        clave = fn_clave(elemento)
        grupos.setdefault(clave, []).append(elemento)
    return grupos

personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Luis", "edad": 17},
    {"nombre": "Eva", "edad": 30},
]
grupos = agrupar_por(personas, lambda p: "adulto" if p["edad"] >= 18 else "menor")
print(grupos)