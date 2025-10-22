def insertar(s1, s2):
    """
    Función que inserta un string en medio de otro.
    Entradas y restricciones:
    - s1, s2: strings.
    Salidas:
    String con la primera mitad de s1 concatenada con
    s2 y con la segunda mitad de s1.
    """
    if type(s1) != str:
        raise Exception("s1 debe ser un string.")
    if type(s2) != str:
        raise Exception("s2 debe ser un string.")
    mitad1 = s1[: len(s1) // 2]
    mitad2 = s1[len(s1) // 2 :]
    resultado = mitad1 + s2 + mitad2
    return resultado
