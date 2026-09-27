# 🧪 Taller Práctico de Alto Nivel: Programación Funcional en Python

## Diseño de Arquitecturas Funcionales: HOFs, Closures Avanzados y Composición con Lambdas

---

## 🎓 Información Académica

**Universidad:** Universidad Estatal Península de Santa Elena (UPSE)
**Carrera:** Software
**Paralelo:** 5/2
**Asignatura:** Programación Funcional
**Actividad:** Ejercicios de práctica de Closures
**Estudiante:** Tamara Chuez Sánchez
**Docente:** Anthony Abrahan Pachay Espinoza

---

## 📌 Descripción

Este repositorio contiene el desarrollo del **Taller Práctico de Alto Nivel de Programación Funcional en Python**, orientado al estudio y aplicación de técnicas de programación funcional mediante ejercicios progresivos.

El taller aborda principalmente:

* Funciones de Orden Superior (HOFs).
* Closures.
* Funciones `lambda`.
* `map()`.
* `filter()`.
* `reduce()`.
* Composición de funciones.
* Uso de `nonlocal`.
* Manejo de estado mediante closures.
* Decoradores.
* Memoización y caché.
* Validación mediante funciones.
* Pipelines funcionales.
* Sistemas basados en eventos.
* Procesamiento y consulta de colecciones.

Los ejercicios avanzan desde conceptos fundamentales hasta implementaciones más elaboradas que permiten observar cómo las técnicas funcionales pueden utilizarse para construir soluciones modulares y reutilizables.

---

## 🎯 Objetivo

Aplicar los principios de la **programación funcional en Python** mediante la implementación de funciones de orden superior, closures, expresiones lambda y técnicas de composición funcional, desarrollando soluciones reutilizables y con manejo de estado encapsulado.

---

## 🧠 Conceptos Principales

### 🔹 Funciones de Orden Superior (HOF)

Son funciones capaces de:

* Recibir otras funciones como argumentos.
* Retornar funciones como resultado.

Ejemplo:

```python
def aplicar_operacion(funcion, valor):
    return funcion(valor)
```

---

### 🔹 Closures

Un closure permite que una función interna conserve acceso a las variables definidas en el ámbito de la función externa incluso después de que esta haya terminado su ejecución.

Ejemplo:

```python
def crear_multiplicador(factor):

    def multiplicar(numero):
        return numero * factor

    return multiplicar
```

Uso:

```python
duplicar = crear_multiplicador(2)

print(duplicar(10))
```

Resultado:

```text
20
```

---

### 🔹 `lambda`

Las funciones lambda permiten crear funciones pequeñas y anónimas de manera concisa.

```python
cuadrado = lambda x: x ** 2

print(cuadrado(5))
```

Resultado:

```text
25
```

---

### 🔹 `map()`

Permite aplicar una función a cada elemento de una colección.

```python
numeros = [1, 2, 3, 4]

resultado = list(map(lambda x: x * 2, numeros))
```

Resultado:

```text
[2, 4, 6, 8]
```

---

### 🔹 `filter()`

Permite seleccionar elementos que cumplen una determinada condición.

```python
numeros = [1, 2, 3, 4, 5, 6]

pares = list(filter(lambda x: x % 2 == 0, numeros))
```

Resultado:

```text
[2, 4, 6]
```

---

### 🔹 `reduce()`

Permite reducir una colección a un único resultado acumulado.

```python
from functools import reduce

numeros = [1, 2, 3, 4]

resultado = reduce(lambda a, b: a + b, numeros)
```

Resultado:

```text
10
```

---

### 🔹 `nonlocal`

La palabra reservada `nonlocal` permite modificar una variable perteneciente al ámbito de la función externa desde una función interna.

```python
def contador():

    cantidad = 0

    def incrementar():
        nonlocal cantidad
        cantidad += 1
        return cantidad

    return incrementar
```

---

## 📚 Ejercicios del Taller

El repositorio contiene **20 ejercicios prácticos**:

