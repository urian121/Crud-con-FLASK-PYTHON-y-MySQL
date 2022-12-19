from flask import Flask, render_template, request, redirect, url_for, jsonify
from conexionBD import *  #Importando conexion BD


#Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)
application = app



def listaCarros():
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur      = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = f"SELECT * FROM carros ORDER BY id DESC"
    print(querySQL)
    cur.execute(querySQL) 
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda


#Lista de Carros
@app.route('/', methods=['GET','POST'])
def inicio():
    return render_template('public/layout.html', miData = listaCarros())



#RUTAS
@app.route('/registrar-carro', methods=['GET','POST'])
def addCarro():
    return render_template('public/acciones/add.html')

@app.route('/form-update-carro/<string:id>', methods=['GET','POST'])
def updateCarro(id):
    msg =''
    if request.method == 'GET':
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM carros WHERE id = %s LIMIT 1", [id])
        resultData = cursor.fetchone() #Devolviendo solo 1 registro
        print(resultData)
        if resultData:
            return render_template('public/acciones/update.html',  dataInfo = resultData)
        else:
            msg="No existe el Carro"
            return render_template('public/layout.html', miData = listaCarros(), mensaje = msg, tipo_msg = 0)
            
    return render_template('public/layout.html',  miData = listaCarros())    
 
 
#Registrando nuevo carro
@app.route('/carro', methods=['POST'])
def registrarCarro():
    msg =''
    if request.method == 'POST':
        marca               = request.form['marca']
        modelo              = request.form['modelo']
        year                = request.form['year']
        color               = request.form['color']
        puertas             = request.form['puertas']
        favorito            = request.form['favorito']
        
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
        
            
        sql         = ("INSERT INTO carros(marca, modelo, year, color, puertas, favorito) VALUES (%s, %s, %s, %s, %s, %s)")
        valores     = (marca, modelo, year, color, puertas, favorito)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        msg = 'Registro con exito'
        
        print(cursor.rowcount, "registro Insertado")
        print("1 registro insertado, id", cursor.lastrowid)
  
        return render_template('public/layout.html', miData = listaCarros(), msg='Formulario enviado')
    else:
        return render_template('public/layout.html', msg = 'Metodo HTTP incorrecto')   
  
  
  
@app.route('/ver-detalles-del-carro/<int:idCarro>', methods=['GET', 'POST'])
def detalleCarro(idCarro):
    msg =''
    if request.method == 'GET':
        #print(idCarro)
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM carros WHERE id ='%s'" % (idCarro,))
        resultadoQuery = cursor.fetchone()
        
        cursor.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        if resultadoQuery:
            return render_template('public/acciones/view.html', infoCarro = resultadoQuery)
        else:
            msg="No exite el Carro"
            return render_template('public/acciones/layout.html', mensaje = msg, tipo_mensaje = 0)
    return redirect(url_for('inicio'))
    

@app.route('/actualizar-carro/<string:idCarro>', methods=['POST'])
def  recibeActualizarCarro(idCarro):

    if request.method == 'POST':
        marca           = request.form['marca']
        modelo          = request.form['modelo']
        year            = request.form['year']
        color           = request.form['color']
        puertas         = request.form['puertas']
        favorito        = request.form['favorito']
        print(idCarro)
        conexion_MySQLdb = connectionBD()
        cur = conexion_MySQLdb.cursor(dictionary=True)
        cur.execute("""
            UPDATE carros
            SET 
                marca   = %s,
                modelo  = %s,
                year    = %s,
                color   = %s,
                puertas = %s,
                favorito= %s
            WHERE id=%s
            """, (marca,modelo, year, color, puertas, favorito, idCarro ))
        conexion_MySQLdb.commit()
        
        cur.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
    return render_template('public/layout.html', miData = listaCarros())     


#Eliminar carro
@app.route('/borrar-carro', methods=['GET', 'POST'])
def borrarCarro():
    
    if request.method == 'POST':
        idCarro    = request.form['id']
        
        conexion_MySQLdb = connectionBD() #Hago instancia a mi conexion desde la funcion
        cur              = conexion_MySQLdb.cursor(dictionary=True)
        cur.execute('DELETE FROM carros WHERE id=%s', (idCarro,))
        conexion_MySQLdb.commit()
        
        #Nota: retorno solo un json y no una vista para evitar refescar la vista
        return jsonify(dataR = ["respuesta", 1])
  
  
#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('inicio'))
    
    
    
    
if __name__ == "__main__":
    app.run(debug=True, port=8000)