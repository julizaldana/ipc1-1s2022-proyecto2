import json
from flask import Blueprint, jsonify, request
from db.database import libraryDatabase
from libro.models.libro_Model import Libro

libro = Blueprint('libro', __name__, url_prefix="/book")

@libro.route("", methods = ["POST"])
def crear():
    body = request.get_json()
    try:
        if("isbn" in body and "author" in body and "title" in body and "year" in body and "no_copies" and "no_available_copies" in body):
            if(body["isbn"] != "" and body["author"] != "" and body["title"] != "" and body["year"] != ""):
                if (body["year"] > 0):
                    if(body["no_copies"] > 0 and body["no_availabe_copies"] > 0):                    
                        if(libraryDatabase.agregar_libro(libro)):
                            return{'msg': 'Libro creado exitosamente'}, 201     #Petición completada - created
                        else:
                            return{'msg': 'Existe un problema con el ISBN, posiblemente ya se encuentra registrado'}, 400 #Error al procesar solicitud - badrequest
                    else:
                        return{'msg': 'Existe un error con la cantidad de copias de los libros'}, 400 #Error al procesar solicitud - badrequest
                else:
                    return{'msg': 'Existe un error con la fecha ingresada'}, 400 #Error al procesar solicitud - badrequest
        
        else:
            return{'msg': "Procure ingresar todos los campos correspondientes, para crear un libro"}, 400 #Error al procesar solicitud - badrequest

    except:
        return {'msg': "Ocurrió un error inesperado en el servidor"}, 500 #Internal Server Error

