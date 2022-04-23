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

