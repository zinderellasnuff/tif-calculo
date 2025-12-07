# 📋 LISTA DE PENDIENTES - TIF CÁLCULO FASE III

**Última actualización**: 2025-12-07
**Estado del proyecto**: 40% completo

---

## 🎯 PRIORIDAD CRÍTICA (Para completar el TIF)

### 1. COMPLETAR NOTEBOOKS JUPYTER

#### 1.1 Finalizar `01_maximos_minimos.ipynb`
**Estado**: 75% completo
**Ubicación**: `/services/jupyter/notebooks/01_maximos_minimos.ipynb`

- [ ] **Ejemplo 3b**: Completar análisis de f(x) = 2x³ - 3x² - 12x + 1 en [-2,3]
  - El código base ya está (celda 10)
  - Falta:
    - Calcular derivada primera
    - Encontrar puntos críticos
    - Evaluar en extremos e interior del intervalo
    - Determinar máximo y mínimo absoluto
    - Crear visualización con Plotly
  - Tiempo estimado: 20-30 minutos

- [ ] Agregar 2-3 ejercicios adicionales de la sección 3.1
  - Funciones polinomiales
  - Funciones con raíces
  - Funciones trigonométricas simples

#### 1.2 Crear `02_concavidad.ipynb` (Sección 3.3)
**Estado**: 0% completo
**Ubicación**: `/services/jupyter/notebooks/02_concavidad.ipynb` (NO EXISTE)

**Contenido requerido**:

- [ ] **Parte 1: Teoría**
  - Definición de concavidad
  - Criterio de concavidad (f'' > 0 → cóncava hacia arriba)
  - Definición de punto de inflexión
  - Criterio del punto de inflexión

- [ ] **Parte 2: Ejemplos básicos**
  - Ejemplo 1: f(x) = x³ - 3x²
    - Calcular f''(x)
    - Determinar intervalos de concavidad
    - Encontrar puntos de inflexión
    - Visualizar con código de colores

  - Ejemplo 2: f(x) = x⁴ - 6x² + 4
    - Análisis completo de concavidad
    - Múltiples puntos de inflexión

  - Ejemplo 3: Función del PDF del curso

- [ ] **Parte 3: Visualización**
  - Gráfica mostrando concavidad con colores
  - Marcar puntos de inflexión
  - Mostrar tangentes en diferentes puntos

- [ ] **Parte 4: Análisis combinado**
  - Combinar extremos locales con concavidad
  - Tabla completa de análisis
  - Gráfica integrada

**Tiempo estimado**: 3-4 horas

#### 1.3 Crear `03_trazo_curvas.ipynb` (Sección 3.5)
**Estado**: 0% completo
**Ubicación**: `/services/jupyter/notebooks/03_trazo_curvas.ipynb` (NO EXISTE)

**Contenido requerido**:

- [ ] **Parte 1: Estrategia de graficación**
  - Paso 1: Dominio
  - Paso 2: Simetrías (par, impar)
  - Paso 3: Asíntotas (verticales, horizontales, oblicuas)
  - Paso 4: Primera derivada (monotonía, extremos)
  - Paso 5: Segunda derivada (concavidad, inflexión)
  - Paso 6: Gráfica final

- [ ] **Parte 2: Ejemplos completos**
  - Ejemplo 1: f(x) = 2 + 3x - x³
    - Análisis paso a paso de los 6 pasos
    - Tabla resumen
    - Gráfica final con todas las características

  - Ejemplo 2: f(x) = (x² - 4) / x
    - Incluye asíntotas verticales
    - Asíntota oblicua

  - Ejemplo 3: f(x) = x / (x² + 1)
    - Función racional
    - Comportamiento en infinito

  - Ejemplo 4-5: Funciones del PDF

- [ ] **Parte 3: Visualización avanzada**
  - Gráfica paso a paso (animación opcional)
  - Vista final integrada
  - Tabla de características

