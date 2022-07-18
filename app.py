import os

from flask import Flask ,jsonify,request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app=Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)
# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:RoPV_1840151087@localhost/bd_app'
                                        #user:clave@localhost/nombreBaseDatos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)
ma=Marshmallow(app)
# defino la tabla
class Mascota(db.Model):   # la clase Producto hereda de db.Model     
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    tipo=db.Column(db.String(100))
    nombre=db.Column(db.String(100))
    foto=db.Column(db.String(100))
    edad=db.Column(db.Integer)
    descripcion=db.Column(db.String(100))
    fechaPerdida=db.Column(db.String(100))
    def __init__(self,tipo,nombre,foto,edad,descripcion,fechaPerdida):   #crea el  constructor de la clase
        self.tipo=tipo
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.foto=foto
        self.edad=edad
        self.descripcion=descripcion
        self.fechaPerdida=fechaPerdida
 
db.create_all()  # crea las tablas
#  ************************************************************
 
class MascotaSchema(ma.Schema):
    class Meta:
        fields=('id','tipo','nombre','foto','edad','descripcion','fechaPerdida')
mascota_schema=MascotaSchema()            # para crear un mascota
mascota_schema=MascotaSchema(many=True)  # multiples registros
 
 
# crea los endpoint o rutas (json)
@app.route('/mascotas',methods=['GET'])
def get_Mascotas():
    all_mascotas=Mascota.query.all()     # query.all() lo hereda de db.Model
    result=mascota_schema.dump(all_mascotas)  # .dump() lo hereda de ma.schema
    return jsonify(result)
 
 
@app.route('/mascotas/<id>',methods=['GET'])
def get_mascota(id):
    mascota=Mascota.query.get(id)
    return mascota_schema.jsonify(mascota)

@app.route('/mascotas/<id>',methods=['DELETE'])
def delete_mascota(id):
    mascota=Mascota.query.get(id)
    db.session.delete(mascota)
    db.session.commit()
    return mascota_schema.jsonify(mascota)
 
@app.route('/mascotas', methods=['POST']) # crea ruta o endpoint
def create_mascota():
    print(request.json)     
    tipo=request.json['tipo']
    nombre=request.json['nombre']
    foto=request.json['foto']
    edad=request.json['edad']
    descripcion=request.json['descripcion']
    fechaPerdida=request.json['fechaPerdida']
    new_mascota=Mascota(tipo,nombre,foto,edad,descripcion,fechaPerdida)
    db.session.add(new_mascota)
    db.session.commit()
    return mascota_schema.jsonify(new_mascota)

@app.route('/mascotas/<id>' ,methods=['PUT'])
def update_mascota(id):
    mascota=Mascota.query.get(id)
    #'id','tipo','nombre','edad','fechaPerdida'
    tipo=request.json['tipo']
    nombre=request.json['nombre']
    foto=request.json['foto']
    edad=request.json['edad']
    descripcion=request.json['descripcion']
    fechaPerdida=request.json['fechaPerdida']
    mascota.tipo=tipo
    mascota.nombre=nombre
    mascota.foto=foto
    mascota.edad=edad
    mascota.descripcion=descripcion
    mascota.fechaPerdida=fechaPerdida
    db.session.commit()
    return mascota_schema.jsonify(mascota)

# programa principal *******************************
if __name__=='__main__':  
    app.run(debug=True, port=5000)  