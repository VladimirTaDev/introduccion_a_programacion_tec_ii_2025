def insertar_en_lista_ordenada(lista, n):
    """
    Programas que inserta un número en la lista ordenada
    - Entradas y restricciones: lista de números ordenados [list]
    - Salida: número insertado ordenadamente.
    """
    if type(lista) != list:
        raise Exception("lista debe ser una lista.")
    if len(lista) == 0:
        raise Exception("lista no debe estar vacía.")
    for elemento in lista:
        if type(elemento) != int and type(elemento) != float:
            raise Exception("Todos los elementos de la lista deben ser int o float.")
    if type(n) != int and type(n) != float:
        raise Exception("n debe ser un número (int o float).")

    for numero in lista:
        if n <= numero:
            lista.insert(lista.index(numero), n)
            break

    return lista

if __name__ == '__main__':
    print(insertar_en_lista_ordenada([3, 6, 12, 57, 88], 7))
    print(insertar_en_lista_ordenada([1, 3, 6, 9, 10], 0))