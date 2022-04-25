from uuid import uuid4;

class Prestamo():
    def __init__(self, cui, isbn):
        self.uuid = uuid4()
        self.CUI = cui
        self.isbn = isbn


    def getCUI(self):
        return self.CUI

    def getisbn(self):
        return self.isbn

    def getdata(self):
        return{
            "uuid": self.uuid,
            "cui": self.CUI,
            "isbn": self.isbn,

    }    