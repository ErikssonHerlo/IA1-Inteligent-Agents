class Mundo:
    def __init__(self):
        self.suciedad = {'A': False, 'B': False}

    def esta_sucio(self, cuadro):
        return self.suciedad[cuadro]

    def limpiar(self, cuadro):
        print("El cuadro", cuadro, "ha sido limpiado.")
        self.suciedad[cuadro] = False

    def ensuciar_cuadro(self, cuadro):
        print("El cuadro", cuadro, "se ha ensuciado.")
        self.suciedad[cuadro] = True
