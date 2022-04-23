class Libro():

    def __init__(self, isbn, autor, año, titulo, edicion, temas, nocopias, estanteria, fila):
        self.isbn = isbn
        self.autor = autor
        self.año = año
        self.titulo = titulo
        self.edicion = edicion
        self.temas = temas
        self.nocopias = nocopias
        self.estanteria = estanteria
        self.fila = fila

    def agregarCopias(self, cantidadcopias):
        if(cantidadcopias > 0):
            self.nocopias += cantidadcopias
    
    def restarCopias(self):
        self.nocopias = self.nocopias - 1

    def devolverCopia(self):
        self.nocopias = self.nocopias + 1

    def getIsbn(self):
        return self.isbn
    
    def getAutor(self):
        return self.autor

    def getAño(self):
        return self.año

    def getTitulo(self):
        return self.titulo

    def getEdicion(self):
        return self.edicion
    
    def getTemas(self):
        return self.temas
    
    def getNoCopias(self):
        return self.nocopias

    def getEstanteria(self):
        return self.estanteria

    def getFila(self):
        return self.fila


    def getData(self):
        return {
            "isbn": self.isbn,
            "autor": self.autor,
            "año": self.año,
            "titulo": self.titulo,
            "edicion": self.edicion,
            "temas": self.temas,
            "copias": self.nocopias,
            "estanteria": self.estanteria,
            "fila": self.fila

        }

        