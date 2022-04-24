class Prestamista():
    def __init__(self, cui, first_name, last_name):
        self.cui = cui
        self.first_name = first_name
        self.last_name = last_name
    
    def prestarLibros(self):
        global libroprestado
        libroprestado = True

    def devolverLibros(self):
        global libroprestado
        libroprestado = False

    def getcui(self):
        return self.cui
    
    def getfirst_name(self):
        return self.first_name

    def getlast_name(self):
        return self.last_name

    

    def getData(self):
        return{
            "cui": self.cui,
            "first_name": self.first_name,
            "last_name": self.last_name
        }