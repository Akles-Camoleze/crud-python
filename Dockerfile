# Use a imagem oficial do Python como base
FROM python:3.10-slim

# Instalar dependências para GTK e PostgreSQL
RUN apt-get update && apt-get install -y \
    libgtk-3-dev \
    libpq-dev \
    libcairo2-dev \
    pkg-config \
    python3-dev \
    g++ \
    cmake \
    libgirepository1.0-dev \
    gir1.2-gtk-4.0 \
    libx11-dev \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    && rm -rf /var/lib/apt/lists/*

# Instalar bibliotecas Python
RUN pip3 install --no-cache-dir \
    setuptools \
    PyGObject \
    psycopg2 \
    pycairo \
    sqlalchemy \
    python-dotenv

# Definir o diretório de trabalho
WORKDIR /app

# Copiar os scripts da aplicação para o contêiner
COPY ./app /app

ENV PYTHONPATH="/."

# Definir o comando de inicialização
CMD ["python3", "main.py"]
