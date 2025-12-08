# 📊 Directorio de Datos - TIF Cálculo Fase III

**Autor:** Aron
**Universidad:** UCSM
**Curso:** Cálculo 2025 - Fase III

---

## 📋 Descripción

Este directorio contiene datasets y archivos de datos utilizados por los diferentes servicios del proyecto TIF Cálculo Fase III. Los datos están organizados en formato JSON para facilitar su lectura y procesamiento por múltiples motores computacionales (Python/SymPy, SageMath, GNU Octave).

## 📁 Contenido del Directorio

### Archivos Actuales

```
shared/data/
├── README.md                    # Este archivo
└── funciones_ejemplos.json      # Dataset de funciones de ejemplo
```

### Archivos Planificados (Futuro)

- `problemas_optimizacion.json`: Problemas de optimización del mundo real
- `datos_experimentales.csv`: Datos para ajuste de curvas
- `parametros_analisis.json`: Configuraciones de análisis
- `resultados_exportados/`: Directorio para resultados de análisis

---

## 📄 Archivos Disponibles

### 1. `funciones_ejemplos.json`

**Descripción:** Dataset con 18 funciones matemáticas organizadas por tipo, diseñadas para el estudio de aplicaciones de la derivada.

**Propósito:**
- Proveer ejemplos listos para usar en notebooks y aplicaciones
- Facilitar pruebas automatizadas
- Servir como banco de ejercicios
- Demostrar diferentes casos de análisis de derivadas

**Categorías incluidas:**
- Polinomiales (6 funciones)
- Racionales (3 funciones)
- Trigonométricas (3 funciones)
- Exponenciales (3 funciones)
- Radicales (2 funciones)
- Logarítmicas (1 función)

**Niveles de dificultad:**
- Básica: 5 funciones
- Intermedia: 12 funciones
- Avanzada: 1 función

---

## 🔧 Formato de los Archivos JSON

### Estructura General

Los archivos JSON siguen una estructura consistente para facilitar su procesamiento:

```json
{
  "metadata": {
    "proyecto": "...",
    "autor": "...",
    "version": "...",
    "descripcion": "..."
  },
  "datos": [...],
  "categorias": {...},
  "uso": {...}
}
```

### Esquema de Funciones

Cada función en `funciones_ejemplos.json` contiene los siguientes campos:

```json
{
  "id": 1,
  "nombre": "f1",
  "expresion": "x**3 - 3*x",
  "expresion_latex": "x^3 - 3x",
  "tipo": "polinomial",
  "grado": 3,
  "dominio": [-5, 5],
  "descripcion": "Descripción de la función y su relevancia",
  "caracteristicas": {
    "puntos_criticos": [-1, 1],
    "tiene_maximos": true,
    "tiene_minimos": true,
    "tiene_inflexion": true,
    "continua": true,
    "derivable": true
  },
  "aplicaciones": ["Uso 1", "Uso 2"],
  "dificultad": "basica"
}
```

#### Campos Obligatorios

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `id` | Integer | Identificador único de la función |
| `nombre` | String | Nombre corto (ej: "f1", "g2") |
| `expresion` | String | Expresión en sintaxis Python/SymPy |
| `expresion_latex` | String | Expresión en LaTeX para renderizado |
| `tipo` | String | Categoría: polinomial, racional, trigonometrica, exponencial, radical, logaritmica |
| `dominio` | Array | Intervalo sugerido [a, b] para visualización |
| `descripcion` | String | Descripción textual de la función |

#### Campos Opcionales

| Campo | Tipo | Descripción |
|-------|------|-------------|
| `grado` | Integer/null | Grado del polinomio (null para no polinomiales) |
| `caracteristicas` | Object | Propiedades matemáticas de la función |
| `aplicaciones` | Array | Lista de aplicaciones prácticas |
| `dificultad` | String | Nivel: basica, intermedia, avanzada |
| `seccion_libro` | String | Referencia al texto guía (ej: "3.1") |