| #  | Ejercicio                                       | Conceptos principales                  |
| -- | ----------------------------------------------- | -------------------------------------- |
| 1  | Crear Formateador                               | Closures, HOFs, transformación         |
| 2  | Multiplicador Paramétrico con Mapeo             | Closures, `map()`                      |
| 3  | Calculador de Descuentos con Regla Dinámica     | Closures, `lambda`                     |
| 4  | Generador de Seriales / Nombres Únicos          | Closures, estado encapsulado           |
| 5  | Conversor de Divisas con Margen                 | Closures, parámetros dinámicos         |
| 6  | Contador Ponderado                              | Closures, `nonlocal`                   |
| 7  | Acumulador con Filtro de Aceptación             | Closures, validación, estado           |
| 8  | Promediador con Eliminación de Valores Extremos | Closures, filtrado, procesamiento      |
| 9  | Limitador de Tasa Inteligente                   | Closures, estado, reset                |
| 10 | Interruptor Múltiple                            | Máquina de estados, closures           |
| 11 | Pipeline de Mapeo y Filtrado Combinado          | `map()`, `filter()`, composición       |
| 12 | Reductor o Agrupador Personalizado              | Reducción, agrupación                  |
| 13 | Ejecutor Repetitivo con Estado Accesible        | Closures, historial                    |
| 14 | Compositor de Cadenas de Operaciones            | Composición funcional                  |
| 15 | Decorador / HOF de Profiling y Auditoría        | Decoradores, HOFs, medición            |
| 16 | Validador Compuesto de Reglas de Negocio        | Validación, composición                |
| 17 | Caché con Expiración o Tamaño Máximo            | Memoización, closures, caché           |
| 18 | Motor de Pipeline Secuencial                    | Currying, middleware, composición      |
| 19 | Sistema Pub/Sub                                 | Eventos, listeners, HOFs, closures     |
| 20 | Mini-Query Engine sobre Listas de Objetos       | Filtrado, mapeo, consultas funcionales |

---

## 🗂️ Estructura del Repositorio

Los ejercicios se encuentran directamente en el directorio principal del repositorio:

```text
Taller-Practico-Alto-Nivel-Programacion-Funcional-Python/
│
├── 1.CREAR FORMATEADOR.py
├── 2. Multiplicador Paramétrico con Mapeo.py
├── 3. Calculador de Descuentos con Regla Dinámica.py
├── 4. Generador de Seriales _Nombres Únicos.py
├── 5. Conversor de Divisas con Margen.py
├── 6. Contador Ponderado.py
├── 7. Acumulador con Filtro de Aceptacion.py
├── 8. Promediador con Eliminación de Valores Extremos.py
├── 9. Limitador de Tasa Inteligente (Rate Limiter con Reset).py
├── 10. Interruptor Múltiple (Máquina de Estados Ligera).py
├── 11. Pipeline de Mapeo y Filtrado Combinado.py
├── 12. Reductor o Agrupador Personalizado.py
├── 13. Ejecutor Repetitivo con Estado Accesible.py
├── 14. Compositor de Cadenas de Operaciones.py
├── 15. Decorador o HOF de Profiling y Auditoría.py
├── 16. Validador Compuesto de Reglas de Negocio.py
├── 17. Caché con Expiración o Tamaño Máximo (Memoización Profesional).py
├── 18. Motor de Pipeline Secuencial (Currying o Middleware).py
├── 19. Sistema Pub o Sub (Event Listener con HOFs y Closures).py
├── 20. Mini-Query Engine sobre Listas de Objetos.py
│
└── README.md
```

---

## ⚙️ Requisitos

Para ejecutar los ejercicios se necesita:

* **Python 3.x**
* Un editor de código, por ejemplo:

  * Visual Studio Code
  * PyCharm
  * IDLE
* Terminal o consola para ejecutar los programas.

No se requieren librerías externas para los ejercicios principales del taller.

---

