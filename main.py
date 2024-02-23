from aspiradora import Aspiradora, AspiradoraInteligente, AspiradoraEstupida
from mundo import Mundo
import threading


def main():
    mundo = Mundo()

    tipo_aspiradora = input(
        "Seleccione el tipo de aspiradora (inteligente / estupida): ")
    if tipo_aspiradora.lower() == "inteligente":
        aspiradora = AspiradoraInteligente(mundo)
    elif tipo_aspiradora.lower() == "estupida":
        aspiradora = AspiradoraEstupida(mundo)
    else:
        print("Tipo de aspiradora no válido.")
        return

    # Función para ejecutar la aspiradora
    def ejecutar_aspiradora():
        while True:
            accion = input(
                "Selecciona una acción (mover derecha, mover izquierda, aspirar, nada): ")
            aspiradora.ejecutar_accion(accion)
            if accion == "q":
                break

    # Crear un thread para ejecutar la aspiradora
    t = threading.Thread(target=ejecutar_aspiradora)
    t.start()

    while True:
        accion = input(
            "Ingrese una acción para ensuciar (A/B) o 'q' para salir: ")
        if accion.lower() == 'q':
            break
        if accion.upper() in ['A', 'B']:
            mundo.ensuciar(accion.upper())
        else:
            print("Cuadrante no válido.")

    t.join()
    print("Programa finalizado.")


if __name__ == "__main__":
    main()