#### Objeto `caracteristicas`

```json
{
  "puntos_criticos": [x1, x2, ...],      // Lista de puntos críticos o "múltiples"
  "tiene_maximos": true/false,           // Tiene máximos locales
  "tiene_minimos": true/false,           // Tiene mínimos locales
  "tiene_inflexion": true/false,         // Tiene puntos de inflexión
  "continua": true/false,                // Es continua en su dominio
  "derivable": true/false,               // Es derivable en su dominio
  "periodica": true/false,               // [Opcional] Es periódica
  "periodo": 6.28...,                    // [Opcional] Periodo si es periódica
  "asintotas": ["x=0", "y=0"],          // [Opcional] Lista de asíntotas
  "discontinuidades": ["x=2"],          // [Opcional] Puntos de discontinuidad
  "puntos_no_derivables": [0]           // [Opcional] Puntos donde no es derivable
}
```

---

## 💻 Cómo Usar los Datasets

### Python / Jupyter Lab

```python
import json
import sympy as sp

# Cargar el dataset
with open('/shared/data/funciones_ejemplos.json', 'r') as f:
    data = json.load(f)

# Acceder a una función específica
funcion = data['funciones'][0]  # Primera función
print(f"Nombre: {funcion['nombre']}")
print(f"Expresión: {funcion['expresion']}")

# Crear función simbólica con SymPy
x = sp.Symbol('x')
f = sp.sympify(funcion['expresion'])

# Calcular derivada
f_prime = sp.diff(f, x)
print(f"Derivada: {f_prime}")

# Encontrar puntos críticos
critical_points = sp.solve(f_prime, x)
print(f"Puntos críticos: {critical_points}")
```

### Filtrar por Categoría

```python
# Obtener todas las funciones polinomiales
polinomiales_ids = data['categorias']['polinomial']['ids']
funciones_polinomiales = [f for f in data['funciones'] if f['id'] in polinomiales_ids]

# Obtener funciones de dificultad básica
basicas_ids = data['niveles_dificultad']['basica']['ids']
funciones_basicas = [f for f in data['funciones'] if f['id'] in basicas_ids]
```

### Iterar sobre Todas las Funciones

```python
# Analizar todas las funciones
for func in data['funciones']:
    print(f"\n{'='*60}")
    print(f"Analizando: {func['nombre']} - {func['descripcion']}")

    x = sp.Symbol('x')
    f = sp.sympify(func['expresion'])
    f_prime = sp.diff(f, x)

    print(f"f(x) = {f}")
    print(f"f'(x) = {f_prime}")

    # Graficar
    a, b = func['dominio']
    import numpy as np
    import matplotlib.pyplot as plt

    x_vals = np.linspace(a, b, 500)
    f_lambda = sp.lambdify(x, f, 'numpy')
    y_vals = f_lambda(x_vals)

    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals)
    plt.title(f"{func['nombre']}: ${func['expresion_latex']}$")
    plt.grid(True)
    plt.show()
```

### SageMath

```python
import json

# Cargar dataset
with open('/shared/data/funciones_ejemplos.json', 'r') as f:
    data = json.load(f)

# Convertir expresión a SageMath
func = data['funciones'][0]
var('x')

# Adaptar sintaxis (** a ^)
expresion_sage = func['expresion'].replace('**', '^')
f = sage_eval(expresion_sage, locals={'x': x})

# Calcular derivada
f_prime = diff(f, x)
print(f"f(x) = {f}")
print(f"f'(x) = {f_prime}")

# Graficar
a, b = func['dominio']
plot(f, (x, a, b), title=func['descripcion'])
```

### GNU Octave

