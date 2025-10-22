def validar_lista_numerica(lista):
    """
    Función que valída si una lista es numérica.
    - Entradas y restricciones: lista (int)
    - Salida: True (Bool) si la lista es numérica.
    """
    if type(lista) != list:
        raise Exception("la entrada debe ser una lista")

    for elemento in lista:
        if type(elemento) != int:
            return False
    return True

def todos_pares(lista):
    """
    Función que valída si una lista contiene solo pares.
    - Entradas y restricciones: lista (int)
    - Salida: True (Bool) si la lista es par.
    """
    if not validar_lista_numerica(lista):
        raise Exception("la entrada debe ser una lista con números")

    for elemento in lista:
        if elemento % 2 == 0:
            continue
        else:
            return False

    return True

if __name__ == "__main__":
    print(validar_lista_numerica([1,2,3,])) # True
    print(todos_pares([1,2,3,])) # False
    print(todos_pares([2, 4, 8, ]))  # Truee