**Tiempo estimado**: 5-6 horas

---

### 2. IMPLEMENTAR SAGEMATH

**Estado**: 0% completo
**Directorio**: `/services/sagemath/notebooks/` (NO EXISTE)

#### 2.1 Crear estructura de directorios
```bash
mkdir -p /services/sagemath/notebooks
```

#### 2.2 Crear notebooks en SageMath

- [ ] **`01_maximos_minimos_sage.ipynb`**
  - Mismos ejemplos que notebook Python
  - Sintaxis Sage para derivadas: `diff(f, x)`
  - Sintaxis Sage para resolver: `solve(f_prime == 0, x)`
  - Comparar velocidad y precisión con Python
  - Tiempo estimado: 2 horas

- [ ] **`02_concavidad_sage.ipynb`**
  - Ejemplos de concavidad en Sage
  - Uso de `plot()` nativo de Sage
  - Tiempo estimado: 2 horas

- [ ] **`03_trazo_curvas_sage.ipynb`**
  - Trazo completo usando Sage
  - Funciones avanzadas de análisis
  - Tiempo estimado: 2 horas

- [ ] **`00_comparativa.ipynb`**
  - Notebook comparando Python vs Sage
  - Misma función analizada con ambos
  - Tabla de ventajas/desventajas
  - Tiempo estimado: 1.5 horas

**Tiempo estimado total**: 7-8 horas

---

### 3. IMPLEMENTAR GNU OCTAVE

**Estado**: 0% completo
**Directorio**: `/services/octave/scripts/` (NO EXISTE)

#### 3.1 Crear estructura
```bash
mkdir -p /services/octave/scripts
```

#### 3.2 Crear scripts .m

- [ ] **`maximos_minimos.m`**
  - Instalar paquete symbolic: `pkg install -forge symbolic`
  - Usar `syms x` para variables simbólicas
  - Calcular derivadas con `diff(f, x)`
  - Resolver ecuaciones con `solve()`
  - Graficar con `plot()`
  - Tiempo estimado: 2 horas

- [ ] **`concavidad.m`**
  - Análisis de segunda derivada
  - Detección de puntos de inflexión
  - Tiempo estimado: 1.5 horas

- [ ] **`trazo_curvas.m`**
  - Script completo de graficación
  - Todas las características
  - Tiempo estimado: 2 horas

- [ ] **`comparativa.m`**
  - Script que compara resultados numéricos
  - Validación de precisión
  - Tiempo estimado: 1 hora

**Tiempo estimado total**: 6-7 horas

---

### 4. DOCUMENTACIÓN ACADÉMICA

**Estado**: 0-10% completo
**Directorio**: `/docs/` (VACÍO)

#### 4.1 Informe Final (Trabajo Escrito)

**Archivo**: `/docs/informe_final.pdf`
**Formato**: PDF (desde LaTeX o Word)
**Extensión**: 15-25 páginas

**Estructura requerida**:

- [ ] **Portada**
  - Universidad, Escuela, Curso
  - Título del TIF
  - Autor, Código, Fecha

- [ ] **Índice**

- [ ] **Resumen** (1 página)
  - Objetivo del trabajo
  - Métodos utilizados
  - Resultados principales

- [ ] **1. Introducción** (2-3 páginas)
  - Contexto del cálculo diferencial
  - Importancia de las aplicaciones de la derivada
  - Objetivos del TIF
  - Justificación del uso de software

- [ ] **2. Marco Teórico** (4-5 páginas)
  - 2.1 Derivada y sus propiedades
  - 2.2 Valores máximos y mínimos
    - Teorema del valor extremo
    - Números críticos
    - Criterio de la primera derivada
    - Criterio de la segunda derivada
  - 2.3 Concavidad
    - Definición
    - Criterio de concavidad
    - Puntos de inflexión
  - 2.4 Trazo de curvas
    - Estrategia completa

