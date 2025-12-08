#!/bin/bash
# Script de inicio para SageMath Jupyter

exec sage --notebook=jupyter \
    --ip=0.0.0.0 \
    --port=8888 \
    --no-browser \
    --allow-root \
    --NotebookApp.token='calculo2025'
