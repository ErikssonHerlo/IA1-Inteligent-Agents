import threading
import time


class Aspiradora(threading.Thread):
    def __init__(self, mundo):
        super().__init__()
        self.mundo = mundo
        self.posicion = 'A'
        self.limpiar = False

    def run(self):
        while True:
            if self.limpiar:
                self.limpiar_cuadrante()
                self.limpiar = False
            else:
                self.moverse()
                self.verificar_suciedad()

    def moverse(self):
        print("Aspiradora moviéndose...")
        time.sleep(1)  # Simulando el tiempo de movimiento
        self.posicion = 'B' if self.posicion == 'A' else 'A'
        print("Aspiradora en cuadro", self.posicion)

    def verificar_suciedad(self):
        if self.mundo.esta_sucio(self.posicion):
            print("El cuadro está sucio.")
            self.limpiar = True

    def limpiar_cuadrante(self):
        print("Aspirando suciedad en cuadro", self.posicion)
        self.mundo.limpiar(self.posicion)
