import threading
import time


class AspiradoraInteligente:
    def __init__(self):
        self.estado = 'limpiar'
        self.cuadrante_actual = 'A'
        self.memoria_cuadrantes = {'A': False, 'B': False}

        # Tabla de estados, acciones y percepciones
        self.tabla_transiciones = {
            ('A', 'limpiar', False): ('mover_a', 'Mover a cuadrante B'),
            ('A', 'limpiar', True): ('limpiar', 'Limpiando cuadrante A'),
            ('B', 'limpiar', False): ('mover_a', 'Mover a cuadrante A'),
            ('B', 'limpiar', True): ('limpiar', 'Limpiando cuadrante B'),
            ('A', 'mover_a', False): ('mover_a', 'Moviendo a cuadrante B'),
            ('B', 'mover_a', False): ('mover_a', 'Moviendo a cuadrante A'),
            ('A', 'mover_a', True): ('limpiar', 'Moviendo a cuadrante B'),
            ('B', 'mover_a', True): ('limpiar', 'Moviendo a cuadrante A'),
        }

    def limpiar(self):
        if self.memoria_cuadrantes[self.cuadrante_actual]:
            print(f"Aspiradora: Limpiando cuadrante {self.cuadrante_actual}")
            self.memoria_cuadrantes[self.cuadrante_actual] = False
        else:
            print(f"El cuadrante {self.cuadrante_actual} ya está limpio.")

    def mover_a(self, cuadrante):
        print(f"Aspiradora Inteligente: Moviendo a cuadrante {cuadrante}")
        self.cuadrante_actual = cuadrante

    def ensuciar(self, cuadrante):
        print(f"¡Cuadrante {cuadrante} ensuciado!")
        self.memoria_cuadrantes[cuadrante] = True

    def ejecutar_accion(self):
        print(
            f"\nPosición actual de la Aspiradora Inteligente: Cuadrante {self.cuadrante_actual}")
        accion, mensaje = self.tabla_transiciones[(
            self.cuadrante_actual, self.estado, self.memoria_cuadrantes[self.cuadrante_actual])]
        if accion == 'limpiar':
            self.limpiar()
        elif accion == 'mover_a':
            self.mover_a('A' if self.cuadrante_actual == 'B' else 'B')

    def ejecutar(self):
        while True:
            time.sleep(2)
            self.ejecutar_accion()
