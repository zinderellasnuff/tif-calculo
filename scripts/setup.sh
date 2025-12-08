#!/bin/bash

# =========================================================================
# TIF Cálculo Fase III - UCSM 2025
# Script de Instalación y Configuración Automatizada
# Autor: Aron
# =========================================================================

set -e  # Salir si hay error

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Funciones de utilidad
print_header() {
    echo -e "${BLUE}"
    echo "========================================================================="
    echo "  $1"
    echo "========================================================================="
    echo -e "${NC}"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

# =========================================================================
# Paso 1: Banner
# =========================================================================

clear
print_header "TIF CÁLCULO FASE III - INSTALACIÓN AUTOMATIZADA"
echo ""
echo "  Universidad: UCSM"
echo "  Autor: Aron"
echo "  Año: 2025"
echo ""
echo "  Este script configurará automáticamente:"
echo "  - Verificación de dependencias (Docker, docker-compose, Git)"
echo "  - Creación de directorios necesarios"
echo "  - Configuración de variables de entorno"
echo "  - Construcción de contenedores Docker"
echo "  - Inicio de servicios"
echo ""
read -p "¿Deseas continuar? (s/n): " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[SsYy]$ ]]; then
    print_warning "Instalación cancelada por el usuario"
    exit 0
fi

# =========================================================================
# Paso 2: Verificar Dependencias
# =========================================================================

print_header "PASO 1: VERIFICACIÓN DE DEPENDENCIAS"

# Verificar Docker
print_info "Verificando Docker..."
if command -v docker &> /dev/null; then
    DOCKER_VERSION=$(docker --version)
    print_success "Docker encontrado: $DOCKER_VERSION"
else
    print_error "Docker no está instalado"
    echo ""
    echo "Por favor instala Docker desde: https://docs.docker.com/get-docker/"
    exit 1
fi

# Verificar Docker Compose
print_info "Verificando Docker Compose..."
if command -v docker-compose &> /dev/null; then
    COMPOSE_VERSION=$(docker-compose --version)
    print_success "Docker Compose encontrado: $COMPOSE_VERSION"
elif docker compose version &> /dev/null; then
    COMPOSE_VERSION=$(docker compose version)
    print_success "Docker Compose (plugin) encontrado: $COMPOSE_VERSION"
    # Alias para usar docker-compose
    alias docker-compose='docker compose'
else
    print_error "Docker Compose no está instalado"
    echo ""
    echo "Por favor instala Docker Compose desde: https://docs.docker.com/compose/install/"
    exit 1
fi

# Verificar Git
print_info "Verificando Git..."
if command -v git &> /dev/null; then
    GIT_VERSION=$(git --version)
    print_success "Git encontrado: $GIT_VERSION"
else
    print_warning "Git no está instalado (opcional)"
fi

# Verificar permisos de Docker
print_info "Verificando permisos de Docker..."
if docker ps &> /dev/null; then
    print_success "Usuario tiene permisos para ejecutar Docker"
else
    print_warning "Es posible que necesites permisos de sudo para Docker"
    print_info "Puedes agregar tu usuario al grupo docker:"
    echo "  sudo usermod -aG docker \$USER"
    echo "  Luego cierra sesión y vuelve a iniciarla"
    echo ""
    read -p "¿Deseas continuar de todos modos? (s/n): " -n 1 -r
    echo ""
    if [[ ! $REPLY =~ ^[SsYy]$ ]]; then
        exit 0
    fi
fi

echo ""

# =========================================================================
# Paso 3: Crear Directorios
# =========================================================================

print_header "PASO 2: CREACIÓN DE DIRECTORIOS"

# Directorios en /shared
DIRS=(
    "shared/data"
    "shared/plots"
    "shared/results"
    "shared/animations"
    "docs"
)

for dir in "${DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        print_success "Creado: $dir/"
    else
        print_info "Ya existe: $dir/"
    fi
done

echo ""

# =========================================================================
# Paso 4: Configurar Variables de Entorno
# =========================================================================

print_header "PASO 3: CONFIGURACIÓN DE VARIABLES DE ENTORNO"

if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        print_info "Copiando .env.example a .env..."
        cp .env.example .env
        print_success "Archivo .env creado"
    else
        print_info "Creando archivo .env con valores por defecto..."
        cat > .env << 'EOF'
# Tokens de acceso
JUPYTER_TOKEN=calculo2025
JUPYTER_PORT=8888
STREAMLIT_PORT=8501
SAGE_PORT=8889

# Configuración adicional
TZ=America/Lima
EOF
        print_success "Archivo .env creado con valores por defecto"
    fi
else
    print_info "Archivo .env ya existe"
fi

# Mostrar configuración
print_info "Configuración actual:"
echo ""
cat .env | grep -v '^#' | grep -v '^$'
echo ""

# =========================================================================
# Paso 5: Construir Contenedores
# =========================================================================

print_header "PASO 4: CONSTRUCCIÓN DE CONTENEDORES DOCKER"

print_info "Este proceso puede tomar varios minutos..."
echo ""

