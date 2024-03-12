import threading
import time
import random


class Aspiradora:
    def __init__(self):
        self.estado = 'limpiar'
        self.cuadrante_actual = 'A'
        self.sucio = False

    def limpiar(self):
        print(f"Aspiradora: Limpiando cuadrante {self.cuadrante_actual}")
        self.sucio = False

    def mover_derecha(self):
        if self.cuadrante_actual == 'A':
            self.cuadrante_actual = 'B'
        print("Aspiradora: Moviendo a la derecha")

    def mover_izquierda(self):
        if self.cuadrante_actual == 'B':
            self.cuadrante_actual = 'A'
        print("Aspiradora: Moviendo a la izquierda")

    def ensuciar(self):
        print(f"¡Cuadrante {self.cuadrante_actual} ensuciado!")
        self.sucio = True

    def actualizar_estado(self, accion, percepcion):
        if percepcion == 'sucio':
            self.estado = 'limpiar'
        elif accion == 'mover_derecha':
            self.estado = 'mover_derecha'
        elif accion == 'mover_izquierda':
            self.estado = 'mover_izquierda'

    def ejecutar_accion(self):
        if self.estado == 'limpiar':
            self.limpiar()
        elif self.estado == 'mover_derecha':
            self.mover_derecha()
        elif self.estado == 'mover_izquierda':
            self.mover_izquierda()