```matlab
% Leer JSON (requiere JSONlab o similar)
% Alternativa: Usar Python para generar script .m

% Ejemplo manual de una función del dataset
syms x
f = x^3 - 3*x;  % funciones[0].expresion adaptado

% Derivada
f_prime = diff(f, x)

% Puntos críticos
critical = solve(f_prime == 0, x)

% Graficar
x_vals = linspace(-5, 5, 500);
y_vals = double(subs(f, x, x_vals));
plot(x_vals, y_vals);
title('f(x) = x^3 - 3x');
grid on;
```

### Streamlit Dashboard

```python
import streamlit as st
import json
import sympy as sp

# Cargar dataset
@st.cache_data
def load_functions():
    with open('/shared/data/funciones_ejemplos.json', 'r') as f:
        return json.load(f)

data = load_functions()

# Selector de función
nombres = [f['nombre'] for f in data['funciones']]
seleccion = st.selectbox("Selecciona una función:", nombres)

# Obtener función seleccionada
func = next(f for f in data['funciones'] if f['nombre'] == seleccion)

# Mostrar información
st.latex(func['expresion_latex'])
st.write(f"**Tipo:** {func['tipo']}")
st.write(f"**Dificultad:** {func['dificultad']}")
st.write(f"**Descripción:** {func['descripcion']}")

# Analizar
x = sp.Symbol('x')
f = sp.sympify(func['expresion'])
st.write("Analizando función...")
```

---

## 📊 Casos de Uso

### 1. Notebooks Educativos

Usar funciones del dataset para crear ejemplos consistentes:

```python
# notebook: 01_maximos_minimos.ipynb
data = load_json('/shared/data/funciones_ejemplos.json')

# Ejemplos de la sección 3.1
ejemplos_3_1 = [f for f in data['funciones'] if f.get('seccion_libro') == '3.1']

for func in ejemplos_3_1:
    analizar_maximos_minimos(func)
```

### 2. Tests Automatizados

Validar implementaciones con casos conocidos:

```python
def test_puntos_criticos():
    for func in data['funciones']:
        if func['caracteristicas']['puntos_criticos']:
            criticos_esperados = func['caracteristicas']['puntos_criticos']
            criticos_calculados = calcular_criticos(func['expresion'])
            assert set(criticos_esperados) == set(criticos_calculados)
```

### 3. Comparación de Motores

Verificar que Python, SageMath y Octave dan los mismos resultados:

```python
def comparar_motores(funcion_id):
    func = obtener_funcion(funcion_id)

    resultado_python = analizar_con_sympy(func['expresion'])
    resultado_sage = analizar_con_sage(func['expresion'])
    resultado_octave = analizar_con_octave(func['expresion'])

    return comparar_resultados(resultado_python, resultado_sage, resultado_octave)
```

### 4. Generación de Ejercicios

Crear hojas de ejercicios aleatorias:

```python
import random

def generar_ejercicios(nivel='basica', cantidad=5):
    ids_nivel = data['niveles_dificultad'][nivel]['ids']
    funciones_nivel = [f for f in data['funciones'] if f['id'] in ids_nivel]

    ejercicios = random.sample(funciones_nivel, cantidad)

    for i, func in enumerate(ejercicios, 1):
        print(f"\nEjercicio {i}:")
        print(f"Analice la función f(x) = {func['expresion_latex']}")
        print(f"en el intervalo {func['dominio']}")
```

---

## 🔄 Actualización de Datos

### Agregar Nueva Función

Para agregar una nueva función al dataset:

1. Abrir `funciones_ejemplos.json`
2. Agregar nuevo objeto al array `funciones`:

```json
{
  "id": 19,
  "nombre": "f19",
  "expresion": "nueva_expresion",
  "expresion_latex": "...",
  "tipo": "...",
  "dominio": [...],
  "descripcion": "...",
  "caracteristicas": {...},
  "dificultad": "..."
}
```

3. Actualizar array de IDs en la categoría correspondiente
4. Actualizar array de IDs en el nivel de dificultad correspondiente
5. Incrementar versión en metadata

### Validar JSON

Asegurarse de que el JSON sea válido:

