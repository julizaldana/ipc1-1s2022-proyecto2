import json
from flask import Blueprint, jsonify, request
from db.database import libraryDatabase
from libro.models.libro_Model import Libro

libro = Blueprint('libro', __name__, url_prefix="/book")


#METODO POST - CREAR LIBRO

@libro.route('', methods = ['POST'])
def crearlibro():
    body = request.get_json()
    try:
        if("isbn" in body and "author" in body and "title" in body and "year" in body and "no_copies" in body and "no_available_copies" in body):
            if(body["isbn"] != "" and body["author"] != "" and body["title"] != "" and body["year"] != ""):          
                if(body["year"] > 0):
                    if(body["no_copies"] > 0 and body["no_available_copies"] > 0 ):
                        libro = Libro(int(body["isbn"]),body["author"],body["title"],int(body["year"]),int(body["no_copies"]),int(body["no_available_copies"]))
                        if(libraryDatabase.agregar_libro(libro)):
                            return{'msg': 'Libro creado existosamente'}, 201    #Petición completada - created
                        else:
                            return{'msg': 'Existe un problema con el ISBN, posiblemente ya se encuentra registrado'}, 400 #Error al procesar solicitud - badrequest
                    else:
                        return{'msg': 'Existe un error con la cantidad de copias de los libros'}, 400 #Error al procesar solicitud - badrequest
                else:
                    return{'msg': 'Existe un error con la fecha ingresada'}, 400 #Error al procesar solicitud - badrequest        
            else:
                return{'msg': 'Procure ingresar correctamente los campos'}, 400              #Error al procesar solicitud - badrequest 
        else:
            return{'msg': 'Procure ingresar todos los campos correspondientes, para crear un libro'}, 400 #Error al procesar solicitud - badrequest

    except:
        return {'msg': 'Ocurrió un error inesperado en el servidor'}, 500 #Internal Server Error


#METODO PUT - ACTUALIZAR/MODIFICAR LIBRO


@libro.route('', methods = ['PUT'])
def actualizarlibro():
    body = request.get_json()
    try:
        if("isbn" in body and "author" in body and "title" in body and "year" in body):
            if(body["isbn"] != "" and body["author"] != "" and body["title"] != "" and body["year"] != ""):
                if(body["year"] > 0):
                    if(libraryDatabase.modificar_libro(body["isbn"],body["author"],body["title"],body["year"])):
                        return{'msg': 'El libro solicitado, ha sido correctamente modificado'}, 200  #Se acepta la solicitud y se modifica
                        
                    else:
                        return{'msg': 'El  ISBN no ha sido encontrado'}, 404            #Error al procesar solicitud - badrequest 
                else:
                    return{'msg': 'La fecha ingresada para modificar no es correcta'}, 406  #Error al procesar solicitud - badrequest 
            else:
                return{'msg': 'Procure ingresar correctamente los campos'}, 400              #Error al procesar solicitud - badrequest 
        else:
            return{'msg': 'Procure ingresar todos los campos correspondientes, para crear un libro'}, 400 #Error al procesar solicitud - badrequest
    except:
        return {'msg': 'Ocurrió un error en el servidor'}, 500   #Internal Server Error



