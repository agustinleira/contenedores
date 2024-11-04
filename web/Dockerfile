# Usa una imagen de Python
FROM python:3.9

# Configura el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# Expone el puerto para la aplicación Flask
EXPOSE 8080

# Comando para correr la aplicación
CMD ["python", "app.py"]
