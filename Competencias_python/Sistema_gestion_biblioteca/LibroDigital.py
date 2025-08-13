from Libro import Libro

class LibroDigital(Libro):

    def __init__(self, titulo, autor, anio_publicacion, estado, formato):
        super().__init__(titulo, autor, anio_publicacion, estado)
        self.formato = formato

    def __str__(self):
        return f"{super().__str__()}, Formato: {self.formato}"

