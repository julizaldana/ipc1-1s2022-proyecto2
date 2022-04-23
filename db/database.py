class Database():

    def __init__(self):
        self.__cuiprestamista = []
        self.__libros = []
        self.__isbnlibros =[]
        self.__prestamistas = []
        self.__prestamos = []
    

## Funciones para prestamistas

    def agregarPrestamista(self, prestamista):
        if not(prestamista.getCUI() in self.__cuiprestamista):
            self.__prestamistas.append(prestamista)
            self.__cuiprestamista.append(prestamista.getCUI())
            print(self.__prestamistas)
            return True
        return False

    def obtenerPrestamista(self, cui):
        if int(cui) in self.__cuiprestamista:
            for prestam in self.__prestamistas:
                if(prestam.getCUI() == int(cui)):
                    return prestam
        return None




## Funciones para libros

    def agregarLibro(self, libro):
        if not(libro.getisbn() in self.__isbnlibros):
            self.__libros.append(libro)
            self.__isbnlibros.append(libro.getIsbn())
            return True
        return False


## Funciones para filtrar libros

    def obtenerLibroIsbn(self, isbn):
        if isbn in self.__libros:
            for lbrs in self.__libros:
                if(lbrs.getIsbn() == isbn):
                    return lbrs
        return None

    def obtenerLibroTitulo(self, titulo):
        for lbrs in self.__libros:
            if(lbrs.getTitulo() == titulo):
                return lbrs
        return None

    def obtenerLibroAutor(self, autor):
        for lbrs in self.__libros:
            if(lbrs.getAutor() == autor):
                return lbrs
        return None


    def obtenerLibroFechas(self, fechainicial, fechafinal):
        for lbrs in self.__libros:
            if(lbrs.getAño() > fechainicial and lbrs.año() < fechafinal):
                return lbrs
        return None



    def modificarLibro(self, libro):
        contador = 0
        for lbrs in self.__libros:
            if(lbrs.getIsbn()==libro.getIsbn()):
                libro.agregarCopias
                self.__libros.insert(contador,libro)
                return True #se puede modificar libro
            contador = contador + 1
        return False #no se puede modificar libro

