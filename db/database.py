class Database():

    def __init__(self):
        self.__cuiprestamista = []
        self.__libros = []
        self.__isbnlibros =[]
        self.__prestamistas = []
    

## Funciones para prestamistas

    def agregar_prestamista(self, prestamista):
        if not(prestamista.getcui() in self.__cuiprestamista):
            self.__prestamistas.append(prestamista)
            self.__cuiprestamista.append(prestamista.getcui())
            return True
        return False

    def obtener_prestamista(self, cui):
        if int(cui) in self.__cuiprestamista:
            for prestam in self.__prestamistas:
                if(prestam.getcui() == int(cui)):
                    return prestam
        return None




## Funciones para libros

    def agregar_libro(self, libro):
        if not(libro.getisbn() in self.__isbnlibros):
            self.__libros.append(libro)
            self.__isbnlibros.append(libro.getisbn())
            return True
        return False


## Funciones para filtrar libros

    def obtenerLibro(self):
        librosguardado = []
        for lbrs in self.__libros:
            librosguardado.append(lbrs.getData())
        return librosguardado

    def obtenerLibroTitulo(self, titulo):
        librosguardado = []
        for lbrs in self.__libros:
            if(lbrs.gettitle() == titulo):
                librosguardado.append(lbrs.getData())
        return librosguardado

    def obtenerLibroAutor(self, autor):
        librosguardado = []
        for lbrs in self.__libros:
            if(lbrs.getauthor() == autor):
                librosguardado.append(lbrs.getData())
        return librosguardado


    def obtenerLibroFechas(self, fechainicial, fechafinal):
        librosguardado = []
        for lbrs in self.__libros:
            if(lbrs.getyear() > fechainicial and lbrs.year() < fechafinal):
                librosguardado.append(lbrs.getData())
        return librosguardado



    def modificar_libro(self, isbn, author, title, year):
        cont = 0
        if int(isbn) in self.__isbnlibros:
            for lbrs in self.__libros:
                if(lbrs.getisbn()==isbn):
                    self.__libros[cont].setauthor(author)
                    self.__libros[cont].settitle(title)
                    self.__libros[cont].setyear(year)
                    return True #se puede modificar libro
                cont = cont + 1 
        return False #no se puede modificar libro




libraryDatabase = Database()