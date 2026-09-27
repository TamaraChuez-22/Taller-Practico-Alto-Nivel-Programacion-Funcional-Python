#EJERCICIO 19: Sistema Pub/Sub (Event Listener con HOFs y Closures): 
def crear_sistema_eventos():
    suscriptores = {}

    def suscribir(evento, callback):
        suscriptores.setdefault(evento, []).append(callback)

    def emitir(evento, *args, **kwargs):
        for callback in suscriptores.get(evento, []):
            callback(*args, **kwargs)

    def gestor(accion, *args, **kwargs):
        if accion == "suscribir":
            return suscribir(*args, **kwargs)
        elif accion == "emitir":
            return emitir(*args, **kwargs)

    gestor.suscribir = suscribir
    gestor.emitir = emitir
    return gestor


eventos = crear_sistema_eventos()
eventos.suscribir("login", lambda usuario: print(f"Bienvenido, {usuario}"))
eventos.suscribir("login", lambda usuario: print(f"[LOG] Login registrado: {usuario}"))
eventos.emitir("login", "Tami")