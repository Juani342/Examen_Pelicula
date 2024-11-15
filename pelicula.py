class Pelicula:
    def __init__(self, titulo, director, actores, libreto):
        self.titulo = titulo
        self.director = director
        self.actores = actores
        self.libreto = libreto

    def info_basica(self):
        return f"Título: {self.titulo}, Director: {self.director}, Actores: {', '.join(self.actores)}, Libreto: {self.libreto}"


