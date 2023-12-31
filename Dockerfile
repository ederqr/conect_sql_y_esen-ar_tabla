# Use the official Python image from Docker Hub
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copiar el nombre del script de phyton aqui. en este caso seria el 
#obtener-datos-mysql.py que es el que quiero hacer
COPY obtener-datos-mysql.py /app/

# Install any dependencies your Python script may have
# Uncomment and modify this section as needed
# RUN pip install -r requirements.txt

# Expose the port that your application will listen on (if applicable)
# EXPOSE 8080

# Define the command to run your Python script
# Asegúrate de guardar este Dockerfile en la misma carpeta que tu código Python
# y poner el nombre aqui del archivo py
CMD ["python", "obtener-datos-mysql.py"]

