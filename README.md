# 🧮 TIF Cálculo Fase III - Aplicaciones de la Derivada

**Plataforma Multi-Motor Dockerizada para Análisis Matemático Computacional**

[![Universidad](https://img.shields.io/badge/Universidad-UCSM-blue)](https://ucsm.edu.pe)
[![Curso](https://img.shields.io/badge/Curso-C%C3%A1lculo-green)](https://github.com)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)](https://www.python.org/)

---

## 📋 Tabla de Contenidos

- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Objetivos Académicos](#-objetivos-académicos)
- [Arquitectura del Sistema](#-arquitectura-del-sistema)
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Instalación y Configuración](#-instalación-y-configuración)
- [Uso de la Plataforma](#-uso-de-la-plataforma)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Funcionalidades Implementadas](#-funcionalidades-implementadas)
- [Estado del Proyecto](#-estado-del-proyecto)
- [Roadmap](#-roadmap)
- [Ejemplos de Uso](#-ejemplos-de-uso)
- [Contribución](#-contribución)
- [Licencia](#-licencia)

---

## 🎯 Descripción del Proyecto

Este proyecto es un **Trabajo de Investigación Formativa (TIF)** para el curso de Cálculo Fase III de la Universidad Católica de Santa María (UCSM), año 2025. Implementa una plataforma computacional avanzada para el análisis de **aplicaciones de la derivada** utilizando múltiples motores de cálculo de software libre.

### Tema Principal
**Aplicaciones de la Derivada** - Capítulo 3 del texto guía

Secciones cubiertas:
- **3.1** Valores Máximos y Mínimos
- **3.3** Concavidad y Puntos de Inflexión
- **3.5** Trazo de Curvas

### Autor
**Aron**
Universidad Católica de Santa María
Curso: Cálculo 2025 - Fase III

---

## 🎓 Objetivos Académicos

### Objetivos Generales
1. Implementar y comparar múltiples motores de cálculo simbólico para análisis de derivadas
2. Desarrollar herramientas interactivas para visualización de conceptos matemáticos
3. Automatizar el proceso de análisis de funciones usando criterios de derivación
4. Crear una plataforma educativa accesible mediante contenedores Docker

### Objetivos Específicos
- Calcular derivadas de primer y segundo orden de forma automática
- Identificar y clasificar puntos críticos (máximos, mínimos, inflexión)
- Analizar concavidad y monotonía de funciones
- Generar visualizaciones interactivas de funciones y sus derivadas
- Comparar resultados entre Python (SymPy), SageMath y GNU Octave

---

## 🏗️ Arquitectura del Sistema

El proyecto utiliza una arquitectura **multi-contenedor basada en Docker** con 4 servicios principales:

```
┌─────────────────────────────────────────────────────────┐
│                    Usuario / Navegador                   │
└─────────────────────────────────────────────────────────┘
                           │
           ┌───────────────┴───────────────┐
           │                               │
      Puerto 8501                    Puerto 8888/8889
           │                               │
┌──────────▼──────────┐         ┌─────────▼──────────┐
│   Streamlit App     │         │   Jupyter Lab      │
│  (Dashboard Web)    │◄────────┤   (Python/SymPy)   │
└─────────────────────┘         └────────────────────┘
           │                               │
           │         Volumen Compartido    │
           │         (/shared)             │
           └───────────────┬───────────────┘
                           │
           ┌───────────────┴───────────────┐
           │                               │
    ┌──────▼──────────┐         ┌─────────▼──────────┐
    │   SageMath      │         │   GNU Octave       │
    │   (Puerto 8889) │         │   (CLI)            │
    └─────────────────┘         └────────────────────┘
```

### Componentes

| Servicio | Puerto | Tecnología | Función |
|----------|--------|------------|---------|
| **Streamlit** | 8501 | Python 3.11 + Streamlit | Dashboard web interactivo |
| **Jupyter Lab** | 8888 | Python 3.x + SciPy Stack | Notebooks de análisis matemático |
| **SageMath** | 8889 | Sage + Jupyter | Sistema de álgebra computacional avanzado |
| **GNU Octave** | - | Octave 7.x | Computación numérica (CLI) |

---

## 🛠️ Tecnologías Utilizadas

### Backend / Motores Computacionales

#### Python (Jupyter Lab)
- **SymPy**: Cálculo simbólico (derivadas, límites, integrales)
- **NumPy**: Computación numérica eficiente
- **SciPy**: Algoritmos científicos y optimización
- **Matplotlib**: Visualización estática
- **Plotly**: Gráficas interactivas
- **Pandas**: Manipulación de datos tabulares

#### SageMath
- Sistema de Álgebra Computacional (CAS) open-source
- Integra 100+ librerías matemáticas
- Ideal para cálculo simbólico avanzado

#### GNU Octave
- Compatible con MATLAB
- Computación numérica de alto rendimiento
- Paquetes: control, signal, statistics

### Frontend

#### Streamlit
- Framework Python para aplicaciones web
- Actualización en tiempo real
- Widgets interactivos
- Renderizado de LaTeX y gráficas

### Infraestructura

- **Docker** y **Docker Compose**: Orquestación de contenedores
- **Git**: Control de versiones
- **Linux**: Plataforma de desarrollo

---

## 🚀 Instalación y Configuración

### Prerrequisitos

```bash
# Versiones mínimas requeridas
docker --version          # Docker 20.10+
docker-compose --version  # Docker Compose 1.29+
git --version            # Git 2.30+
```

### Instalación Paso a Paso

#### 1. Clonar el Repositorio

```bash
git clone https://github.com/tu-usuario/tif-calculo-fase3.git
cd tif-calculo-fase3
```

#### 2. Configurar Variables de Entorno

```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar si es necesario (opcional)
nano .env
```

Contenido de `.env`:
```bash
JUPYTER_TOKEN=calculo2025
JUPYTER_PORT=8888
STREAMLIT_PORT=8501
SAGE_PORT=8889
```

#### 3. Construir Contenedores

```bash
# Construir todas las imágenes
docker-compose build

# Construcción con caché limpio (si hay problemas)
docker-compose build --no-cache
```

#### 4. Levantar Servicios

```bash
# Iniciar todos los servicios
docker-compose up -d

# Ver logs en tiempo real
docker-compose logs -f

# Ver logs de un servicio específico
docker-compose logs -f streamlit
```

#### 5. Verificar Estado

```bash
# Ver contenedores en ejecución
docker-compose ps

# Resultado esperado:
# NAME              STATUS    PORTS
# tif-jupyter       Up        0.0.0.0:8888->8888/tcp
# tif-streamlit     Up        0.0.0.0:8501->8501/tcp
# tif-sagemath      Up        0.0.0.0:8889->8888/tcp
# tif-octave        Up        -
```

---

## 💻 Uso de la Plataforma

### Acceso a los Servicios

#### 1. Dashboard Streamlit (Recomendado para empezar)
```
URL: http://localhost:8501
```
- Interfaz web interactiva
- Sin necesidad de programar
- Análisis inmediato de funciones
- Visualización automática

**Funcionalidades:**
- Pestaña **Análisis**: Calculadora interactiva de derivadas
- Pestaña **Ejemplos**: Funciones predefinidas del curso
- Pestaña **Ayuda**: Sintaxis y guía de uso

#### 2. Jupyter Lab (Para análisis avanzado)
```
URL: http://localhost:8888
Token: calculo2025
```
- Notebooks interactivos
- Código Python ejecutable
- Exportación a PDF/HTML
- Documentación académica

**Notebooks disponibles:**
- `01_maximos_minimos.ipynb`: Sección 3.1 del curso

#### 3. SageMath Jupyter
```
URL: http://localhost:8889
Token: calculo2025
```
- CAS avanzado con sintaxis Python
- Notebooks .sage
- Cálculo simbólico potente

#### 4. GNU Octave (Línea de comandos)
```bash
# Acceder al contenedor
docker exec -it tif-octave octave

# Ejecutar script
docker exec -it tif-octave octave /workspace/mi_script.m
```

### Ejemplo de Flujo de Trabajo

```bash
# 1. Iniciar servicios
docker-compose up -d

# 2. Abrir navegador en http://localhost:8501
#    → Usar dashboard para análisis rápido

# 3. Para análisis detallado: http://localhost:8888
#    → Abrir notebook 01_maximos_minimos.ipynb

# 4. Al finalizar
docker-compose down
```

---

## 📁 Estructura del Proyecto

```
tif-calculo-fase3/
│
├── docker-compose.yml           # Orquestación de servicios
├── .env                         # Variables de entorno
├── .env.example                # Plantilla de configuración
├── .gitignore                  # Exclusiones de Git
├── README.md                   # Este archivo
│
├── docs/                       # 📄 Documentación del proyecto
│   ├── informe_final.pdf      # (PENDIENTE) Trabajo escrito
│   ├── manual_usuario.md      # (PENDIENTE) Guía detallada
│   └── referencias.bib        # (PENDIENTE) Bibliografía
│
├── scripts/                    # 🔧 Scripts de utilidad
│   ├── setup.sh               # (PENDIENTE) Instalación automatizada
│   ├── export_results.py      # (PENDIENTE) Exportar a PDF/Word
│   └── cleanup.sh             # (PENDIENTE) Limpieza de contenedores
│
├── services/                   # 🐳 Servicios Dockerizados
│   │
│   ├── jupyter/               # Motor Python principal
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   └── notebooks/
│   │       ├── 01_maximos_minimos.ipynb        # ✅ Implementado
│   │       ├── 02_concavidad.ipynb             # ❌ PENDIENTE
│   │       └── 03_trazo_curvas.ipynb           # ❌ PENDIENTE
│   │
│   ├── streamlit/            # Dashboard web
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   ├── app.py            # ✅ Aplicación principal
│   │   └── shared/           # (Vacío) Módulos compartidos
│   │
│   ├── sagemath/             # CAS avanzado
│   │   └── notebooks/        # ❌ PENDIENTE - Sin notebooks
│   │
│   └── octave/               # Computación numérica
│       ├── Dockerfile
│       └── scripts/          # ❌ PENDIENTE - Sin scripts .m
│
└── shared/                   # 📊 Archivos compartidos entre servicios
    ├── animations/           # (Vacío) Animaciones de funciones
    ├── data/                 # (Vacío) Datasets de prueba
    ├── plots/                # (Vacío) Gráficas exportadas
    └── results/              # (Vacío) Resultados de análisis
```

### Convenciones de Archivos

- **✅ Implementado**: Funcionalidad completa
- **🚧 En Progreso**: Parcialmente implementado
- **❌ PENDIENTE**: No implementado
- **(Vacío)**: Directorio sin contenido

---

## ✨ Funcionalidades Implementadas

### Dashboard Streamlit (app.py)

#### Análisis Automático de Funciones
- ✅ Input de función matemática con validación
- ✅ Cálculo de primera derivada f'(x)
- ✅ Cálculo de segunda derivada f''(x)
- ✅ Renderizado LaTeX de expresiones matemáticas
- ✅ Configuración de intervalo [a, b]

#### Detección de Puntos Críticos
- ✅ Solución de f'(x) = 0
- ✅ Filtrado de soluciones reales
- ✅ Evaluación de f(x) en puntos críticos
- ✅ Clasificación usando criterio de segunda derivada:
  - f''(x) > 0 → Mínimo local
  - f''(x) < 0 → Máximo local
  - f''(x) = 0 → Punto de inflexión

#### Visualización Interactiva
- ✅ Gráfica dual (f(x) y f'(x)) con Plotly
- ✅ Marcado visual de puntos críticos
- ✅ Zoom y pan interactivos
- ✅ Exportación de gráficas

#### Interfaz de Usuario
- ✅ Diseño responsivo de 3 pestañas
- ✅ Ejemplos predefinidos del PDF
- ✅ Sintaxis de ayuda
- ✅ Manejo de errores

### Jupyter Notebook (01_maximos_minimos.ipynb)

#### Ejemplos Implementados
- ✅ **Ejemplo 2a**: f(x) = 2x³ + x² + 2x
  - Números críticos
  - Análisis de dominio de derivada

- ✅ **Ejemplo 2b**: h(t) = t^(3/4) - 2t^(1/4)
  - Puntos donde derivada no existe
  - Raíces de derivada

- ✅ **Ejemplo 3a**: f(x) = 3x² - 12x + 5 en [0,3]
  - Valores máximos/mínimos absolutos
  - Evaluación en extremos e interior
  - Visualización completa

- 🚧 **Ejemplo 3b**: INCOMPLETO

#### Capacidades
- ✅ Cálculo simbólico con SymPy
- ✅ Gráficas interactivas con Plotly
- ✅ Código educativo documentado
- ✅ Análisis paso a paso

---

## 📊 Estado del Proyecto

### Resumen General

```
Progreso Total: ████████████░░░░░░░░  40%

Infraestructura:  ████████████████████  100%
Frontend:         ████████████████░░░░   80%
Notebooks:        ████████░░░░░░░░░░░░   35%
Documentación:    ████░░░░░░░░░░░░░░░░   20%
```

### Por Componente

| Componente | Estado | Completado | Faltante |
|------------|--------|------------|----------|
| **Docker/Infraestructura** | ✅ Completo | 100% | - |
| **Streamlit Dashboard** | ✅ Funcional | 80% | Conexión con otros motores |
| **Jupyter - Sección 3.1** | 🚧 Parcial | 75% | Ejemplo 3b |
| **Jupyter - Sección 3.3** | ❌ Pendiente | 0% | Todo |
| **Jupyter - Sección 3.5** | ❌ Pendiente | 0% | Todo |
| **SageMath** | ❌ Pendiente | 0% | Notebooks |
| **Octave** | ❌ Pendiente | 0% | Scripts |
| **Documentación** | ❌ Pendiente | 20% | Informe, manual |
| **Scripts Utilidad** | ❌ Pendiente | 0% | Todo |

### Funcionalidades Operativas

✅ **Funcionando:**
- Cálculo automático de derivadas (SymPy)
- Dashboard web interactivo
- Análisis de máximos/mínimos básico
- Visualización de funciones
- Contenedores Docker

❌ **Pendiente:**
- Análisis de concavidad
- Trazo completo de curvas
- Comparación entre motores
- Exportación a PDF/Word
- Animaciones
- Tests/validación
- Documentación académica

---

## 🗺️ Roadmap

### Fase 1: Completar Contenido Académico (PRIORITARIO)

#### Notebooks Jupyter

- [ ] **01_maximos_minimos.ipynb**
  - [x] Ejemplo 2a y 2b
  - [x] Ejemplo 3a
  - [ ] **Ejemplo 3b: f(x) = 2x³ - 3x² - 12x + 1 en [-2,3]**
  - [ ] Ejercicios adicionales del PDF

- [ ] **02_concavidad.ipynb** (Sección 3.3)
  - [ ] Definición y criterios
  - [ ] Criterio de concavidad (f'' > 0 cóncava hacia arriba)
  - [ ] Puntos de inflexión
  - [ ] Ejemplos del texto guía
  - [ ] Visualización de concavidad

- [ ] **03_trazo_curvas.ipynb** (Sección 3.5)
  - [ ] Estrategia completa de graficación
  - [ ] Dominio, simetrías, asíntotas
  - [ ] Monotonía y extremos
  - [ ] Concavidad y puntos de inflexión
  - [ ] Gráfica final integrada
  - [ ] 3-5 ejemplos completos

#### Implementación en Otros Motores

- [ ] **SageMath**
  - [ ] `sage/01_maximos_minimos.sage`
  - [ ] `sage/02_concavidad.sage`
  - [ ] `sage/03_trazo_curvas.sage`
  - [ ] Notebook comparativo con Python

- [ ] **GNU Octave**
  - [ ] `octave/maximos_minimos.m`
  - [ ] `octave/concavidad.m`
  - [ ] `octave/trazo_curvas.m`
  - [ ] Script de validación numérica

### Fase 2: Documentación Académica

- [ ] **Informe Final (PDF)**
  - [ ] Marco teórico (derivadas, criterios)
  - [ ] Metodología (software utilizado)
  - [ ] Resultados (ejemplos resueltos)
  - [ ] Análisis comparativo de motores
  - [ ] Conclusiones y recomendaciones
  - [ ] Bibliografía

- [ ] **Manual de Usuario**
  - [ ] Instalación detallada
  - [ ] Guía de uso de cada servicio
  - [ ] Ejemplos paso a paso
  - [ ] Troubleshooting

- [ ] **Documentación Técnica**
  - [ ] Arquitectura del sistema
  - [ ] API de módulos
  - [ ] Guía de contribución

### Fase 3: Mejoras Funcionales

- [ ] **Integración entre Servicios**
  - [ ] API REST para comunicación
  - [ ] Ejecutar código Sage desde Streamlit
  - [ ] Ejecutar código Octave desde Streamlit
  - [ ] Comparación de resultados en tiempo real

- [ ] **Exportación y Reportes**
  - [ ] Script de exportación a PDF (nbconvert)
  - [ ] Exportación a Word (.docx)
  - [ ] Generación automática de informe
  - [ ] Plantilla LaTeX profesional

- [ ] **Visualizaciones Avanzadas**
  - [ ] Animaciones de funciones
  - [ ] Visualización 3D de superficies
  - [ ] Sliders interactivos
  - [ ] Comparación lado a lado

### Fase 4: Scripts y Automatización

- [ ] `scripts/setup.sh`: Instalación automatizada
- [ ] `scripts/test_all.py`: Tests de validación
- [ ] `scripts/export_results.py`: Exportación masiva
- [ ] `scripts/cleanup.sh`: Limpieza de caché y logs
- [ ] `scripts/compare_engines.py`: Benchmark de motores

### Fase 5: Calidad y Testing

- [ ] Tests unitarios (pytest)
- [ ] Validación de resultados matemáticos
- [ ] Tests de integración entre servicios
- [ ] CI/CD con GitHub Actions

---

## 📚 Ejemplos de Uso

### Ejemplo 1: Análisis Rápido con Streamlit

```bash
# 1. Iniciar servicios
docker-compose up -d

# 2. Abrir http://localhost:8501

# 3. En la pestaña "Análisis":
#    - Función: 2*x**3 - 3*x**2 - 12*x + 1
#    - Intervalo: [-2, 3]
#    - Clic en "Analizar"

# 4. Ver resultados:
#    - Derivadas calculadas
#    - Puntos críticos identificados
#    - Gráfica interactiva
```

### Ejemplo 2: Análisis Detallado con Jupyter

```bash
# 1. Abrir http://localhost:8888 (token: calculo2025)

# 2. Navegar a: notebooks/01_maximos_minimos.ipynb

# 3. Ejecutar celdas paso a paso:
#    - Importar librerías
#    - Definir función
#    - Calcular derivadas
#    - Encontrar puntos críticos
#    - Visualizar

# 4. Modificar código según necesites
```

### Ejemplo 3: Usar SageMath

```bash
# Acceder al contenedor
docker exec -it tif-sagemath bash

# Iniciar Sage
sage

# Código Sage
sage: var('x')
sage: f = 2*x^3 - 3*x^2 - 12*x + 1
sage: diff(f, x)
# Output: 6*x^2 - 6*x - 12
```

### Ejemplo 4: Usar Octave

```bash
# Acceder al contenedor
docker exec -it tif-octave octave

# Código Octave
octave> syms x
octave> f = 2*x^3 - 3*x^2 - 12*x + 1
octave> diff(f, x)
```

---

## 🔧 Troubleshooting

### Problemas Comunes

#### Error: Puerto ya en uso
```bash
# Ver qué proceso usa el puerto
sudo lsof -i :8888

# Cambiar puerto en .env
JUPYTER_PORT=8890
```

#### Contenedor no inicia
```bash
# Ver logs detallados
docker-compose logs jupyter

# Reconstruir sin caché
docker-compose build --no-cache jupyter
```

#### Token de Jupyter no funciona
```bash
# Obtener token desde logs
docker-compose logs jupyter | grep token

# O usar el configurado en .env
# Token por defecto: calculo2025
```

#### Dependencias faltantes
```bash
# Reconstruir servicio específico
docker-compose build streamlit

# Verificar instalación
docker exec -it tif-streamlit pip list
```

---

## 🤝 Contribución

### Cómo Contribuir

1. **Fork** el repositorio
2. Crear rama feature: `git checkout -b feature/nueva-funcionalidad`
3. Commit cambios: `git commit -m 'Agregar nueva funcionalidad'`
4. Push a la rama: `git push origin feature/nueva-funcionalidad`
5. Crear **Pull Request**

### Guías de Estilo

- Código Python: PEP 8
- Commits: Conventional Commits
- Documentación: Markdown con GitHub Flavored Markdown

---

## 📖 Referencias

### Bibliografía del Curso
- Stewart, J. (2012). *Cálculo de una variable: Trascendentes tempranas* (7ª ed.). Cengage Learning.
- Larson, R., & Edwards, B. (2016). *Cálculo* (10ª ed.). Cengage Learning.

### Documentación Técnica
- [SymPy Documentation](https://docs.sympy.org)
- [SageMath Documentation](https://doc.sagemath.org)
- [GNU Octave Manual](https://docs.octave.org)
- [Streamlit Documentation](https://docs.streamlit.io)
- [Docker Compose Reference](https://docs.docker.com/compose)

---

## 📄 Licencia

Este proyecto es un trabajo académico para la Universidad Católica de Santa María (UCSM).

**Uso Educativo**: El código puede ser usado con fines educativos citando la fuente.

---

## 👨‍💻 Autor

**Aron**
Universidad Católica de Santa María
Curso: Cálculo 2025 - Fase III

---

## 📞 Contacto y Soporte

Para preguntas sobre el proyecto:
- Crear un [Issue](https://github.com/tu-usuario/tif-calculo-fase3/issues)
- Consultar la [documentación](./docs/)

---

## 🎉 Agradecimientos

- **UCSM** por la formación académica
- **Comunidad Open Source** por las herramientas
- **Desarrolladores** de SymPy, SageMath, Octave y Streamlit

---

**Última actualización**: Diciembre 2025
**Versión del proyecto**: 0.4.0 (40% completo)

