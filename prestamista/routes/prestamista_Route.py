from flask import Blueprint, jsonify, request
from db.database import libraryDatabase
from prestamista.models.prestamista_Model import Prestamista

prestamista = Blueprint('prestamista', __name__, url_prefix='/person')


##METODO POST - CREAR PRESTAMISTA

@prestamista.route('', methods = ['POST'])
def crearprestamista():
    body = request.get_json()
    try:
        if("cui" in body and "last_name"in body and "first_name" in  body):
            if(body["cui"] != "" and body["last_name"] != "" and body["first_name"] != ""):
                prestamista = Prestamista(body["cui"], body["last_name"], body["first_name"], False)
                if(libraryDatabase.agregar_prestamista(prestamista)):
                    return{'msg': 'El prestamista ha sido creado exitosamente'}, 201     #Petición completada - created
                else:
                    return{'msg': 'Ya existe un prestamista con el mismo número de CUI'}, 400       #Error al procesar solicitud - badrequest 
            else:
                return{'msg': 'Procure que todos los campos sean correctos'}, 400           #Error al procesar solicitud - badrequest
        else:
            return{'msg': 'Procure ingresar todos los campos correspondientes, para crear al prestamista'}, 400         #Error al procesar solicitud - badrequest
    except:
        return {'msg': 'Ocurrió un error inesperado en el servidor'}, 500       #Internal Server Error
