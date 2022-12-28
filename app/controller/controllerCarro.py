from random import sample
from conexionBD import *  #Importando conexion BD



#Creando una funcion para obtener la lista de carros.
def listaCarros():
    conexion_MySQLdb = connectionBD() #creando mi instancia a la conexion de BD
    cur      = conexion_MySQLdb.cursor(dictionary=True)

    querySQL = "SELECT * FROM carros ORDER BY id DESC"
    cur.execute(querySQL) 
    resultadoBusqueda = cur.fetchall() #fetchall () Obtener todos los registros
    totalBusqueda = len(resultadoBusqueda) #Total de busqueda
    
    cur.close() #Cerrando conexion SQL
    conexion_MySQLdb.close() #cerrando conexion de la BD    
    return resultadoBusqueda




def updateCarro(id=''):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM carros WHERE id = %s LIMIT 1", [id])
        resultQueryData = cursor.fetchone() #Devolviendo solo 1 registro
        return resultQueryData
    
    
    
def registrarCarro(marca='', modelo='', year='', color='', puertas='', favorito='', nuevoNombreFile=''):       
        conexion_MySQLdb = connectionBD()
        cursor           = conexion_MySQLdb.cursor(dictionary=True)
            
        sql         = ("INSERT INTO carros(marca, modelo, year, color, puertas, favorito, foto) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        valores     = (marca, modelo, year, color, puertas, favorito, nuevoNombreFile)
        cursor.execute(sql, valores)
        conexion_MySQLdb.commit()
        cursor.close() #Cerrando conexion SQL
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        resultado_insert = cursor.rowcount #retorna 1 o 0
        ultimo_id        = cursor.lastrowid #retorna el id del ultimo registro
        return resultado_insert
  

def detallesdelCarro(idCarro):
        conexion_MySQLdb = connectionBD()
        cursor = conexion_MySQLdb.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM carros WHERE id ='%s'" % (idCarro,))
        resultadoQuery = cursor.fetchone()
        cursor.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        
        return resultadoQuery
    
    

def  recibeActualizarCarro(marca, modelo, year, color, puertas, favorito, nuevoNombreFile, idCarro):
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
                favorito= %s,
                foto    = %s
            WHERE id=%s
            """, (marca,modelo, year, color, puertas, favorito, nuevoNombreFile,  idCarro))
        conexion_MySQLdb.commit()
        
        cur.close() #cerrando conexion de la consulta sql
        conexion_MySQLdb.close() #cerrando conexion de la BD
        resultado_update = cur.rowcount #retorna 1 o 0
        return resultado_update
 

#Crear un string aleatorio para renombrar la foto 
# y evitar que exista una foto con el mismo nombre
def stringAleatorio():
    string_aleatorio = "0123456789abcdefghijklmnopqrstuvwxyz_"
    longitud         = 20
    secuencia        = string_aleatorio.upper()
    resultado_aleatorio  = sample(secuencia, longitud)
    string_aleatorio     = "".join(resultado_aleatorio)
    return string_aleatorio