- [ ] **3. Metodología** (2-3 páginas)
  - 3.1 Herramientas de software
    - Python (SymPy)
    - SageMath
    - GNU Octave
    - Streamlit
  - 3.2 Arquitectura del sistema
    - Docker y contenedores
    - Diagrama de componentes
  - 3.3 Proceso de análisis

- [ ] **4. Resultados** (5-7 páginas)
  - 4.1 Máximos y mínimos
    - Ejemplos resueltos
    - Gráficas
    - Comparación entre motores
  - 4.2 Concavidad
    - Ejemplos con visualización
  - 4.3 Trazo de curvas
    - 3 ejemplos completos paso a paso
  - 4.4 Análisis comparativo
    - Tabla Python vs Sage vs Octave
    - Ventajas/desventajas

- [ ] **5. Discusión** (2 páginas)
  - Interpretación de resultados
  - Ventajas del enfoque computacional
  - Limitaciones encontradas

- [ ] **6. Conclusiones** (1-2 páginas)
  - Conclusiones principales
  - Recomendaciones
  - Trabajo futuro

- [ ] **7. Referencias**
  - Libros de cálculo
  - Documentación de software
  - Artículos relacionados

- [ ] **Anexos**
  - Código fuente relevante
  - Capturas de pantalla
  - Gráficas adicionales

**Tiempo estimado**: 10-15 horas

#### 4.2 Manual de Usuario

**Archivo**: `/docs/manual_usuario.md`
**Formato**: Markdown

- [ ] Instalación detallada (paso a paso con screenshots)
- [ ] Guía de uso de cada servicio
- [ ] Troubleshooting expandido
- [ ] FAQ
- [ ] Ejemplos prácticos

**Tiempo estimado**: 3-4 horas

#### 4.3 Referencias Bibliográficas

**Archivo**: `/docs/referencias.bib`
**Formato**: BibTeX

- [ ] Libros de cálculo (Stewart, Larson, etc.)
- [ ] Documentación oficial de software
- [ ] Artículos académicos sobre CAS
- [ ] Papers sobre educación matemática con software

**Tiempo estimado**: 1-2 horas

---

### 5. ACTUALIZAR STREAMLIT DASHBOARD

**Estado**: 80% completo
**Archivo**: `/services/streamlit/app.py`

**Mejoras necesarias**:

- [ ] **Pestaña nueva: "Concavidad"**
  - Input de función
  - Cálculo de f''(x)
  - Detección de puntos de inflexión
  - Gráfica con código de colores (cóncava arriba/abajo)
  - Tiempo estimado: 2 horas

- [ ] **Pestaña nueva: "Trazo Completo"**
  - Análisis completo en 6 pasos
  - Mostrar tabla resumen
  - Gráfica final con todas las características
  - Tiempo estimado: 3 horas

- [ ] **Mejora: Comparación de motores**
  - Botón para ejecutar en Python/Sage/Octave
  - Mostrar resultados lado a lado
  - Tiempo de ejecución
  - Tiempo estimado: 4-5 horas (requiere API)

- [ ] **Mejora: Exportación**
  - Botón para exportar a PDF
  - Botón para exportar a Word
  - Guardar gráficas en `/shared/plots/`
  - Tiempo estimado: 2 horas

**Tiempo estimado total**: 11-12 horas

---

## 🔧 PRIORIDAD ALTA (Mejoras importantes)

### 6. SCRIPTS DE UTILIDAD

**Directorio**: `/scripts/` (VACÍO)

- [ ] **`setup.sh`**
  - Verificar dependencias (Docker, docker-compose, git)
  - Crear directorios necesarios
  - Copiar .env.example a .env
  - Construir contenedores
  - Levantar servicios
  - Mostrar URLs de acceso
  - Tiempo estimado: 1 hora

- [ ] **`cleanup.sh`**
  - Detener contenedores
  - Limpiar volúmenes
  - Limpiar caché de Docker
  - Opcional: limpiar todo o solo caché
  - Tiempo estimado: 30 minutos

