import threading
import random
import time


class Mundo:
    def __init__(self):
        self.suciedad = {"A": False, "B": False}

    def ensuciar(self, posicion):
        self.suciedad[posicion] = True
        print("Cuadrante", posicion, "ensuciado.")

    def limpiar(self, posicion):
        self.suciedad[posicion] = False
        print("Cuadrante", posicion, "limpiado.")
