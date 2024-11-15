class UnLugarEnSilencio():
    def __init__(self, director, actores, libreto):
        super().__init__("Un Lugar en Silencio", director, actores, libreto)
        self.tema = "Extraterrestres"

    def descripcion(self):
        return f"{self.info_basica()}, Tema: {self.tema}, {self.caracteristicas_accion()}, {self.caracteristicas_suspenso()}"


