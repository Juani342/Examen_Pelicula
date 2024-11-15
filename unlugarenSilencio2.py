class UnLugarEnSilencio2():
    def __init__(self, director, actores, libreto):
        super().__init__("Un Lugar en Silencio 2", director, actores, libreto)
        self.tema = "Extraterrestres y personajes secundarios"

    def descripcion(self):
        return f"{self.info_basica()}, Tema: {self.tema}, {self.caracteristicas_accion()}, {self.caracteristicas_suspenso()}"
