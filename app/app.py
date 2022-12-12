from flask import Flask, render_template, request, redirect, url_for, session
from conexionBD import *  #Importando conexion BD


#Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)
application = app


#Lista de Carros
@app.route('/', methods=['GET','POST'])
def inicio():
        conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
        cur      = conexion_MySQLdb.cursor(dictionary=True)

        querySQL = f"SELECT * FROM carros ORDER BY id DESC"
        print(querySQL)
        cur.execute(querySQL) 
        resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
        totalBusqueda = len(resultadoBusqueda) #Total de busqueda
       
        cur.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD

        return render_template('public/layout.html', miData = resultadoBusqueda, total = totalBusqueda)


@app.route('/registrar-carro', methods=['GET','POST'])
def nuevoCarro():
        return render_template('public/nuevoCarro.html')

    
    
#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    if 'conectado' in session:
        return redirect(url_for('inicio'))
    else:
        return render_template('public/index.html')
    
    
    
    
if __name__ == "__main__":
    app.run(debug=True, port=8000)