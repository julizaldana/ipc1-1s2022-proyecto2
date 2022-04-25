from uuid import uuid4;

class Prestamo():
    def __init__(self, cui, isbn, titulo, fechaparaprestamo, fechadevolucion):
        self.uuid = uuid4()
        self.CUI = cui
        self.isbn = isbn
        self.titulo = titulo
        self.fechaparaprestamo = fechaparaprestamo
        self.fechadevolucion = fechadevolucion

    def getCUI(self):
        return self.CUI

    def getisbn(self):
        return self.isbn

    def getitulo(self):
        return self.titulo

    def getfechaparaprestamo(self):
        return self.fechaparaprestamo

    def getfechadevolucion(self):
        return self.fechadevolucion

    def putfechadevuelta(self, fecha):
        self.fechadevolucion = fecha

    def getdata(self):
        return{
            "uuid": self.uuid,
            "cui": self.CUI,
            "isbn": self.isbn,
            "fechaparaprestamo": self.fechaparaprestamo,
            "fechadevolucion": self.fechadevolucion

    }    