#!/bin/bash

# =========================================================================
# TIF Cálculo Fase III - UCSM 2025
# Script de Limpieza
# Autor: Aron
# =========================================================================

# Colores
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

print_header() {
    echo -e "${BLUE}=========================================================================${NC}"
    echo -e "${BLUE}  $1${NC}"
    echo -e "${BLUE}=========================================================================${NC}"
}

print_success() { echo -e "${GREEN}✓ $1${NC}"; }
print_error() { echo -e "${RED}✗ $1${NC}"; }
print_warning() { echo -e "${YELLOW}⚠ $1${NC}"; }
print_info() { echo -e "${BLUE}ℹ $1${NC}"; }

# =========================================================================
# Banner
# =========================================================================

clear
print_header "TIF CÁLCULO FASE III - SCRIPT DE LIMPIEZA"

echo ""
echo "  Este script puede:"
echo "  1. Detener contenedores"
echo "  2. Eliminar contenedores"
echo "  3. Eliminar imágenes Docker"
echo "  4. Limpiar volúmenes"
echo "  5. Limpiar caché de Docker"
echo "  6. Limpiar archivos temporales del proyecto"
echo ""
print_warning "ADVERTENCIA: Algunas opciones eliminarán datos permanentemente"
echo ""

# =========================================================================
# Menú
# =========================================================================

echo "Selecciona el nivel de limpieza:"
echo ""
echo "  1) Ligera   - Solo detener contenedores"
echo "  2) Media    - Detener y eliminar contenedores"
echo "  3) Completa - Detener, eliminar contenedores e imágenes"
echo "  4) Profunda - Todo lo anterior + limpiar volúmenes y caché"
echo "  5) Cancelar"
echo ""
read -p "Opción (1-5): " -n 1 -r
echo ""
echo ""

OPTION=$REPLY

# =========================================================================
# Limpieza Ligera
# =========================================================================

if [[ $OPTION =~ ^[1234]$ ]]; then
    print_header "PASO 1: DETENER CONTENEDORES"

    if docker-compose ps -q | grep -q .; then
        print_info "Deteniendo contenedores..."
        if docker-compose down; then
            print_success "Contenedores detenidos"
        else
            print_error "Error al detener contenedores"
        fi
    else
        print_info "No hay contenedores en ejecución"
    fi
    echo ""
fi

# =========================================================================
# Limpieza Media
# =========================================================================

if [[ $OPTION =~ ^[234]$ ]]; then
    print_header "PASO 2: ELIMINAR CONTENEDORES"

    print_warning "Esto eliminará los contenedores (no las imágenes)"
    read -p "¿Continuar? (s/n): " -n 1 -r
    echo ""

    if [[ $REPLY =~ ^[SsYy]$ ]]; then
        if docker-compose rm -f; then
            print_success "Contenedores eliminados"
        else
            print_info "No había contenedores para eliminar"
        fi
    else
        print_info "Eliminación de contenedores omitida"
    fi
    echo ""
fi

# =========================================================================
# Limpieza Completa
# =========================================================================

if [[ $OPTION =~ ^[34]$ ]]; then
    print_header "PASO 3: ELIMINAR IMÁGENES DOCKER"

    print_warning "Esto eliminará las imágenes Docker del proyecto"
    print_info "Tendrás que reconstruirlas con 'docker-compose build'"
    read -p "¿Continuar? (s/n): " -n 1 -r
    echo ""

    if [[ $REPLY =~ ^[SsYy]$ ]]; then
        # Obtener imágenes del proyecto
        IMAGES=$(docker images | grep 'tif-calculo' | awk '{print $3}')

        if [ -n "$IMAGES" ]; then
            print_info "Eliminando imágenes del proyecto..."
            echo "$IMAGES" | xargs docker rmi -f 2>/dev/null || true
            print_success "Imágenes eliminadas"
        else
            print_info "No hay imágenes del proyecto para eliminar"
        fi
    else
        print_info "Eliminación de imágenes omitida"
    fi
    echo ""
fi

# =========================================================================
# Limpieza Profunda
# =========================================================================

if [[ $OPTION == "4" ]]; then
    print_header "PASO 4: LIMPIEZA PROFUNDA"

    # Limpiar volúmenes
    print_warning "¿Eliminar volúmenes de Docker? (esto eliminará datos persistentes)"
    read -p "¿Continuar? (s/n): " -n 1 -r
    echo ""

    if [[ $REPLY =~ ^[SsYy]$ ]]; then
        if docker-compose down -v; then
            print_success "Volúmenes eliminados"
        else
            print_info "No había volúmenes para eliminar"
        fi
    else
        print_info "Eliminación de volúmenes omitida"
    fi
    echo ""

    # Limpiar caché de Docker
    print_info "Limpiando caché de Docker..."
    if docker system prune -f; then
        print_success "Caché de Docker limpiado"
    fi
    echo ""

    # Limpiar archivos temporales del proyecto
    print_header "PASO 5: LIMPIAR ARCHIVOS TEMPORALES"

    print_info "Limpiando archivos temporales del proyecto..."

    # Python cache
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete 2>/dev/null || true
    find . -type f -name "*.pyo" -delete 2>/dev/null || true

    # Jupyter checkpoints
    find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} + 2>/dev/null || true

    # Logs
    find . -type f -name "*.log" -delete 2>/dev/null || true

    print_success "Archivos temporales eliminados"
    echo ""

    # Opcionalmente limpiar resultados
    print_warning "¿Eliminar archivos generados en /shared? (plots, results, etc.)"
    read -p "¿Continuar? (s/n): " -n 1 -r
    echo ""

    if [[ $REPLY =~ ^[SsYy]$ ]]; then
        rm -rf shared/plots/* 2>/dev/null || true
        rm -rf shared/results/* 2>/dev/null || true
        rm -rf shared/animations/* 2>/dev/null || true
        print_success "Archivos en /shared eliminados"
    else
        print_info "Archivos en /shared conservados"
    fi
    echo ""
fi

# =========================================================================
# Cancelar
# =========================================================================

if [[ $OPTION == "5" ]]; then
    print_info "Limpieza cancelada"
    exit 0
fi

# =========================================================================
# Resumen Final
# =========================================================================

if [[ $OPTION =~ ^[1234]$ ]]; then
    print_header "LIMPIEZA COMPLETADA"

    echo ""
    print_success "Limpieza finalizada exitosamente"
    echo ""

    case $OPTION in
        1)
            print_info "Se realizó limpieza LIGERA"
            echo "  - Contenedores detenidos"
            ;;
        2)
            print_info "Se realizó limpieza MEDIA"
            echo "  - Contenedores detenidos"
            echo "  - Contenedores eliminados"
            ;;
        3)
            print_info "Se realizó limpieza COMPLETA"
            echo "  - Contenedores detenidos"
            echo "  - Contenedores eliminados"
            echo "  - Imágenes eliminadas"
            ;;
        4)
            print_info "Se realizó limpieza PROFUNDA"
            echo "  - Contenedores detenidos"
            echo "  - Contenedores eliminados"
            echo "  - Imágenes eliminadas"
            echo "  - Volúmenes limpiados"
            echo "  - Caché de Docker limpiado"
            echo "  - Archivos temporales eliminados"
            ;;
    esac

    echo ""
    print_info "Para volver a iniciar el proyecto:"
    echo "  ./scripts/setup.sh"
    echo ""
    print_info "O manualmente:"
    echo "  docker-compose build"
    echo "  docker-compose up -d"
    echo ""
else
    print_error "Opción inválida"
    exit 1
fi

exit 0
