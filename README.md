# 🧮 Plataforma Multi-Motor para Análisis de Derivadas

**Sistema Dockerizado de Análisis Matemático Computacional con Python, SageMath y GNU Octave**

[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Lab-F37626?logo=jupyter)](https://jupyter.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?logo=streamlit)](https://streamlit.io/)

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características Principales](#-características-principales)
- [Arquitectura del Sistema](#-arquitectura-del-sistema)
- [Tecnologías](#-tecnologías)
- [Instalación](#-instalación)
- [Uso](#-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Ejemplos](#-ejemplos)
- [Documentación](#-documentación)

---

## 🎯 Descripción

Plataforma computacional avanzada para el **análisis automático de derivadas** y **estudio de funciones matemáticas**. Implementa múltiples motores de cálculo simbólico (Python/SymPy, SageMath, GNU Octave) en contenedores Docker aislados, con interfaz web interactiva desarrollada en Streamlit.

El sistema permite analizar funciones matemáticas de forma automática, identificando:
- Puntos críticos (máximos y mínimos)
- Concavidad y puntos de inflexión
- Asíntotas y comportamiento en el infinito
- Trazo completo de curvas
- Visualización interactiva con Plotly

### Secciones Matemáticas Cubiertas

- **Sección 3.1**: Valores Máximos y Mínimos
- **Sección 3.3**: Concavidad y Puntos de Inflexión
- **Sección 3.5**: Trazo Completo de Curvas

---

## ✨ Características Principales

### 🎨 Dashboard Web Interactivo
- Interfaz Streamlit sin necesidad de programar
- Input de funciones con validación de sintaxis
- Cálculo automático de derivadas de primer y segundo orden
- Renderizado LaTeX de expresiones matemáticas
- Gráficas interactivas con zoom y exportación

### 🔬 Análisis Matemático Automatizado
- **Detección de puntos críticos**: Resuelve f'(x) = 0 automáticamente
- **Clasificación de extremos**: Usa criterio de segunda derivada
- **Análisis de concavidad**: Identifica regiones cóncavas arriba/abajo
- **Puntos de inflexión**: Detecta cambios de concavidad
- **Tabla de intervalos**: Genera análisis tabular completo

### 🖥️ Multi-Motor Computacional
- **Python (SymPy)**: Cálculo simbólico en Jupyter Lab
- **SageMath**: Sistema de álgebra computacional avanzado
- **GNU Octave**: Computación numérica compatible con MATLAB
- **Comparación de resultados**: Entre diferentes motores

### 📊 Visualización Avanzada
- Gráficas duales (función y derivadas)
- Código de colores por concavidad
- Marcado visual de puntos críticos
- Animaciones y exportación a PNG/SVG

### 🐳 Infraestructura Docker
- Orquestación con Docker Compose
- Servicios aislados y escalables
- Volúmenes compartidos para datos
- Red privada entre contenedores
- Fácil despliegue y reproducibilidad

---

## 🏗️ Arquitectura del Sistema

```
┌──────────────────────────────────────────────────────────┐
│                  Usuario / Navegador                      │
└──────────────────────────────────────────────────────────┘
                          │
          ┌───────────────┴───────────────┐
          │                               │
     Puerto 8501                    Puerto 8888/8889
          │                               │
┌─────────▼──────────┐         ┌──────────▼─────────┐
│  Streamlit App     │         │   Jupyter Lab      │
│  (Dashboard Web)   │◄────────┤   (Python/SymPy)   │
└────────────────────┘         └────────────────────┘
          │                               │
          │        Volumen Compartido     │
          │           (/shared)           │
          └───────────────┬───────────────┘
                          │
          ┌───────────────┴───────────────┐
          │                               │
   ┌──────▼─────────┐          ┌─────────▼──────────┐
   │   SageMath     │          │   GNU Octave       │
   │  (Puerto 8889) │          │   (CLI)            │
   └────────────────┘          └────────────────────┘
```

### Componentes

| Servicio | Puerto | Descripción | Función Principal |
|----------|--------|-------------|-------------------|
| **Streamlit** | 8501 | Dashboard Web | Interfaz interactiva para usuarios |
| **Jupyter Lab** | 8888 | Python + SymPy | Notebooks de análisis matemático |
| **SageMath** | 8889 | CAS Avanzado | Cálculo simbólico potente |
| **GNU Octave** | CLI | Computación Numérica | Scripts MATLAB-compatible |

---

## 🛠️ Tecnologías

### Backend / Motores Computacionales

#### Python Stack
- **SymPy** 1.12: Cálculo simbólico (derivadas, límites, integrales)
- **NumPy** 1.24: Computación numérica eficiente
- **SciPy** 1.11: Algoritmos científicos y optimización
- **Matplotlib** 3.7: Visualización estática
- **Plotly** 5.15: Gráficas interactivas 3D
- **Pandas** 2.0: Manipulación de datos

#### SageMath
- Sistema de Álgebra Computacional (CAS) open-source
- Integra 100+ librerías matemáticas
- Sintaxis Python-compatible
- Ideal para cálculo simbólico avanzado

#### GNU Octave
- Compatible con MATLAB
- Computación numérica de alto rendimiento
- Paquetes: control, signal, statistics

### Frontend

#### Streamlit 1.28
- Framework Python para apps web
- Actualización reactiva en tiempo real
- Widgets interactivos integrados
- Renderizado de LaTeX matemático

### Infraestructura

- **Docker** 20.10+: Contenedorización
- **Docker Compose** 2.x: Orquestación multi-servicio
- **Git**: Control de versiones

---

## 🚀 Instalación

### Prerrequisitos

```bash
# Versiones mínimas requeridas
docker --version          # Docker 20.10+
docker-compose --version  # Docker Compose 2.0+
git --version            # Git 2.30+
```

### Instalación Rápida

```bash
# 1. Clonar repositorio
git clone https://github.com/tu-usuario/tif-calculo-fase3.git
cd tif-calculo-fase3

# 2. Configurar variables de entorno (opcional)
cp .env.example .env
# Editar .env si deseas cambiar puertos o tokens

# 3. Construir e iniciar servicios
docker-compose up -d

# 4. Verificar estado
docker-compose ps
```

### Verificación de Instalación

```bash
# Todos los servicios deben estar "Up"
docker-compose ps

# Salida esperada:
# NAME              STATUS    PORTS
# tif-jupyter       Up        0.0.0.0:8888->8888/tcp
# tif-streamlit     Up        0.0.0.0:8501->8501/tcp
# tif-sagemath      Up        0.0.0.0:8889->8888/tcp
# tif-octave        Up        -
```

---

## 💻 Uso

### Acceso Rápido

#### 1. Dashboard Web (Recomendado)
```
URL: http://localhost:8501
```

**Funcionalidades:**
- ✅ Pestaña **Análisis**: Calculadora de máximos y mínimos
- ✅ Pestaña **Concavidad**: Análisis de curvatura
- ✅ Pestaña **Trazo Completo**: Análisis integral en 6 pasos
- ✅ Pestaña **Ejemplos**: Funciones predefinidas
- ✅ Pestaña **Ayuda**: Sintaxis y troubleshooting

**Ejemplo de uso:**
1. Ingresa función: `x**3 - 3*x**2 - 9*x + 5`
2. Define intervalo: `[-5, 5]`
3. Clic en "Analizar"
4. Obtén derivadas, puntos críticos y gráfica

#### 2. Jupyter Lab (Análisis Avanzado)
```
URL: http://localhost:8888
Token: calculo2025
```

**Notebooks disponibles:**
- `01_maximos_minimos.ipynb`: Ejemplos resueltos paso a paso
- `02_concavidad.ipynb`: Análisis de curvatura
- `03_trazo_curvas.ipynb`: Trazo completo de funciones

#### 3. SageMath Jupyter
```
URL: http://localhost:8889
Token: calculo2025
```

**Notebooks SageMath:**
- `00_comparativa_python_sage.ipynb`: Comparación de motores
- `01_maximos_minimos_sage.ipynb`: Ejemplos con Sage

#### 4. GNU Octave (CLI)
```bash
# Acceder al contenedor
docker exec -it tif-octave octave-cli

# Ejecutar script
docker exec -it tif-octave octave /workspace/scripts/maximos_minimos.m
```

### Flujo de Trabajo Típico

```bash
# 1. Iniciar servicios
docker-compose up -d

# 2. Análisis rápido → http://localhost:8501
#    Ingresar función y obtener resultados inmediatos

# 3. Análisis detallado → http://localhost:8888
#    Abrir notebooks para estudio paso a paso

# 4. Detener servicios
docker-compose down
```

---

## 📁 Estructura del Proyecto

```
tif-calculo-fase3/
│
├── docker-compose.yml           # Orquestación de servicios
├── .env                         # Variables de entorno (no en repo)
├── .env.example                 # Plantilla de configuración
├── .gitignore                   # Exclusiones de Git
├── README.md                    # Documentación principal
│
├── docs/                        # 📄 Documentación técnica
│   └── INFORME_FINAL.md         # Informe técnico del proyecto
│
├── scripts/                     # 🔧 Scripts de utilidad
│   ├── setup.sh                 # Instalación automatizada
│   ├── export_results.py        # Exportar a PDF/Word
│   └── cleanup.sh               # Limpieza de contenedores
│
├── services/                    # 🐳 Servicios Dockerizados
│   │
│   ├── jupyter/                 # Motor Python principal
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── notebooks/
│   │       ├── 01_maximos_minimos.ipynb
│   │       ├── 02_concavidad.ipynb
│   │       └── 03_trazo_curvas.ipynb
│   │
│   ├── streamlit/               # Dashboard web
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── app.py               # Aplicación principal
│   │
│   ├── sagemath/                # CAS avanzado
│   │   ├── start-notebook.sh
│   │   └── notebooks/
│   │       ├── 00_comparativa_python_sage.ipynb
│   │       └── 01_maximos_minimos_sage.ipynb
│   │
│   └── octave/                  # Computación numérica
│       ├── Dockerfile
│       └── scripts/
│           ├── maximos_minimos.m
│           ├── concavidad.m
│           └── README.md
│
└── shared/                      # 📊 Archivos compartidos entre servicios
    ├── animations/              # Animaciones generadas
    ├── data/                    # Datasets de funciones
    │   ├── funciones_ejemplos.json
    │   └── README.md
    ├── plots/                   # Gráficas exportadas
    └── results/                 # Resultados de análisis
```

---

## 📚 Ejemplos

### Ejemplo 1: Análisis con Streamlit

```bash
# 1. Abrir http://localhost:8501
# 2. Pestaña "Análisis"
# 3. Función: 2*x**3 - 3*x**2 - 12*x + 1
# 4. Intervalo: [-2, 3]
# 5. Click "Analizar"

# Resultado:
# - f'(x) = 6x² - 6x - 12
# - f''(x) = 12x - 6
# - Puntos críticos: x = -1 (máximo), x = 2 (mínimo)
# - Gráfica interactiva con puntos marcados
```

### Ejemplo 2: Notebook Jupyter

```python
# En http://localhost:8888
# Abrir: notebooks/01_maximos_minimos.ipynb

import sympy as sp
import numpy as np
import plotly.graph_objects as go

# Definir función
x = sp.Symbol('x')
f = x**3 - 3*x**2 - 9*x + 5

# Calcular derivadas
f_prime = sp.diff(f, x)
f_double_prime = sp.diff(f_prime, x)

# Encontrar puntos críticos
critical_points = sp.solve(f_prime, x)
print(f"Puntos críticos: {critical_points}")

# Clasificar usando segunda derivada
for point in critical_points:
    second = f_double_prime.subs(x, point)
    if second > 0:
        print(f"x = {point}: Mínimo local")
    elif second < 0:
        print(f"x = {point}: Máximo local")
```

### Ejemplo 3: SageMath

```python
# En http://localhost:8889
# SageMath notebook

var('x')
f = 2*x^3 - 3*x^2 - 12*x + 1

# Derivadas
f_prime = diff(f, x)
f_double_prime = diff(f_prime, x)

# Puntos críticos
critical = solve(f_prime == 0, x)
show(critical)

# Gráfica
plot(f, (x, -2, 3), color='blue', legend_label='f(x)')
```

### Ejemplo 4: GNU Octave

```bash
# Acceder al contenedor
docker exec -it tif-octave octave-cli
```

```octave
% En Octave CLI
pkg load symbolic
syms x
f = 2*x^3 - 3*x^2 - 12*x + 1;

% Derivada
f_prime = diff(f, x)

% Puntos críticos
critical = solve(f_prime == 0, x)
double(critical)
```

---

## 🔧 Comandos Útiles

### Gestión de Servicios

```bash
# Iniciar todos los servicios
docker-compose up -d

# Ver logs en tiempo real
docker-compose logs -f

# Ver logs de un servicio específico
docker-compose logs -f streamlit

# Reiniciar un servicio
docker-compose restart jupyter

# Detener todos los servicios
docker-compose down

# Reconstruir imágenes
docker-compose build --no-cache

# Ver estado de servicios
docker-compose ps
```

### Acceso a Contenedores

```bash
# Bash en Jupyter
docker exec -it tif-jupyter bash

# Octave CLI
docker exec -it tif-octave octave-cli

# SageMath
docker exec -it tif-sagemath sage

# Ver archivos compartidos
docker exec -it tif-jupyter ls -la /workspace/shared
```

### Debugging

```bash
# Ver logs completos de un servicio
docker-compose logs --tail=100 jupyter

# Verificar red
docker network inspect tif-calculo-fase3_calculo-network

# Verificar volúmenes
docker volume ls

# Probar conectividad
curl http://localhost:8501
curl http://localhost:8888
```

---

## 🔍 Troubleshooting

### Puerto ya en uso

```bash
# Ver qué proceso usa el puerto
sudo lsof -i :8888

# Cambiar puerto en .env
JUPYTER_PORT=8890
docker-compose down && docker-compose up -d
```

### Contenedor no inicia

```bash
# Ver logs detallados
docker-compose logs jupyter

# Reconstruir sin caché
docker-compose build --no-cache jupyter
docker-compose up -d
```

### Error de dependencias

```bash
# Reconstruir servicio
docker-compose build streamlit

# Verificar instalación
docker exec -it tif-streamlit pip list
```

### Token no funciona

```bash
# Ver token en logs
docker-compose logs jupyter | grep token

# Token por defecto: calculo2025
# URL: http://localhost:8888?token=calculo2025
```

---

## 📖 Documentación Adicional

### Sintaxis de Funciones

**Operaciones básicas:**
```python
x + 2          # Suma
x - 3          # Resta
2*x            # Multiplicación (usar *)
x/2            # División
x**2           # Potencia
sqrt(x)        # Raíz cuadrada
Abs(x)         # Valor absoluto
```

**Funciones especiales:**
```python
exp(x)         # Exponencial e^x
log(x)         # Logaritmo natural ln(x)
log(x, 10)     # Logaritmo base 10
sin(x)         # Seno
cos(x)         # Coseno
tan(x)         # Tangente
asin(x)        # Arcoseno
acos(x)        # Arcocoseno
atan(x)        # Arcotangente
```

**Constantes:**
```python
pi             # π ≈ 3.14159
E              # e ≈ 2.71828
```

### Referencias Técnicas

- [SymPy Documentation](https://docs.sympy.org)
- [SageMath Documentation](https://doc.sagemath.org)
- [GNU Octave Manual](https://docs.octave.org)
- [Streamlit Documentation](https://docs.streamlit.io)
- [Docker Compose Reference](https://docs.docker.com/compose)
- [Plotly Python](https://plotly.com/python)

---

## 🤝 Contribución

Las contribuciones son bienvenidas. Para contribuir:

1. Fork el repositorio
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`
3. Commit cambios: `git commit -m 'Agregar nueva funcionalidad'`
4. Push: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

**Guías de estilo:**
- Python: PEP 8
- Commits: Conventional Commits
- Documentación: Markdown

---

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo licencia MIT.

---

## 🙏 Agradecimientos

- Comunidad Open Source por las herramientas
- Desarrolladores de SymPy, SageMath, Octave y Streamlit
- Proyecto Jupyter por la infraestructura de notebooks

---

**Versión**: 1.0.0
**Última actualización**: Diciembre 2025
