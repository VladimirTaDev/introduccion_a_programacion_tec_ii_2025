# cuadradoMagico([[2, 7, 6], [9, 5, 1], [4, 3, 8]])

def cuadradoMagico(cuadrado):
    """
    Verifica si el cuadrado dado es un cuadrado mágico.
    Entradas y restricciones:
    - cuadrado: lista de listas, debe ser una matriz cuadrada de enteros.
    Salidas:
    - bool, True si el cuadrado es mágico (todas las filas, columnas y diagonales
      suman lo mismo), False en caso contrario.
    """
    if not isinstance(cuadrado, list):
        raise Exception("cuadrado debe ser una lista.")

    if not es_matriz_cuadrada(cuadrado):
        return False

    suma_objetivo = sumar_filas(cuadrado)
    if suma_objetivo is False:
        return False

    suma_cols = sumar_columnas(cuadrado)
    if suma_cols != suma_objetivo:
        return False

    suma_diag1 = sumar_diagonal_1(cuadrado)
    if suma_diag1 != suma_objetivo:
        return False

    suma_diag2 = sumar_diagonal_2(cuadrado)
    if suma_diag2 != suma_objetivo:
        return False

    return True

def es_lista_enteros(obj):
    """
    Verifica que obj es una lista y que todos sus elementos son enteros.
    Entradas y restricciones:
    - obj: objeto a verificar.
    Salidas:
    - bool, True si obj es una lista y todos sus elementos son enteros,
      False en caso contrario.
    """
    if not isinstance(obj, list):
        return False
    return all(isinstance(x, int) for x in obj)

def es_matriz_enteros(mat):
    """
    Verifica que mat es una lista de listas y todos los elementos son enteros.
    Entradas y restricciones:
    - mat: any, objeto a verificar.
    Salidas:
    - bool, True si mat es una matriz (lista de listas) y todos sus elementos
      son enteros, False en caso contrario.
    """
    if not isinstance(mat, list):
        return False
    if len(mat) == 0:
        return True
    for fila in mat:
        if not isinstance(fila, list):
            return False
        if not all(isinstance(x, int) for x in fila):
            return False
    return True

def es_matriz_cuadrada(mat):
    """
    Verifica que mat es una matriz y que tiene el mismo número de filas y columnas.
    Entradas y restricciones:
    - mat: objeto a verificar.
    Salidas:
    - bool, True si mat es una matriz cuadrada (mismo número de filas y columnas)
      con todos sus elementos enteros, False en caso contrario.
    """
    if not es_matriz_enteros(mat):
        return False
    n = len(mat)
    if n == 0:
        return True
    return all(len(fila) == n for fila in mat)

def es_matriz_con_enteros_consecutivos(mat):
    """
    Verifica que una matriz cuadrada contenga los enteros consecutivos de 1 a n².
    Entradas y restricciones:
    - mat: objeto a verificar.
    Salidas:
    - bool, True si mat es una matriz cuadrada que contiene exactamente los
      enteros del 1 a n² (donde n es el tamaño de la matriz), False en caso contrario.
    """
    if not es_matriz_cuadrada(mat):
        return False

    n = len(mat)
    if n == 0:
        return False

    # Crear un conjunto con todos los números de la matriz.
    numeros_en_matriz = set()
    for fila in mat:
        for numero in fila:
            numeros_en_matriz.add(numero)

    # Crear un conjunto con los números consecutivos de 1 a n².
    numeros_esperados = set(range(1, n * n + 1))

    # Verificar que ambos conjuntos sean iguales.
    return numeros_en_matriz == numeros_esperados

def sumar_filas(cuadrado): # Verifica si las filas suman lo mismo.
    """
    Verifica si todas las filas del cuadrado suman lo mismo.
    Entradas y restricciones:
    - cuadrado: lista de listas, debe ser una matriz cuadrada de enteros.
    Salidas:
    - int, la suma común de todas las filas si son iguales.
    - bool (False), si las filas no suman lo mismo.
    """
    if not isinstance(cuadrado, list):
        raise Exception("cuadrado debe ser una lista.")
    if len(cuadrado) == 0:
        raise Exception("cuadrado no puede estar vacío.")
    for fila in cuadrado:
        if not isinstance(fila, list):
            raise Exception("Cada fila de cuadrado debe ser una lista.")

    suma_filas = [] # Lista para almacenar las sumas de las filas
    # Sumar las filas del cuadrado
    for fila in cuadrado:
        suma = 0
        for numero in fila:
            suma += numero
        suma_filas.append(suma)

    # Verificar si todas las sumas de las filas son iguales.
    todos_iguales = True

    for num in suma_filas:
        if num != suma_filas[0]:
            todos_iguales = False
            break

    if todos_iguales:
        return suma_filas[0]
    return todos_iguales

