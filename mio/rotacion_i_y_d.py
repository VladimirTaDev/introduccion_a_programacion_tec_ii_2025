def rotacionDerecha(m):
    """
    Rota una matriz 90 grados en sentido horario (derecha)
    Entradas y restricciones:
    - m: list de listas, matriz válida no vacía
    Salidas:
    - list de listas, matriz rotada 90° a la derecha
    """
    if type(m) != list or len(m) == 0:
        raise Exception("m debe ser una lista no vacía")
    if type(m[0]) != list or len(m[0]) == 0:
        raise Exception("m debe ser una matriz válida")

    rotacion = []
    for col in range(len(m[0])):
        nueva_fila = []
        for fila in reversed(m):
            nueva_fila.append(fila[col])
        rotacion.append(nueva_fila)

    return rotacion

def rotacionIzquierda(m):
    """
    Rota una matriz 90 grados en sentido antihorario (izquierda)
    Entradas y restricciones:
    - m: list de listas, matriz válida no vacía
    Salidas:
    - list de listas, matriz rotada 90° a la izquierda
    """
    if type(m) != list or len(m) == 0:
        raise Exception("m debe ser una lista no vacía")
    if type(m[0]) != list or len(m[0]) == 0:
        raise Exception("m debe ser una matriz válida")

    rotacion = []
    for col in range(len(m[0]) - 1, -1, -1):
        nueva_fila = []
        for fila in m:
            nueva_fila.append(fila[col])
        rotacion.append(nueva_fila)

    return rotacion

if __name__ == "__main__":
    matriz = [[1, 2, 3, 4], [5, 6, 7, 8]]

    print("Matriz original:")
    print(matriz)
    print("\nRotación derecha:")
    print(rotacionDerecha(matriz))
    print("\nRotación izquierda:")
    print(rotacionIzquierda(matriz))

