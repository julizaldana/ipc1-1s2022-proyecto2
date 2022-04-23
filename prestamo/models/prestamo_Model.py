from uuid import uuid4;

class Prestamo():
    def __init__(self, CUI, nombre, apellido, isbn, titulo, fechaparaprestamo, fechadevolucion):
        self.uuid = uuid4()
        self.cui = cui
        self.nombre = nombre
        self.apellido = apellido
        self.isbn = isbn
        self.titulo = titulo
        self.fechaparaprestamo = fechaparaprestamo
        self.fechadevolucion = fechadevolucion