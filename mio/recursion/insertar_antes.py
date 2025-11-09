def insertarAntes(nuevo, referencia, lista):
    """Programa que inserta una lista antes del elemento de referencia
    Entradas y restricciones:
    - nuevo: (any) nuevo elemento.
    - referencia: (any) referencia.
    - lista: (list) lista de elementos.
    Salida:
    - lista: (list) nueva lista de elementos.
    """
    if not isinstance(lista, list):
        raise Exception("debe ser una lista de elementos.")

    def aux(nue, ref, lst, i):
        # Caso base
        if len(lst) == i:
            return lst.append(nue)
        if lst[i] == ref:
            lst.insert(i, nue)
            return lst
        return aux(nue, ref, lst, i + 1)

    return aux(nuevo, referencia, lista, 0)

if __name__ == "__main__":
    print(insertarAntes('x', 'y', ['a', 'b', 'c', 'y', 'd', 'e', 'y']))