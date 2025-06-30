# Usamos una imagen base ligera con Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo en el contenedor
WORKDIR /app

# Copiamos el código de la aplicación en el contenedor
COPY . .

# Actualizamos pip e instalamos las dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Exponemos el puerto en el que Streamlit escuchará
EXPOSE 8000

# Ejecutamos Streamlit en el puerto 8000
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8000", "--server.address=0.0.0.0"]
