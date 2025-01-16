# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app2

# Copiar los archivos de la aplicación al contenedor
COPY app2.py /app2

# Instalar Flask
RUN pip install Flask

# Exponer el puerto en el que corre la aplicación
EXPOSE 8092

# Comando para ejecutar la aplicación
CMD ["python", "app2.py"]
