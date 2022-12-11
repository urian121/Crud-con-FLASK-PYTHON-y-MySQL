# PASO 1, Crear mi entorno virtual
#  virtualenv -p python3 env o python3 -m venv env

# PASO 2, Activar el entorno virtual ejecutando;
#  . env/Scripts/activate  
 
# PASO 3, Ya dentro del entorno virtual instalar flask
#  pip install flask

# PASO 4, Instalar Python MySQL Connector, es una bibliote (Driver) para conectar Python con MySQL
# pip install mysql-connector-python

# PASO 5, Lista todos mis paquetes
# pip list  o pip freeze

# Crear/Actualizar el fichero requirements.txt:
# pip freeze > requirements.txt

# IMPORTANTE, para correr el proyecto solo debes ejecutar el archivo
# requirements.txt con el comando pip install -r requirements.txt en el 
# mismo se encuentran todas las dependecias del proyecto.

# (env)$ deactivate   Para desactivar nuestro entono virtual
 
# Comando para actualizar pip: python -m pip install --upgrade pip

# https://www.youtube.com/watch?v=E0Ys_ntvshY   y   https://hackersandslackers.com/configure-flask-applications/
# Variables de Entorno con Python (.env) | python-dotenv | python-decouple
# He instalado pip install python-dotenv  para crear entornos de variables
# pip install python-decouple


# flask run
Queremos instalar el paquete python-dotenv para poder almacenar nuestras variables MySQL fuera de nuestro código.

pip install python-dotenv