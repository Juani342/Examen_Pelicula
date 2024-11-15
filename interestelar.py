class Interestelar():
    def __init__(self, director, actores, libreto):
        super().__init__("Interestelar", director, actores, libreto)
        self.tema = "Viaje en el espacio"

    def descripcion(self):
        return f"{self.info_basica()}, Tema: {self.tema}, {self.caracteristicas_accion()}"
