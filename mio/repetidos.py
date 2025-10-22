def repetidos(lista):
    """
    Función que extrae elementos repetidos de una lista.
    - Entradas y restricciones: lista no vacía (list)
    - Salida: lista con solo los elementos repetidos.
    """
    if type(lista) != list and len(lista) != 0:
        raise Exception("La entrada debe ser una lista no vacía")

    return list({x for x in lista if lista.count(x) > 1})

if __name__ == "__main__":
    print(repetidos([2, 5, 6, 8, 2]))      # esperado: [2]
    print(repetidos(['a', 'b', 'c', 'd'])) # esperado: []
    print(repetidos([1, 4, 6, 1, 4, 7, 9, 1])) # esperado: [1, 4]
