class Libro():


    def __init__(self, titulo, autor, anio_publicacion, estado):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.__estado = estado

    def get_estado(self):
        return self.__estado
    
    def set_estado(self, nuevo_estado):
        self.__estado = nuevo_estado
        
    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio_publicacion}, Estado: {self.__estado}"

    def to_csv(self):
        return f"{self.titulo},{self.autor},{self.anio_publicacion},{self.__estado}"

    @classmethod
    def from_csv(cls, linea):
        try:
            titulo, autor, anio, estado = linea.strip().split(",", 3)
            return cls(titulo, autor, int(anio), estado)
        except ValueError as e:
            print(f"Error al procesar la línea: {linea}. Detalle: {e}")
            return None