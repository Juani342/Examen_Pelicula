class Pelicula:
    def __init__(self, titulo, director, actores, libreto):
        self.titulo = titulo
        self.director = director
        self.actores = actores
        self.libreto = libreto

    def info_basica(self):
        actores_str = ', '.join(self.actores)
        return f"Nombre: {self.titulo}\nDirector: {self.director}\nActores: {actores_str}\nLibreto: {self.libreto}"


class Accion:
    def caracteristicas_accion(self):
        return "Efectos Visuales: Altos\nRitmo: Rápido\nTensión: Alta"


class Suspenso:
    def caracteristicas_suspenso(self):
        return "Ambientación: Oscura\nMisterio: Sí"


class ElOrigen(Pelicula, Accion):
    def __init__(self, director, actores, libreto):
        super().__init__("El Origen", director, actores, libreto)
        self.tema = "Viaje en los sueños"

    def descripcion(self):
        return f"{self.info_basica()}\nTema: {self.tema}\n{self.caracteristicas_accion()}"


class Interestelar(Pelicula, Accion):
    def __init__(self, director, actores, libreto):
        super().__init__("Interestelar", director, actores, libreto)
        self.tema = "Viaje en el espacio"

    def descripcion(self):
        return f"{self.info_basica()}\nTema: {self.tema}\n{self.caracteristicas_accion()}"


class UnLugarEnSilencio(Pelicula, Accion, Suspenso):
    def __init__(self, director, actores, libreto):
        super().__init__("Un Lugar en Silencio", director, actores, libreto)
        self.tema = "Extraterrestres"

    def descripcion(self):
        return f"{self.info_basica()}\nTema: {self.tema}\n{self.caracteristicas_accion()}\n{self.caracteristicas_suspenso()}"


class UnLugarEnSilencio2(Pelicula, Accion, Suspenso):
    def __init__(self, director, actores, libreto):
        super().__init__("Un Lugar en Silencio 2", director, actores, libreto)
        self.tema = "Extraterrestres y personajes secundarios"

    def descripcion(self):
        return f"{self.info_basica()}\nTema: {self.tema}\n{self.caracteristicas_accion()}\n{self.caracteristicas_suspenso()}"


def main():
    el_origen = ElOrigen("Christopher Nolan", ["Leonardo DiCaprio", "Elliot Page"], "Libreto de Nolan")
    interestelar = Interestelar("Christopher Nolan", ["Matthew McConaughey", "Anne Hathaway"], "Libreto de Nolan")
    un_lugar_en_silencio = UnLugarEnSilencio("John Krasinski", ["Emily Blunt", "John Krasinski"], "Libreto de Krasinski")
    un_lugar_en_silencio_2 = UnLugarEnSilencio2("John Krasinski", ["Emily Blunt", "Cillian Murphy"], "Libreto de Krasinski")

    # Mostrar descripciones con formato vertical
    print(el_origen.descripcion())
    print("\n" + "="*30 + "\n")
    print(interestelar.descripcion())
    print("\n" + "="*30 + "\n")
    print(un_lugar_en_silencio.descripcion())
    print("\n" + "="*30 + "\n")
    print(un_lugar_en_silencio_2.descripcion())


if __name__ == "__main__":
    main()
