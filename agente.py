modelo = {
    ('sin-moneda', 'pedir-moneda', 'moneda'): "recibi-moneda",
    ('recibi-moneda', 'pedir-codigo', 'c1'): "servido-c1",
    ('recibi-moneda', 'pedir-codigo', 'c2'): "servido-c2",
    ('recibi-moneda', 'pedir-codigo', 'c3'): "servido-c3",
    ('servido-c1', 'servir-c1-esperar', 'servido'): "sin-moneda",
    ('servido-c2', 'servir-c2-esperar', 'servido'): "sin-moneda",
    ('servido-c3', 'servir-c3-esperar', 'servido'): "sin-moneda",
}

acciones = {
    "pedir-moneda": "Mostrar en pantalla 'Pedir moneda'",
    "pedir-codigo": "Mostrar en pantalla 'Pedir codigo'",
    "servir-c1-esperar": "Mostrar en pantalla 'Sirviendo refresco 1 y esperar'",
    "servir-c2-esperar": "Mostrar en pantalla 'Sirviendo refresco 2 y esperar'",
    "servir-c3-esperar": "Mostrar en pantalla 'Sirviendo refresco 3 y esperar'"
}


def actualizar_estado(estado, accion, percepcion):
    for key in modelo.keys():
        if key[0] == estado and key[1] == accion and key[2] == percepcion:
            return modelo[key]
    return "estado no definido"


def actualizar_accion(estado):
    for key in modelo.keys():
        if key[0] == estado:
            return key[1]
    return "accion no definida"


def main():
    estado = 'sin-moneda'
    accion = 'pedir-moneda'

    while True:
        print("Estado actual:", estado)
        print("Acción actual:", acciones.get(accion, "Acción no definida"))
        percepcion = input("Ingresar percepcion: ")
        estado_anterior = estado

        # Actualizar el estado basado en la percepción actual y la acción anterior
        estado = actualizar_estado(estado, accion, percepcion)
        if (estado == "estado no definido"):
            print("Estado no definido, intente de nuevo.")
            estado = estado_anterior
            continue
        # Actualizar la acción basada en el modelo
        accion = actualizar_accion(estado)

        # Mostrar la acción correspondiente al estado actual y la percepción actual
        texto_accion = acciones.get(accion, "Acción no definida")
        print(texto_accion)


if __name__ == "__main__":
    main()