```bash
# Verificar sintaxis JSON
python3 -m json.tool shared/data/funciones_ejemplos.json > /dev/null
echo $?  # Debe retornar 0 si es válido
```

---

## 📖 Referencia de Sintaxis

### Conversión entre Motores

| Operación | Python/SymPy | SageMath | Octave |
|-----------|--------------|----------|--------|
| Potencia | `x**2` | `x^2` | `x^2` |
| Exponencial | `exp(x)` | `e^x` o `exp(x)` | `exp(x)` |
| Logaritmo natural | `ln(x)` | `ln(x)` | `log(x)` |
| Logaritmo base 10 | `log(x, 10)` | `log(x, 10)` | `log10(x)` |
| Raíz cuadrada | `sqrt(x)` | `sqrt(x)` | `sqrt(x)` |
| Raíz n-ésima | `x**(1/n)` | `x^(1/n)` | `x^(1/n)` |
| Valor absoluto | `abs(x)` | `abs(x)` | `abs(x)` |
| Seno | `sin(x)` | `sin(x)` | `sin(x)` |
| Coseno | `cos(x)` | `cos(x)` | `cos(x)` |
| Tangente | `tan(x)` | `tan(x)` | `tan(x)` |
| Pi | `pi` | `pi` | `pi` |
| Euler | `E` | `e` | `exp(1)` |

### Funciones Especiales

```python
# Python/SymPy
from sympy import *
factorial(n)      # n!
binomial(n, k)    # Coeficiente binomial
Abs(x)           # Valor absoluto
Max(a, b)        # Máximo
Min(a, b)        # Mínimo
Piecewise(...)   # Función por partes
```

---

## 🎯 Mejores Prácticas

### Al Usar los Datasets

1. **Siempre cargar con manejo de errores:**
   ```python
   try:
       with open('/shared/data/funciones_ejemplos.json', 'r') as f:
           data = json.load(f)
   except FileNotFoundError:
       print("Error: Dataset no encontrado")
   except json.JSONDecodeError:
       print("Error: JSON inválido")
   ```

2. **Validar campos antes de usar:**
   ```python
   if 'puntos_criticos' in func['caracteristicas']:
       criticos = func['caracteristicas']['puntos_criticos']
   ```

3. **Cachear datos en aplicaciones:**
   ```python
   @st.cache_data  # Streamlit
   def load_functions():
       with open('/shared/data/funciones_ejemplos.json', 'r') as f:
           return json.load(f)
   ```

4. **Adaptar sintaxis según el motor:**
   ```python
   def to_sage_syntax(expr):
       return expr.replace('**', '^').replace('exp', 'e^')

   def to_octave_syntax(expr):
       return expr.replace('**', '^').replace('ln', 'log')
   ```

### Al Crear Nuevos Datasets

1. Seguir el esquema establecido
2. Incluir metadata completa
3. Documentar campos especiales
4. Validar JSON antes de commit
5. Actualizar este README con nueva información

---

## 📞 Soporte y Contacto

Para preguntas o sugerencias sobre los datasets:

- Revisar documentación del proyecto: `/README.md`
- Consultar notebooks de ejemplo: `/services/jupyter/notebooks/`
- Abrir issue en el repositorio del proyecto

---

## 📝 Changelog

### Versión 1.0 (2025-12-07)
- Creación del directorio `shared/data/`
- Primer dataset: `funciones_ejemplos.json` con 18 funciones
- Documentación inicial en `README.md`

### Versión Futura
- [ ] Agregar `problemas_optimizacion.json`
- [ ] Agregar `datos_experimentales.csv`
- [ ] Agregar funciones trigonométricas inversas
- [ ] Agregar funciones hiperbólicas
- [ ] Agregar funciones por partes (piecewise)

---

**Última actualización:** 2025-12-07
**Versión:** 1.0
**Mantenedor:** Aron - UCSM Cálculo 2025
