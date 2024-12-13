# Usa la imagen base de Python (versión 3.10 con Alpine)
FROM python:3.10-alpine

# Instala dependencias necesarias para PostgreSQL y compilación
RUN apk update && apk add --no-cache \
    libpq-dev \
    gcc \
    musl-dev \
    postgresql-dev \
    python3-dev \
    libffi-dev \
    && rm -rf /var/cache/apk/*

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia los archivos del proyecto en el contenedor
COPY . .

# Instala las dependencias de Python desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que correrá la aplicación Django
EXPOSE 8000

# Define el comando de inicio del contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
