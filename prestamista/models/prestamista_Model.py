class Prestamista():
    def __init__(self, CUI, nombre, apellido):
        self.CUI = CUI
        self.nombre = nombre
        self.apellido = apellido
    
    def prestarLibros(self):
        global libroprestado
        libroprestado = True

    def devolverLibros(self):
        global libroprestado
        libroprestado = False

    def getCUI(self):
        return self.CUI
    
    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    

    def getData(self):
        return{
            "cui": self.CUI,
            "nombre": self.nombre,
            "apellido": self.apellido
        }