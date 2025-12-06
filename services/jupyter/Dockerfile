FROM jupyter/scipy-notebook:latest

USER root

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    vim \
    && rm -rf /var/lib/apt/lists/*

USER jovyan

# Instalar paquetes Python necesarios (versiones compatibles)
RUN pip install --no-cache-dir \
    sympy \
    numpy \
    scipy \
    matplotlib \
    plotly \
    pandas \
    seaborn \
    ipywidgets \
    kaleido \
    nbconvert \
    python-docx

# Habilitar extensiones de Jupyter
RUN jupyter labextension install jupyterlab-plotly || true

WORKDIR /workspace

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
