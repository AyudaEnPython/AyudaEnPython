def saludar(nombre: str) -> str:
    """Saludo de bienvenida a los integrantes de la comunidad
    'Ayuda en Python'.

    :param nombre: Nombre del usuario
    :type nombre: str
    :return: Mensaje de bienvenida
    :rtype: str
    """
    return f"Hola {nombre.capitalize()}, " \
        "'Ayuda en Python' te da la bienvenida!"


if __name__ == "__main__":
    nombre = input("Ingresa tu nombre: ")
    print(saludar(nombre))