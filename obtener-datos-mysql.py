#En este codigo, haremos una llamada a la base de datos indicada abajo
# para que se lance una consulta desde un archivo xxx.html y que muestre
# lo que tiene exactamente dicha tabla que deseamos. Luego, los datos
# se devuelven como una respuesta JSON al frontend xxx.html.

#Una vez que despliegues este microservicio de Python en Cloud Run, 
#puedes hacer una solicitud AJAX desde tu página HTML (index.html) a la
#URL completa de este servicio (https://nombre-del-servicio-b.cloudrun.app/obtener_datos) 
#para obtener los datos de la base de datos y mostrarlos en tu página 
#HTML como se describió anteriormente.

# Importamos las bibliotecas necesarias
import sqlalchemy  # Para interactuar con la base de datos
from flask import Flask, jsonify  # Para crear la aplicación web y devolver respuestas JSON

# Creamos una instancia de la aplicación Flask
app = Flask(__name__)

# Configuración de la conexión a la base de datos MySQL
connection_name = "proyecto1-404122:europe-southwest1:mysql-instance-test1"  # Nombre de la instancia de Cloud SQL
db_name = "nombresyapellidos"  # Nombre de la base de datos
db_user = "root"  # Nombre de usuario de la base de datos
db_password = "Ed3r2022-1"  # Contraseña de la base de datos

# Definimos una ruta en la que se obtendrán los datos
@app.route('/obtener_datos', methods=['GET'])
def obtener_datos():
    try:
        # Crea una conexión a la base de datos MySQL utilizando SQLAlchemy
        db = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername="mysql+pymysql",  # Usamos el controlador MySQL
                username=db_user,  # Nombre de usuario de la base de datos
                password=db_password,  # Contraseña de la base de datos
                database=db_name,  # Nombre de la base de datos
                query={"unix_socket": "/cloudsql/{}".format(connection_name)},  # Configuración de la conexión a Cloud SQL
            ),
            pool_size=5,  # Número máximo de conexiones en la piscina de conexiones
            max_overflow=2,  # Número máximo de conexiones que se pueden crear por encima de pool_size
            pool_timeout=30,  # Tiempo máximo de espera para obtener una conexión de la piscina
            pool_recycle=1800,  # Tiempo en segundos antes de reciclar conexiones en la piscina
        )

        # Ejecuta una consulta SQL para obtener los datos (ajusta esta consulta según tus necesidades)
        query = "SELECT * FROM tabla_nombres"
        
        with db.connect() as conn:
            result = conn.execute(query)  # Ejecuta la consulta y obtén el resultado
            data = [dict(row) for row in result]  # Convierte los resultados en una lista de diccionarios

        # Devuelve los datos como una respuesta JSON al frontend
        return jsonify(data)

    except Exception as e:
        # Si ocurre un error, devuelve un mensaje de error
        return 'Error: {}'.format(str(e))

# Punto de entrada del programa cuando se ejecuta el archivo directamente
if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la aplicación Flask en modo de depuración
