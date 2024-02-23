import threading
import time


class Aspiradora(threading.Thread):
    def __init__(self, mundo, limite_movimientos):
        super().__init__()
        self.mundo = mundo
        self.posicion = 'A'
        self.limpiar = False
        self.limite_movimientos = limite_movimientos
        self.movimientos_realizados = 0
        self.movimientos_totales = 0

    def run(self):
        while True:
            if self.limpiar:
                self.limpiar_cuadrante()
                self.limpiar = False
            else:
                if self.movimientos_realizados < self.limite_movimientos:  # Movimientos permitidos
                    self.moverse()
                    self.verificar_suciedad()
                else:
                    print("\n------------------------------")
                    print(
                        f"- Aspiradora Inteligente alcanzó el límite de {self.limite_movimientos} movimientos.")
                    print(
                        "- Aspiradora Inteligente ha terminado de limpiar, por lo que se queda inmovil.")
                    print("- Si deseas que la Aspiradora Inteligente limpie de nuevo, debes ensuciar alguno de los Cuadros A o B, con los Números 1 o 2 respectivamente.")
                    while not self.limpiar:  # Esperar hasta que se ensucie un cuadrante
                        pass

    def moverse(self):
        print("- Aspiradora Inteligente moviéndose...")
        time.sleep(1)  # Simulando el tiempo de movimiento
        self.posicion = 'B' if self.posicion == 'A' else 'A'
        print("- Aspiradora Inteligente en cuadro", self.posicion)
        self.movimientos_realizados += 1
        self.movimientos_totales += 1

    def verificar_suciedad(self):
        if self.mundo.esta_sucio(self.posicion):
            print("El cuadro está sucio.")
            self.limpiar = True

    def limpiar_cuadrante(self):
        print("Aspirando suciedad en cuadro", self.posicion)
        self.mundo.limpiar(self.posicion)
        self.movimientos_realizados = 0  # Reiniciar contador de movimientos