def sumar_columnas(cuadrado): # Verifica si las columnas suman lo mismo.
    """
    Verifica si todas las columnas del cuadrado suman lo mismo.
    Entradas y restricciones:
    - cuadrado: lista de listas, debe ser una matriz cuadrada de enteros.
    Salidas:
    - int, la suma común de todas las columnas si son iguales.
    - bool (False), si las columnas no suman lo mismo.
    """
    if not isinstance(cuadrado, list):
        raise Exception("cuadrado debe ser una lista.")
    if len(cuadrado) == 0:
        raise Exception("cuadrado no puede estar vacío.")
    for fila in cuadrado:
        if not isinstance(fila, list):
            raise Exception("Cada fila de cuadrado debe ser una lista.")

    suma_columnas = [] # Lista para almacenar las sumas de las columnas
    # Sumar las columnas del cuadrado
    for i in range(len(cuadrado)):
        suma = 0
        for fila in cuadrado:
            suma += fila[i]
        suma_columnas.append(suma)

    # Verificar si todas las sumas de las columnas son iguales.
    todos_iguales = True

    for num in suma_columnas:
        if num != suma_columnas[0]:
            todos_iguales = False
            break

    if todos_iguales:
        return suma_columnas[0]
    return todos_iguales

def sumar_diagonal_1(cuadrado):
    """
    Calcula la suma de la diagonal principal del cuadrado (de arriba-izquierda a abajo-derecha).
    Entradas y restricciones:
    - cuadrado: lista de listas, debe ser una matriz cuadrada de enteros.
    Salidas:
    - int, la suma de los elementos en la diagonal principal.
    """
    if not isinstance(cuadrado, list):
        raise Exception("cuadrado debe ser una lista.")
    if len(cuadrado) == 0:
        raise Exception("cuadrado no puede estar vacío.")
    for fila in cuadrado:
        if not isinstance(fila, list):
            raise Exception("Cada fila de cuadrado debe ser una lista.")

    suma_diagonal_1 = 0
    for i in range(len(cuadrado)):
        suma_diagonal_1 += cuadrado[i][i]
    return suma_diagonal_1

def sumar_diagonal_2(cuadrado):
    """
    Calcula la suma de la diagonal secundaria del cuadrado (de arriba-derecha a abajo-izquierda).
    Entradas y restricciones:
    - cuadrado: lista de listas, debe ser una matriz cuadrada de enteros.
    Salidas:
    - int, la suma de los elementos en la diagonal secundaria.
    """
    if not isinstance(cuadrado, list):
        raise Exception("cuadrado debe ser una lista.")
    if len(cuadrado) == 0:
        raise Exception("cuadrado no puede estar vacío.")
    for fila in cuadrado:
        if not isinstance(fila, list):
            raise Exception("Cada fila de cuadrado debe ser una lista.")

    suma_diagonal_2 = 0
    n = len(cuadrado)
    for i in range(n):
        suma_diagonal_2 += cuadrado[i][n - 1 - i]
    return suma_diagonal_2

if __name__ == "__main__":
    cuadrado = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

    # Pruebas de verificación
    print("Prueba es_lista_enteros([1, 2, 3]):", es_lista_enteros([1, 2, 3]))
    print("Prueba es_lista_enteros(['a', 'b']):", es_lista_enteros(['a', 'b']))
    print()

    print("Prueba es_matriz_enteros(cuadrado):", es_matriz_enteros(cuadrado))
    print("Prueba es_matriz_enteros([[1, 'a'], [2, 3]]):", es_matriz_enteros([[1, 'a'], [2, 3]]))
    print()

    print("Prueba es_matriz_cuadrada(cuadrado):", es_matriz_cuadrada(cuadrado))
    print("Prueba es_matriz_cuadrada([[1, 2], [3, 4, 5]]):", es_matriz_cuadrada([[1, 2], [3, 4, 5]]))
    print()

    print("Prueba es_matriz_con_enteros_consecutivos(cuadrado):", es_matriz_con_enteros_consecutivos(cuadrado))
    cuadrado_invalido = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Prueba es_matriz_con_enteros_consecutivos(cuadrado_invalido):", es_matriz_con_enteros_consecutivos(cuadrado_invalido))
    print()

    print("Suma de filas:", sumar_filas(cuadrado))
    print("Suma de columnas:", sumar_columnas(cuadrado))
    print("Suma diagonal 1:", sumar_diagonal_1(cuadrado))
    print("Suma diagonal 2:", sumar_diagonal_2(cuadrado))
    print()

    print("¿Es cuadrado mágico?", cuadradoMagico(cuadrado))
