# Scripts GNU Octave - TIF Cálculo Fase III

## Descripción

Scripts de análisis matemático usando GNU Octave con el paquete simbólico (symbolic).

## Requisitos

- GNU Octave 7.0+
- Paquete `symbolic` (se carga automáticamente en los scripts)

## Instalación del Paquete Symbolic

Si el paquete no está instalado:

```octave
pkg install -forge symbolic
```

## Uso

### Dentro del contenedor Docker

```bash
# Acceder al contenedor
docker exec -it tif-octave bash

# Ejecutar un script
octave --no-gui /workspace/maximos_minimos.m
octave --no-gui /workspace/concavidad.m
```

### Desde la línea de comandos del host

```bash
# Ejecutar script directamente
docker exec -it tif-octave octave --no-gui /workspace/maximos_minimos.m

# O más corto si los scripts están en /shared
docker exec -it tif-octave octave --no-gui /workspace/concavidad.m
```

## Scripts Disponibles

### 1. maximos_minimos.m

Análisis de máximos y mínimos absolutos en intervalos cerrados.

**Contenido:**
- Ejemplo 1: f(x) = 3x² - 12x + 5 en [0, 3]
- Ejemplo 2: f(x) = 2x³ - 3x² - 12x + 1 en [-2, 3]
- Ejemplo 3: f(x) = x + 4/x en [0.5, 4]

**Salida:**
- Derivadas calculadas
- Puntos críticos
- Evaluación en puntos importantes
- Clasificación de extremos
- Gráficas (si interfaz gráfica disponible)

### 2. concavidad.m

Análisis de concavidad y puntos de inflexión.

**Contenido:**
- Ejemplo 1: f(x) = x³ - 3x²
- Ejemplo 2: f(x) = 3x⁴ - 4x³ - 12x² + 5
- Ejemplo 3: f(x) = x³ - 3x² - 9x + 4 (análisis combinado)

**Salida:**
- Segunda derivada
- Candidatos a inflexión
- Tabla de concavidad
- Clasificación de extremos usando f''
- Gráficas con código de colores

## Características de los Scripts

- ✅ Cálculo simbólico exacto
- ✅ Salida formateada y profesional
- ✅ Explicaciones en español
- ✅ Gráficas opcionales (cuando GUI disponible)
- ✅ Manejo automático del paquete symbolic
- ✅ Código bien comentado

## Comparación con Python/SageMath

| Característica | Octave | Python (SymPy) | SageMath |
|----------------|--------|----------------|----------|
| Sintaxis | MATLAB-like | Programática | Matemática |
| Potencias | `x^2` | `x**2` | `x^2` |
| Paquete simbólico | `pkg load symbolic` | `import sympy` | Nativo |
| Derivadas | `diff(f, x)` | `sp.diff(f, x)` | `diff(f, x)` |
| Resolver | `solve(eq == 0, x)` | `sp.solve(eq, x)` | `solve(eq == 0, x)` |
| Gráficas | `plot()` nativo | matplotlib/plotly | `plot()` nativo |

## Notas Importantes

- Los scripts están diseñados para ejecutarse sin interfaz gráfica (`--no-gui`)
- Las gráficas se generarán solo si hay interfaz gráfica disponible
- Todos los resultados se muestran en la consola
- El paquete symbolic se carga al inicio y se descarga al final

## Ejemplos de Ejecución

```bash
# Análisis de máximos y mínimos
docker exec -it tif-octave octave --no-gui /workspace/maximos_minimos.m

# Análisis de concavidad
docker exec -it tif-octave octave --no-gui /workspace/concavidad.m
```

## Salida Esperada

Cada script imprime:
1. Encabezado con título y autor
2. Función analizada
3. Derivadas calculadas
4. Puntos críticos/inflexión
5. Tablas de análisis
6. Conclusiones
7. Confirmación de gráficas (si disponibles)

## Autor

**Aron**
Universidad Católica de Santa María
TIF Cálculo Fase III - 2025
