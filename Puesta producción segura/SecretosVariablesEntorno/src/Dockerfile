# Usa una imagen de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia el requirements.txt y luego instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de la aplicación (incluida la carpeta src)
COPY . .

# Asegura que Python pueda encontrar el módulo src
ENV PYTHONPATH=/app

# Expone el puerto en el que correrá la app
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
