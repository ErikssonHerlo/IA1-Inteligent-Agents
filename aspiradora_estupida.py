import threading
import time


class AspiradoraEstupida(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            print("* Aspiradora estúpida inmóvil...")
            time.sleep(3)  # Simulando el tiempo de espera
