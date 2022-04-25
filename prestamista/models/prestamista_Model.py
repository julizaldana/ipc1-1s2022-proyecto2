class Prestamista():
    def __init__(self, cui, last_name, first_name):
        self.cui = cui
        self.last_name = last_name
        self.first_name = first_name
    
    def prestarLibros(self):
        global libroprestado
        libroprestado = True

    def devolverLibros(self):
        global libroprestado
        libroprestado = False

    def getcui(self):
        return self.cui

        
    def getlastname(self):
        return self.last_name
    
    def getfirstname(self):
        return self.first_name

    def getDataPrestamista(self):
        return{
            "cui": self.cui,
            "first_name": self.first_name,
            "last_name": self.last_name
        }