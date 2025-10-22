def esListaOrdenada(lista):
    """
    Función que recibe una lista y revisa si está ordenada de menor a mayor.
    Entradas y restricciones: lista: list no vacia con números.
    Salida: Bool True si la lista es ordenada.
    """
    if type(lista) != list or len(lista) == 0:
        raise Exception("lista debe ser una lista no vacía.")
    for elemento in lista:
        if type(elemento) != int and type(elemento) != float:
            raise Exception("Todos los elementos deben ser int o float.")

    lista_ordenada = True
    numero_anterior = 0
    for numero in lista:
        if numero >= numero_anterior:
            numero_anterior = numero
        else:
            lista_ordenada = False
            break

    return print(f"Es lista ordenada: {lista_ordenada}")

if __name__ == "__main__":
    esListaOrdenada([2, 5, 8, 12, 12, 15]) # True
    esListaOrdenada([5, 7, 3, 2, 0]) # False
    esListaOrdenada([1]) #  True