# CRUD con Python 🐍 y Flask

Este proyecto es un ejemplo de un CRUD (Crear, Leer, Actualizar, Eliminar) desarrollado en Python utilizando el framework Flask. La base de datos utilizada es MySQL, y la conexión se realiza mediante el conector oficial de Python. 


## Resultado final 🚀

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/crud-pytho-con-flask.png)


## Requisitos previos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu sistema:

- Python 3.6 o superior
- MySQL
- Virtualenv o una herramienta similar para entornos virtuales

---

## Configuración del proyecto

A continuación, se detallan los pasos para configurar y ejecutar el proyecto:

### Paso 1: Crear un entorno virtual

Crea un entorno virtual para aislar las dependencias del proyecto:

```bash
virtualenv -p python3 env
# O
python3 -m venv env
```

### Paso 2: Activar el entorno virtual

Activa el entorno virtual ejecutando el siguiente comando:

#### En Windows:
```bash
env\Scripts\activate
```

#### En macOS/Linux:
```bash
source env/bin/activate
```

### Paso 3: Instalar Flask

Una vez dentro del entorno virtual, instala Flask con el siguiente comando:

```bash
pip install flask
```

### Paso 4: Instalar el conector MySQL para Python

Instala el controlador oficial de MySQL para Python ejecutando:

```bash
pip install mysql-connector-python
```

### Paso 5 (opcional): Instalar dependencias desde un archivo `requirements.txt`

Si el proyecto ya incluye un archivo `requirements.txt` con todas las dependencias necesarias, puedes instalar todo de una vez con el siguiente comando:

```bash
pip install -r requirements.txt
```

Esto garantizará que todas las bibliotecas necesarias para el proyecto se instalen automáticamente.

---

## Ejecución del proyecto

Después de completar los pasos de configuración, puedes ejecutar el proyecto con:

```bash
python app.py
```

Asegúrate de que la base de datos esté configurada correctamente y que las credenciales en el código coincidan con las de tu servidor MySQL.



---

## Agradecimientos

Gracias por tu interés en este proyecto. Si tienes preguntas o sugerencias, no dudes en abrir un issue o ponerte en contacto.