## ▶️ Ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/TamaraChuez-22/Taller-Practico-Alto-Nivel-Programacion-Funcional-Python.git
```

### 2. Ingresar al directorio

```bash
cd Taller-Practico-Alto-Nivel-Programacion-Funcional-Python
```

### 3. Ejecutar un ejercicio

Por ejemplo:

```bash
python "1.CREAR FORMATEADOR.py"
```

También es posible abrir cualquiera de los archivos `.py` directamente desde el editor de código y ejecutarlo.

---

## 🔍 Enfoque del Taller

Los ejercicios fueron planteados de forma progresiva para demostrar la evolución desde closures sencillos hasta arquitecturas funcionales más elaboradas.

### Nivel inicial

Se trabajan conceptos como:

* Creación de closures.
* Parámetros dinámicos.
* Funciones lambda.
* Estado encapsulado.

### Nivel intermedio

Se incorporan:

* `map()`.
* `filter()`.
* `reduce()`.
* Composición.
* Validación.
* Manejo de estado.
* Historial de operaciones.

### Nivel avanzado

Se desarrollan soluciones relacionadas con:

* Decoradores.
* Profiling.
* Memoización.
* Caché.
* Pipelines.
* Currying.
* Middleware.
* Sistemas Pub/Sub.
* Mini motores de consulta.

---

## 💡 Importancia de los Closures

Uno de los elementos centrales del taller es el uso de **closures**.

Los closures permiten encapsular información y conservar el estado de una función sin necesidad de utilizar variables globales.

Esto permite construir componentes reutilizables como:

```text
Función externa
      │
      ├── Define estado
      │
      └── Retorna función interna
                    │
                    └── Conserva el estado
```

Esta característica se utiliza en diferentes ejercicios para crear contadores, acumuladores, generadores, validadores, cachés y otros componentes funcionales.

---

## 🧩 Programación Funcional Aplicada

El taller demuestra que la programación funcional no se limita a utilizar `lambda`, sino que también permite construir soluciones completas mediante la combinación de diferentes técnicas:

```text
HOF
 │
 ├── Closure
 │     └── Estado encapsulado
 │
 ├── Lambda
 │
 ├── map()
 │
 ├── filter()
 │
 ├── reduce()
 │
 └── Composición
        │
        └── Pipeline funcional
```

La combinación de estas herramientas permite crear código modular, reutilizable y adaptable a diferentes necesidades.

---

## 🎓 Resultados de Aprendizaje

Al finalizar el taller se busca demostrar la capacidad para:

* Comprender el funcionamiento de las funciones de orden superior.
* Crear y utilizar closures.
* Trabajar con funciones lambda.
* Encapsular estado mediante `nonlocal`.
* Aplicar `map()`, `filter()` y `reduce()`.
* Construir funciones reutilizables.
* Componer múltiples funciones.
* Implementar validaciones funcionales.
* Crear pipelines de procesamiento.
* Utilizar decoradores y técnicas de profiling.
* Implementar mecanismos de caché y memoización.
* Modelar sistemas basados en eventos.
* Procesar y consultar colecciones mediante técnicas funcionales.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Paradigma:** Programación Funcional
* **Herramientas principales:**

  * Closures
  * Higher-Order Functions
  * Lambda
  * Map
  * Filter
  * Reduce
  * Decoradores
  * Composición funcional
  * Currying
  * Memoización
  * Pipelines
  * Event Listeners

---

## 👩‍💻 Autora

**Tamara Chuez Sánchez**

Estudiante de la carrera de **Software**
Universidad Estatal Península de Santa Elena — UPSE
Paralelo **5/2**

---

## 👨‍🏫 Docente

**Anthony Abrahan Pachay Espinoza**

Asignatura: **Programación Funcional**

---

## 📖 Propósito Académico

Este repositorio ha sido desarrollado con fines **académicos**, como evidencia práctica del aprendizaje y aplicación de conceptos relacionados con la programación funcional en Python.

Cada ejercicio busca demostrar de manera práctica el uso de diferentes técnicas funcionales, avanzando progresivamente desde implementaciones sencillas hasta soluciones con mayor nivel de abstracción.

---

## 🔗 Repositorio

El código fuente del taller se encuentra disponible en GitHub:

**Taller Práctico de Alto Nivel — Programación Funcional en Python**

https://github.com/TamaraChuez-22/Taller-Practico-Alto-Nivel-Programacion-Funcional-Python

---

⭐ **Taller desarrollado como parte de la asignatura de Programación Funcional — UPSE.**
