from aspiradora_estupida import AspiradoraEstupida
from aspiradora_inteligente import AspiradoraInteligente
from mundo import Mundo
import threading


def main():

    # Iniciar el hilo para la aspiradora estúpida
    aspiradora_estupida = AspiradoraEstupida()
    hilo_estupida = threading.Thread(target=aspiradora_estupida.ejecutar)
    hilo_estupida.start()

    # Iniciar el hilo para la aspiradora inteligente
    aspiradora_inteligente = AspiradoraInteligente()
    hilo_inteligente = threading.Thread(target=aspiradora_inteligente.ejecutar)
    hilo_inteligente.start()

    while True:
        ensuciar = input(
            "¿Qué cuadrante desea ensuciar (A/B)? (Presione 'q' para salir): \n\n")
        if ensuciar.lower() == 'q':
            break
        elif ensuciar.upper() in ['A', 'B']:
            aspiradora_inteligente.ensuciar(ensuciar.upper())
        else:
            print("Cuadrante no válido. Intente de nuevo.")


if __name__ == "__main__":
    main()
