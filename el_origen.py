class ElOrigen():
    def __init__(self, director, actores, libreto):
        super().__init__("El Origen", director, actores, libreto)
        self.tema = "Viaje en los sueños"

    def descripcion(self):
        return f"{self.info_basica()}, Tema: {self.tema}, {self.caracteristicas_accion()}"