- [ ] **`export_results.py`**
  - Exportar todos los notebooks a PDF usando nbconvert
  - Generar reporte Word con python-docx
  - Copiar gráficas a `/shared/results/`
  - Crear ZIP con todo
  - Tiempo estimado: 2 horas

- [ ] **`test_all.py`**
  - Tests unitarios para funciones matemáticas
  - Validar que f'(x) sea correcto
  - Comparar resultados entre motores
  - Pytest framework
  - Tiempo estimado: 3 horas

- [ ] **`compare_engines.py`**
  - Benchmark de Python vs Sage vs Octave
  - Medir tiempo de ejecución
  - Medir precisión numérica
  - Generar reporte comparativo
  - Tiempo estimado: 2 horas

**Tiempo estimado total**: 8-9 horas

---

### 7. CONTENIDO EN DIRECTORIOS SHARED

**Directorio**: `/shared/` (TODO VACÍO)

#### 7.1 `/shared/data/`
- [ ] Crear datasets de funciones de prueba
  - `funciones_polinomiales.json`
  - `funciones_racionales.json`
  - `funciones_trigonometricas.json`
  - Formato: {"nombre": "f1", "expresion": "x**3 - 3*x", "dominio": [-5, 5]}
  - Tiempo estimado: 1 hora

#### 7.2 `/shared/plots/`
- [ ] Será llenado automáticamente al ejecutar notebooks
- [ ] Crear script que organice plots por sección
  - `/shared/plots/maximos_minimos/`
  - `/shared/plots/concavidad/`
  - `/shared/plots/trazo_curvas/`

#### 7.3 `/shared/results/`
- [ ] Exportaciones de notebooks en PDF
- [ ] Reportes generados en Word
- [ ] Archivos CSV con resultados numéricos

#### 7.4 `/shared/animations/` (OPCIONAL)
- [ ] Animación de función con sliders
- [ ] Animación mostrando construcción de gráfica paso a paso
- [ ] Formato: GIF o MP4
- [ ] Tiempo estimado: 4-6 horas

---

## 📊 PRIORIDAD MEDIA (Mejoras opcionales)

### 8. INTEGRACIÓN ENTRE SERVICIOS

- [ ] **Crear API REST**
  - Endpoint para ejecutar código Python
  - Endpoint para ejecutar código Sage
  - Endpoint para ejecutar código Octave
  - Flask o FastAPI
  - Tiempo estimado: 6-8 horas

- [ ] **Conectar Streamlit con API**
  - Botones para cambiar de motor
  - Mostrar comparación en tiempo real
  - Tiempo estimado: 3-4 horas

---

### 9. TESTING Y VALIDACIÓN

- [ ] **Tests unitarios**
  - `tests/test_derivatives.py`
  - `tests/test_critical_points.py`
  - `tests/test_concavity.py`
  - Usar pytest
  - Tiempo estimado: 4-5 horas

- [ ] **Tests de integración**
  - Verificar que servicios se comuniquen
  - Validar que volúmenes compartidos funcionen
  - Docker compose test
  - Tiempo estimado: 2-3 horas

- [ ] **Validación matemática**
  - Comparar resultados simbólicos vs numéricos
  - Verificar derivadas con diferenciación numérica
  - Tiempo estimado: 2 horas

---

### 10. CI/CD

- [ ] **GitHub Actions**
  - `.github/workflows/test.yml`
  - Ejecutar tests en cada push
  - Build de contenedores
  - Tiempo estimado: 2-3 horas

- [ ] **Docker Hub**
  - Publicar imágenes en Docker Hub
  - Automatizar builds
  - Tiempo estimado: 1-2 horas

---

## 📝 PRIORIDAD BAJA (Nice to have)

### 11. MEJORAS DE VISUALIZACIÓN

