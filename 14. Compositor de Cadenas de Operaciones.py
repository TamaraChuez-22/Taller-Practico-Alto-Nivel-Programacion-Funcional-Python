#EJERCICIO 14: Compositor de Cadenas de Operaciones

def componer_dos(f, g):
    def compuesta(x):
        return f(g(x))
    return compuesta

duplicar = lambda x: x * 2
incrementar = lambda x: x + 1
combinada = componer_dos(duplicar, incrementar)   # duplicar(incrementar(x))
otra_combinada = componer_dos(incrementar, duplicar)  # incrementar(duplicar(x))
print(combinada(5))
print(otra_combinada(5))