#EJERCICIO 20. Mini-Query Engine sobre Listas de Objetos

def crear_consultor(campo):
    operadores = {
        "==": lambda a, b: a == b,
        "!=": lambda a, b: a != b,
        ">":  lambda a, b: a > b,
        "<":  lambda a, b: a < b,
        ">=": lambda a, b: a >= b,
        "<=": lambda a, b: a <= b,
    }
    def consultar(lista, operador, valor):
        fn_operador = operadores[operador]
        return list(filter(lambda item: fn_operador(item.get(campo), valor), lista))
    return consultar


productos = [
    {"nombre": "A", "precio": 10},
    {"nombre": "B", "precio": 25},
    {"nombre": "C", "precio": 5},
]
consultar_precio = crear_consultor("precio")
print(consultar_precio(productos, ">", 8))
print(consultar_precio(productos, "<=", 10))