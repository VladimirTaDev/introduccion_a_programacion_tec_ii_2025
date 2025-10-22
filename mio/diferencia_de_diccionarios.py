from copy import deepcopy

def diferencia_de_diccionarios(d1, d2):
    """
    Programa que retorna solo la diferencia de dos diccionarios.
    - Entradas y restriciones: diccionarios no vacios.
    - Salidas: diferencia de diccionarios
    """
    d3 = deepcopy(d1)
    for k in d2:
        if k in d1:
            d3.pop(k)
    return d3

if __name__ == "__main__":
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'b': 2, 'd': 4}
    resultado = diferencia_de_diccionarios(d1, d2)
    print("Diferencia de diccionarios:", resultado)  # Salida esperada: {'a': 1, 'c': 3}

