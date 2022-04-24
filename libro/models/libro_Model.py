class Libro():

    def __init__(self, isbn, author, title, year, no_copies, no_available_copies):
        self.isbn = isbn
        self.author = author
        self.title = title
        self.year = year
        self.no_copies = no_copies
        self.no_available_copies = no_available_copies


    def agregarCopias(self, cantidadcopias):
        if(cantidadcopias > 0):
            self.nocopias += cantidadcopias
    
    def restarCopias(self):
        self.nocopias = self.nocopias - 1

    def devolverCopia(self):
        self.nocopias = self.nocopias + 1

    def getisbn(self):
        return self.isbn
    
    def getauthor(self):
        return self.author

    def gettitle(self):
        return self.title

    def getyear(self):
        return self.year

    def getno_copies(self):
        return self.no_copies

    def getno_available_copies(self):
        return self.no_available_copies



    def getData(self):
        return {
            "isbn": self.isbn,
            "author": self.author,
            "title": self.title,
            "year": self.year,
            "no_copies": self.no_copies,
            "no_available_copies": self.no_available_copies,

        }

        