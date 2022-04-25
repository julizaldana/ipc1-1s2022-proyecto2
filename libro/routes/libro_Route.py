from db.database import libraryDatabase
from flask import Blueprint, jsonify, request
from libro.models.libro_Model import Libro

libro = Blueprint('libro', __name__, url_prefix="/book")

@libro.route("", methods = ["POST"])
def crear():
    body = request.get_json()
    try:
        if("isbn" in body and "author" in body and "title" in body and "year" in body and "no_copies" and "no_available_copies" in body ):
            if(body['no_copies']>0):
                libro = Libro(body["isbn"],body["author"],int(body["year"]),body["title"])
                if(libraryDatabase.agregarLibro(libro)):
                    return{'msg': "Libro creado exitosamente"}, 201
                else:
                    return{'msg': 'Existe un problema con el ISBN'}, 404
            else:
                return{'msg': 'Existe un error con la cantidad de copias de los libros'}, 404
        else:
            return{'msg': "Procure ingresar todos los campos correspondientes, para crear un libro"}, 404

    except:
        return {'msg': "Ocurrió un error inesperado en el servidor"}, 500

