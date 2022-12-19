from flask import Flask, render_template, request, redirect, url_for, jsonify
from controller.controllerCarro import *


#Declarando nombre de la aplicación e inicializando, crear la aplicación Flask
app = Flask(__name__)
application = app



#Creando mi decorador para el home, el cual retornara la Lista de Carros
@app.route('/', methods=['GET','POST'])
def inicio():
    return render_template('public/layout.html', miData = listaCarros())


#RUTAS
@app.route('/registrar-carro', methods=['GET','POST'])
def addCarro():
    return render_template('public/acciones/add.html')


 
#Registrando nuevo carro
@app.route('/carro', methods=['POST'])
def formAddCarro():
    msg =''
    if request.method == 'POST':
        marca               = request.form['marca']
        modelo              = request.form['modelo']
        year                = request.form['year']
        color               = request.form['color']
        puertas             = request.form['puertas']
        favorito            = request.form['favorito']

        resultData = registrarCarro(marca, modelo, year, color, puertas, favorito)
        if(resultData ==1):
            msg = 'Registro con exito'
            return render_template('public/layout.html', miData = listaCarros(), msg='Formulario enviado')
        else:
            return render_template('public/layout.html', msg = 'Metodo HTTP incorrecto')   
    

@app.route('/form-update-carro/<string:id>', methods=['GET','POST'])
def formViewUpdate(id):
    msg =''
    if request.method == 'GET':
        resultData = updateCarro(id)
        if resultData:
            return render_template('public/acciones/update.html',  dataInfo = resultData)
        else:
            msg="No existe el Carro"
            return render_template('public/layout.html', miData = listaCarros(), mensaje = msg, tipo_msg = 0)
    else:
        return render_template('public/layout.html', miData = listaCarros())          
 
   
  
@app.route('/ver-detalles-del-carro/<int:idCarro>', methods=['GET', 'POST'])
def viewDetalleCarro(idCarro):
    msg =''
    if request.method == 'GET':
        resultData = detallesdelCarro(idCarro)
        
        if resultData:
            return render_template('public/acciones/view.html', infoCarro = resultData)
        else:
            msg="No exite el Carro"
            return render_template('public/acciones/layout.html', mensaje = msg, tipo_mensaje = 0)
    return redirect(url_for('inicio'))
    

@app.route('/actualizar-carro/<string:idCarro>', methods=['POST'])
def  formActualizarCarro(idCarro):
    msg=''
    if request.method == 'POST':
        marca           = request.form['marca']
        modelo          = request.form['modelo']
        year            = request.form['year']
        color           = request.form['color']
        puertas         = request.form['puertas']
        favorito        = request.form['favorito']
        
        resultData = recibeActualizarCarro(marca, modelo, year, color, puertas, favorito, idCarro)
        if(resultData ==1):
            return render_template('public/layout.html', miData = listaCarros())
        else:
            msg ='No se actualizo el registro'
            return render_template('public/layout.html', miData = listaCarros(), mensaje = msg, tipo_mensaje = 0)
               


#Eliminar carro
@app.route('/borrar-carro', methods=['GET', 'POST'])
def formViewBorrarCarro():
    
    if request.method == 'POST':
        idCarro    = request.form['id']
        resultData = eliminarCarro(idCarro)

        if resultData ==1:
            #Nota: retorno solo un json y no una vista para evitar refescar la vista
            return jsonify(data = ["respuesta", 1])
        else: 
            return jsonify(data = ["respuesta", 0])

        
  
  
#Redireccionando cuando la página no existe
@app.errorhandler(404)
def not_found(error):
    return redirect(url_for('inicio'))
    
    
    
    
if __name__ == "__main__":
    app.run(debug=True, port=8000)