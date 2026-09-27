#EJERCICIO 15: Decorador / HOF de Profiling y Auditoría

import time

def auditar_ejecucion(fn_objetivo, fn_logger):
    inicio = time.perf_counter()
    resultado = fn_objetivo()
    fin = time.perf_counter()
    duracion = fin - inicio
    informe = {"resultado": resultado, "duracion_segundos": duracion}
    fn_logger(informe)
    return resultado

def tarea_pesada():
    return sum(range(1_000_000))

resultado = auditar_ejecucion(
    tarea_pesada,
    lambda info: print(f"[LOG] resultado={info['resultado']} tiempo={info['duracion_segundos']:.6f}s")
)
print("Resultado final:", resultado)