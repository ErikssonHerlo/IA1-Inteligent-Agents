import time


class Aspiradora:
    def __init__(self, mundo):
        self.mundo = mundo
        self.posicion = "A"

    def mover_derecha(self):
        self.posicion = "B"
        print("Aspiradora se movió a la derecha.")

    def mover_izquierda(self):
        self.posicion = "A"
        print("Aspiradora se movió a la izquierda.")

    def aspirar(self):
        self.mundo.limpiar(self.posicion)
        print("Aspiradora ha aspirado el cuadrante", self.posicion)

    def ejecutar_accion(self, accion):
        if accion == "derecha":
            self.mover_derecha()
        elif accion == "izquierda":
            self.mover_izquierda()
        elif accion == "aspirar":
            self.aspirar()
        elif accion == "nada":
            print("Aspiradora no hace nada.")
        else:
            print("Acción no reconocida.")

    def ejecutar(self):
        while True:
            accion = input(
                "Selecciona una acción (derecha, izquierda, aspirar, nada): ")
            self.ejecutar_accion(accion)
            time.sleep(1)


class AspiradoraInteligente(Aspiradora):
    def ejecutar(self):
        while True:
            if self.mundo.suciedad[self.posicion]:
                self.aspirar()
            else:
                if self.posicion == "A":
                    self.mover_derecha()
                else:
                    self.mover_izquierda()
            time.sleep(1)


class AspiradoraEstupida(Aspiradora):
    def ejecutar(self):
        while True:
            self.aspirar()
            if self.posicion == "A":
                self.mover_derecha()
            else:
                self.mover_izquierda()
            time.sleep(1)
