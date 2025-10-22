"""
OPERACIONES CON MATRICES
========================

Este archivo contiene explicaciones breves y ejemplos simples de
las operaciones básicas con matrices.
"""

# ===== SUMA DE MATRICES =====
"""
SUMA: Se suman las matrices elemento por elemento.
Las matrices deben tener las mismas dimensiones.

Ejemplo:
A = [[1, 2],     B = [[5, 6],     A + B = [[6, 8],
     [3, 4]]          [7, 8]]              [10, 12]]
"""

def suma_matrices(A, B):
    """
    Suma dos matrices elemento por elemento.
    Entradas y restricciones:
    - A: list de listas, matriz de números.
    - B: list de listas, matriz de números con las mismas dimensiones que A.
    Salidas:
    - list de listas, matriz resultado de sumar A y B.
    """
    if type(A) != list or type(B) != list:
        raise Exception("A y B deben ser listas.")
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise Exception("Las matrices deben tener las mismas dimensiones.")

    filas = len(A)
    columnas = len(A[0])
    resultado = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(A[i][j] + B[i][j])
        resultado.append(fila)

    return resultado


# ===== RESTA DE MATRICES =====
"""
RESTA: Se restan las matrices elemento por elemento.
Las matrices deben tener las mismas dimensiones.

Ejemplo:
A = [[5, 6],     B = [[1, 2],     A - B = [[4, 4],
     [7, 8]]          [3, 4]]              [4, 4]]
"""

def resta_matrices(A, B):
    """
    Resta dos matrices elemento por elemento.
    Entradas y restricciones:
    - A: list de listas, matriz de números.
    - B: list de listas, matriz de números con las mismas dimensiones que A.
    Salidas:
    - list de listas, matriz resultado de restar B de A.
    """
    if type(A) != list or type(B) != list:
        raise Exception("A y B deben ser listas.")
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise Exception("Las matrices deben tener las mismas dimensiones.")

    filas = len(A)
    columnas = len(A[0])
    resultado = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(A[i][j] - B[i][j])
        resultado.append(fila)

    return resultado


# ===== TRANSPUESTA =====
"""
TRANSPUESTA: Se intercambian filas por columnas.
Una matriz de m×n se convierte en una de n×m.

Ejemplo:
A = [[1, 2, 3],     A^T = [[1, 4],
     [4, 5, 6]]            [2, 5],
                            [3, 6]]
"""

def transpuesta(A):
    """
    Calcula la transpuesta de una matriz.
    Entradas y restricciones:
    - A: list de listas, matriz de números.
    Salidas:
    - list de listas, matriz transpuesta de A.
    """
    if type(A) != list:
        raise Exception("A debe ser una lista.")

    filas = len(A)
    columnas = len(A[0])
    resultado = []

    for j in range(columnas):
        fila = []
        for i in range(filas):
            fila.append(A[i][j])
        resultado.append(fila)

    return resultado


# ===== MULTIPLICACIÓN POR ESCALAR =====
"""
MULTIPLICACIÓN POR ESCALAR: Se multiplica cada elemento de la matriz por un número.

Ejemplo:
k = 3
A = [[1, 2],     k * A = [[3, 6],
     [3, 4]]              [9, 12]]
"""

def multiplicacion_escalar(k, A):
    """
    Multiplica una matriz por un escalar.
    Entradas y restricciones:
    - k: int o float, escalar.
    - A: list de listas, matriz de números.
    Salidas:
    - list de listas, matriz resultado de multiplicar A por k.
    """
    if type(k) not in [int, float]:
        raise Exception("k debe ser un número.")
    if type(A) != list:
        raise Exception("A debe ser una lista.")

    filas = len(A)
    columnas = len(A[0])
    resultado = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(k * A[i][j])
        resultado.append(fila)

    return resultado


# ===== MULTIPLICACIÓN DE MATRICES =====
"""
MULTIPLICACIÓN: Se multiplican las matrices según la regla del producto matricial.
El número de columnas de A debe ser igual al número de filas de B.
Resultado: matriz de dimensiones (filas de A) × (columnas de B).

Ejemplo:
A = [[1, 2],     B = [[5, 6],     A * B = [[19, 22],
     [3, 4]]          [7, 8]]              [43, 50]]

Cálculo: 
A*B[0][0] = 1*5 + 2*7 = 19
A*B[0][1] = 1*6 + 2*8 = 22
A*B[1][0] = 3*5 + 4*7 = 43
A*B[1][1] = 3*6 + 4*8 = 50
"""

def multiplicacion_matrices(A, B):
    """
    Multiplica dos matrices según el producto matricial.
    Entradas y restricciones:
    - A: list de listas, matriz de números.
    - B: list de listas, matriz de números donde columnas de A = filas de B.
    Salidas:
    - list de listas, matriz resultado de multiplicar A por B.
    """
    if type(A) != list or type(B) != list:
        raise Exception("A y B deben ser listas.")
    if len(A[0]) != len(B):
        raise Exception("El número de columnas de A debe ser igual al número de filas de B.")

    filas_A = len(A)
    columnas_A = len(A[0])
    columnas_B = len(B[0])
    resultado = []

    for i in range(filas_A):
        fila = []
        for j in range(columnas_B):
            suma = 0
            for k in range(columnas_A):
                suma = suma + A[i][k] * B[k][j]
            fila.append(suma)
        resultado.append(fila)

    return resultado


# ===== DIVISIÓN DE MATRICES =====
"""
DIVISIÓN: No existe la división directa de matrices.
En su lugar, se multiplica A por la inversa de B: A * B^(-1)

NOTA: Calcular la inversa de una matriz es complejo y requiere
métodos avanzados (determinante, matriz adjunta, etc.).
Para este curso introductorio, se recomienda usar bibliotecas
como NumPy para calcular inversas.

Ejemplo conceptual:
A / B = A * B^(-1)

Para implementarlo, necesitarías primero calcular B^(-1) y luego
hacer la multiplicación de matrices.
"""

def division_matrices(A, B):
    """
    Nota: Esta función es solo conceptual.
    La división de matrices requiere calcular la inversa de B,
    lo cual es un tema avanzado que no se cubre en este curso.
    """
    raise Exception("La división de matrices requiere calcular la inversa, un tema avanzado.")


# ===== EJEMPLOS DE USO =====
if __name__ == "__main__":
    # Ejemplos
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    k = 3

    print("Matriz A:")
    print(A)
    print("\nMatriz B:")
    print(B)

    print("\nSuma A + B:")
    print(suma_matrices(A, B))

    print("\nResta A - B:")
    print(resta_matrices(A, B))

    print("\nTranspuesta de A:")
    print(transpuesta(A))

    print("\nMultiplicación por escalar (3 * A):")
    print(multiplicacion_escalar(k, A))

    print("\nMultiplicación A * B:")