read -p "¿Deseas construir los contenedores ahora? (s/n): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[SsYy]$ ]]; then
    print_info "Construyendo contenedores..."

    if docker-compose build; then
        print_success "Contenedores construidos exitosamente"
    else
        print_error "Error al construir contenedores"
        print_info "Revisa los logs arriba para más detalles"
        exit 1
    fi
else
    print_warning "Construcción de contenedores omitida"
    print_info "Puedes construirlos más tarde con:"
    echo "  docker-compose build"
fi

echo ""

# =========================================================================
# Paso 6: Iniciar Servicios
# =========================================================================

print_header "PASO 5: INICIO DE SERVICIOS"

read -p "¿Deseas iniciar los servicios ahora? (s/n): " -n 1 -r
echo ""

if [[ $REPLY =~ ^[SsYy]$ ]]; then
    print_info "Iniciando servicios en segundo plano..."

    if docker-compose up -d; then
        print_success "Servicios iniciados exitosamente"
        echo ""

        # Esperar a que los servicios estén listos
        print_info "Esperando a que los servicios estén listos..."
        sleep 5

        # Mostrar estado
        print_info "Estado de los contenedores:"
        docker-compose ps

    else
        print_error "Error al iniciar servicios"
        exit 1
    fi
else
    print_warning "Inicio de servicios omitido"
    print_info "Puedes iniciarlos más tarde con:"
    echo "  docker-compose up -d"
fi

echo ""

# =========================================================================
# Paso 7: Verificar Servicios
# =========================================================================

if [[ $REPLY =~ ^[SsYy]$ ]]; then
    print_header "PASO 6: VERIFICACIÓN DE SERVICIOS"

    # Esperar un poco más
    sleep 3

    # Verificar cada servicio
    print_info "Verificando accesibilidad de servicios..."

    # Jupyter
    if curl -s http://localhost:8888 > /dev/null; then
        print_success "Jupyter Lab: http://localhost:8888 (token: calculo2025)"
    else
        print_warning "Jupyter Lab: No disponible aún (puede tardar unos segundos más)"
    fi

    # Streamlit
    if curl -s http://localhost:8501 > /dev/null; then
        print_success "Streamlit: http://localhost:8501"
    else
        print_warning "Streamlit: No disponible aún (puede tardar unos segundos más)"
    fi

    # SageMath
    if curl -s http://localhost:8889 > /dev/null; then
        print_success "SageMath: http://localhost:8889 (token: calculo2025)"
    else
        print_warning "SageMath: No disponible aún (puede tardar unos segundos más)"
    fi

    echo ""
fi

# =========================================================================
# Paso 8: Información Final
# =========================================================================

print_header "INSTALACIÓN COMPLETADA"

cat << 'EOF'

  ╔══════════════════════════════════════════════════════════════════╗
  ║           TIF CÁLCULO FASE III - UCSM 2025                       ║
  ║           Plataforma Multi-Motor para Análisis de Derivadas      ║
  ╚══════════════════════════════════════════════════════════════════╝

EOF

print_success "¡Instalación completada exitosamente!"
echo ""

print_info "ACCESO A LOS SERVICIOS:"
echo ""
echo "  1. Dashboard Streamlit (Recomendado para empezar):"
echo "     URL: http://localhost:8501"
echo ""
echo "  2. Jupyter Lab (Notebooks de análisis):"
echo "     URL: http://localhost:8888"
echo "     Token: calculo2025"
echo ""
echo "  3. SageMath Jupyter:"
echo "     URL: http://localhost:8889"
echo "     Token: calculo2025"
echo ""
echo "  4. GNU Octave (Línea de comandos):"
echo "     docker exec -it tif-octave octave"
echo ""

print_info "COMANDOS ÚTILES:"
echo ""
echo "  Ver logs:           docker-compose logs -f"
echo "  Ver estado:         docker-compose ps"
echo "  Detener servicios:  docker-compose down"
echo "  Reiniciar:          docker-compose restart"
echo "  Limpiar todo:       ./scripts/cleanup.sh"
echo ""

print_info "NOTEBOOKS DISPONIBLES:"
echo ""
echo "  Jupyter Lab:"
echo "    - notebooks/01_maximos_minimos.ipynb"
echo "    - notebooks/02_concavidad.ipynb"
echo "    - notebooks/03_trazo_curvas.ipynb"
echo ""
echo "  SageMath:"
echo "    - notebooks/00_comparativa_python_sage.ipynb"
echo "    - notebooks/01_maximos_minimos_sage.ipynb"
echo ""

print_info "SCRIPTS OCTAVE:"
echo ""
echo "  Ejecutar scripts:"
echo "    docker exec -it tif-octave octave --no-gui /workspace/maximos_minimos.m"
echo "    docker exec -it tif-octave octave --no-gui /workspace/concavidad.m"
echo ""

print_warning "IMPORTANTE:"
echo "  - Los servicios pueden tardar 10-30 segundos en estar completamente listos"
echo "  - Si un servicio no responde, espera un poco y recarga la página"
echo "  - Consulta el README.md para más información"
echo ""

print_success "¡Disfruta del TIF Cálculo Fase III!"
echo ""

# =========================================================================
# Final
# =========================================================================

exit 0
