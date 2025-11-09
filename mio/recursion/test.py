def busqueda_anidada(lista, elemento):
    """
    Busca un elemento en una lista que puede contener otras listas anidadas,
    utilizando recursión de pila.

    Entradas y restricciones:
    - lista: list, la lista (posiblemente anidada) en la que se buscará.
    - elemento: cualquier tipo, el elemento a buscar.

    Salidas:
    - bool, True si el elemento se encuentra, False en caso contrario.
    """
    # Validación de entradas
    if not isinstance(lista, list):
        raise TypeError("La entrada 'lista' debe ser de tipo list.")

    # Caso base: la lista está vacía
    if not lista:
        return False

    cabeza = lista[0]
    cola = lista[1:]

    # Caso general: se explora la cabeza y luego la cola
    if isinstance(cabeza, list):
        # Si la cabeza es una lista, busca recursivamente en ella.
        # Si se encuentra, el 'or' detiene la búsqueda (evaluación perezosa).
        # Si no, continúa la búsqueda en la cola de la lista original.
        return busqueda_anidada(cabeza, elemento) or busqueda_anidada(cola, elemento)
    elif cabeza == elemento:
        # Caso base: se encontró el elemento en la cabeza
        return True
    else:
        # El elemento no está en la cabeza, buscar en la cola
        return busqueda_anidada(cola, elemento)


if __name__ == "__main__":
    mi_lista = [1, [2, 3, [4]], 5, [[6, 7]]]
    print(f"Buscando el 4: {busqueda_anidada(mi_lista, 4)}")  # True
    print(f"Buscando el 7: {busqueda_anidada(mi_lista, 7)}")  # True
    print(f"Buscando el 8: {busqueda_anidada(mi_lista, 8)}")  # False
    print(f"Buscando el 1: {busqueda_anidada(mi_lista, 1)}")  # True

    # Ejemplo del código original
    # print(busquedaAnidada([1, 2, 3], 0))
