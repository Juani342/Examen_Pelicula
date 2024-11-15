class Accion:
    def __init__(self):
        self.efectos_visuales = True
        self.ritmo = "Rápido"
        self.tension = "Alta"

    def caracteristicas_accion(self):
        return f"Efectos Visuales: {self.efectos_visuales}, Ritmo: {self.ritmo}, Tensión: {self.tension}"
