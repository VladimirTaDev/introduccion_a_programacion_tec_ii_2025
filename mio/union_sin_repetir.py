
def union_sin_repetidos(d1, d2):
    """
    Programa que retorna solo los pares que no se encuentran repetidos en ambos diccionarios.
    - Entradas y restriciones: diccionarios no vacios.
    - Salidas: valores no repetidos.
    """
    d3 = {}
    for k in d1:
        if k not in d2:
            d3[k] = d1[k]
    for k in d2:
        if k not in d1:
            d3[k] = d2[k]

    return d3

if __name__ == "__main__":
    d1 = {'a': 1, 'b': 2, 'c': 3}
    d2 = {'b': 2, 'd': 4}
    resultado = union_sin_repetidos(d1, d2)
    print("Union sin repetidos:", resultado)  # Salida esperada: {'a': 1, 'c': 3, 'd': 4}
