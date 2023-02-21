

from flask import Flask
from flask import render_template, request, redirect
from flaskext.mysql import MySQL

app=Flask(__name__)
#Crear la conexión a la base de datos
mysql=MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='proyectoweb'
mysql.init_app(app)

@app.route('/')
def inicio():
    conexion=mysql.connect()
    return render_template('sitio/index.html')
    

@app.route('/guardar', methods=['POST'])
def guardar():
    __nombres__ = request.form['nombres']
    __edad__ = request.form['edad']
    __email__ = request.form['email']
#Insertar la información a la base de datos
    sql="INSERT INTO usuarios (nombres, edad, email) VALUES (%s, %s, %s)"
    datos=(__nombres__, __edad__, __email__)
    conexion=mysql.connect()
    cursor=conexion.cursor()
    cursor.execute(sql, datos)
    conexion.commit()    
    return redirect('/')

if __name__ =='__main__':
    app.run(debug=True)    