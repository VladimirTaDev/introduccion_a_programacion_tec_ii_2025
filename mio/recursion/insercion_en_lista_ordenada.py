def insertar_en_lista_ordenada(lista, elemento):
    """
    Programa que inserta un elemento en lista ordenada manteniendo el orden.
    Entradas y restricciones:
    - lista: (list, int) positivo.
    - elemento: (int) positivo.
    Salida:
    - lista: (list, int) positivo.
    """

    # Chequeo de restricciones.
    if type(lista) != list and len(lista) < 0:
        raise Exception("Debe ser una lista no vacía.")
    for e in lista:
        if type(e) != int:
            raise Exception("Los elementos de la lista deben ser int")

    def aux_cola(l, e, i):
        if i == len(l):
            l.append(e)
            return l
        elif l[i] > e:
            l.insert(i, e)
            return l
        else:
            return aux_cola(l, e, i + 1)

    def aux_pila(l_resto, e):
        # Caso base lista vacía
        if l_resto == []:
            return [e]
        # Caso base índice encontrado.
        if l_resto[0] > e:
            return [e] + l_resto
        # Caso general.
        return [l_resto[0]] + aux_pila(l_resto[1:], e)

    return aux_pila(lista, elemento)

if __name__ == "__main__":
    print(insertar_en_lista_ordenada([1,2,3], 2))