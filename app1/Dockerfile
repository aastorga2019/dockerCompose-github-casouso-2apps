# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app1

# Copiar los archivos de la aplicación al contenedor
COPY app1.py /app1

# Instalar Flask
RUN pip install Flask

# Exponer el puerto en el que corre la aplicación
EXPOSE 8091

# Comando para ejecutar la aplicación
CMD ["python", "app1.py"]
