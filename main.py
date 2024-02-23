from aspiradora import Aspiradora
from aspiradora_estupida import AspiradoraEstupida
from mundo import Mundo
import threading


def main():
    mundo = Mundo()
    limite_movimientos = 3  # Definir el límite de movimientos
    aspiradora_inteligente = Aspiradora(mundo, limite_movimientos=5)
    aspiradora_estupida = AspiradoraEstupida()

    aspiradora_inteligente.start()
    aspiradora_estupida.start()

    while True:
        print("\n--- Menú ---")
        print("1. Enviar suciedad a cuadro A")
        print("2. Enviar suciedad a cuadro B")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mundo.ensuciar_cuadro('A')
            aspiradora_inteligente.limpiar = True  # Iniciar limpieza en cuadro A
        elif opcion == '2':
            mundo.ensuciar_cuadro('B')
            aspiradora_inteligente.limpiar = True  # Iniciar limpieza en cuadro B
        elif opcion == '3':
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")


if __name__ == "__main__":
    main()