- [ ] Animaciones interactivas con Plotly
- [ ] Gráficas 3D de superficies
- [ ] Sliders para modificar parámetros en vivo
- [ ] Dark mode en Streamlit
- [ ] Tiempo estimado: 8-10 horas

### 12. FUNCIONALIDADES AVANZADAS

- [ ] Exportación a LaTeX
- [ ] Generación automática de ejercicios
- [ ] Sistema de caché para resultados
- [ ] Base de datos de funciones
- [ ] Tiempo estimado: 15-20 horas

---

## 📊 RESUMEN DE TIEMPOS ESTIMADOS

### CRÍTICO (Para completar TIF básico)
| Tarea | Tiempo |
|-------|--------|
| Completar notebooks Jupyter | 8-10 horas |
| Implementar SageMath | 7-8 horas |
| Implementar Octave | 6-7 horas |
| Informe final (PDF) | 10-15 horas |
| Manual de usuario | 3-4 horas |
| Referencias | 1-2 horas |
| Actualizar Streamlit | 11-12 horas |
| **TOTAL CRÍTICO** | **46-58 horas** |

### ALTA (Recomendado)
| Tarea | Tiempo |
|-------|--------|
| Scripts de utilidad | 8-9 horas |
| Contenido shared | 1-2 horas |
| **TOTAL ALTA** | **9-11 horas** |

### MEDIA (Opcional)
| Tarea | Tiempo |
|-------|--------|
| API REST | 9-12 horas |
| Testing | 8-10 horas |
| CI/CD | 3-5 horas |
| **TOTAL MEDIA** | **20-27 horas** |

### **GRAN TOTAL**
- **Mínimo viable (solo crítico)**: 46-58 horas (~1-1.5 semanas de trabajo)
- **Proyecto completo (crítico + alta)**: 55-69 horas (~1.5-2 semanas)
- **Proyecto excelente (crítico + alta + media)**: 75-96 horas (~2-2.5 semanas)

---

## 🎯 PLAN RECOMENDADO DE IMPLEMENTACIÓN

### Semana 1: Contenido Académico
1. **Día 1-2**: Completar notebooks Jupyter (secciones 3.1, 3.3, 3.5)
2. **Día 3**: Implementar notebooks SageMath
3. **Día 4**: Implementar scripts Octave
4. **Día 5**: Actualizar dashboard Streamlit

### Semana 2: Documentación y Pulido
1. **Día 1-3**: Escribir informe final
2. **Día 4**: Manual de usuario y referencias
3. **Día 5**: Scripts de utilidad, testing básico

### Semana 3 (Opcional): Mejoras
1. Integración de servicios
2. Testing completo
3. CI/CD

---

## ✅ CHECKLIST DE ENTREGA MÍNIMA

Para considerar el TIF completo, debes tener:

- [x] Infraestructura Docker funcionando
- [x] README.md completo
- [ ] **3 notebooks Jupyter completos (secciones 3.1, 3.3, 3.5)**
- [ ] **Notebooks SageMath con al menos 1 ejemplo por sección**
- [ ] **Scripts Octave con al menos 1 ejemplo por sección**
- [ ] **Streamlit con análisis de las 3 secciones**
- [ ] **Informe final en PDF (15-25 páginas)**
- [ ] **Manual de usuario**
- [ ] **Referencias bibliográficas**
- [ ] Al menos 1 ejemplo comparativo entre los 3 motores

---

## 📞 NOTAS FINALES

### Prioriza
1. Notebooks Jupyter (contenido académico principal)
2. Informe final (requisito académico)
3. Implementación básica en Sage y Octave (justifica el enfoque multi-motor)

### Puedes postergar
- Animaciones
- API REST
- CI/CD
- Funcionalidades avanzadas

### Recuerda
- Calidad sobre cantidad
- Documentar bien el código
- Validar resultados matemáticos
- Citar fuentes correctamente

**Lo que tienes ahora es una excelente base (40% completo). Con 50-60 horas más de trabajo enfocado, tendrás un TIF sobresaliente.**

