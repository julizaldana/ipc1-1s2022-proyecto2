class Database():

    def __init__(self):
        self.__cuiprestamista = []
        self.__libros = []
        self.__isbnlibros =[]
        self.__prestamistas = []
    

## Funciones para libros

    def agregar_libro(self, libro):
        if not(libro.getisbn() in self.__isbnlibros):
            self.__libros.append(libro)
            self.__isbnlibros.append(libro.getisbn())
            return True
        return False


## Funciones para filtrar y buscar libros

    def obtenerlibro(self):
        librosguardado = []
        for all_libros in self.__libros:
            librosguardado.append(all_libros.getData())
        return librosguardado

    def obtenerlibro_title(self, titulo):
        librosguardado = []
        for all_libros in self.__libros:
            if(all_libros.gettitle() == titulo):
                librosguardado.append(all_libros.getData())
        return librosguardado

    def obtenerlibro_author(self, autor):
        librosguardado = []
        for all_libros in self.__libros:
            if(all_libros.getauthor() == autor):
                librosguardado.append(all_libros.getData())
        return librosguardado


    def obtenerlibro_date(self, year_from, year_to):
        librosguardado = []
        for all_libros in self.__libros:
            if(all_libros.getyear() > year_from and all_libros.year() < year_to):
                librosguardado.append(all_libros.getData())
        return librosguardado



    def modificar_libro(self, isbn, author, title, year):
        cont = 0
        if int(isbn) in self.__isbnlibros:
            for all_libros in self.__libros:
                if(all_libros.getisbn()==isbn):
                    self.__libros[cont].setauthor(author)
                    self.__libros[cont].settitle(title)
                    self.__libros[cont].setyear(year)
                    return True #se puede modificar libro
                cont = cont + 1 
        return False #no se puede modificar libro



## Funciones para prestamistas

    def agregar_prestamista(self, prestamista):
        if not(prestamista.getcui() in self.__cuiprestamista):
            self.__prestamistas.append(prestamista)
            self.__cuiprestamista.append(prestamista.getcui())
            return True
        return False


libraryDatabase = Database()