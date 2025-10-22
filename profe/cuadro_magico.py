def es_matriz_enteros(M):
    if type(M) != list:
        return False
    for fila in M:
        if type(fila) != list:
            return False
        if len(fila) != len(M[0]):
            return False
        for e in fila:
            if type(e) != int:
                return False
    return True

def contiene_consecutivos(M):
    union = []
    for fila in M:
        union.extend(fila)
    union.sort()
    return union == list(range(1, len(M)**2 + 1))

def suma_fila(M, fila):
    suma = 0
    for c in range(len(M[fila])):
        suma += M[fila][c]
    return suma

def suma_columna(M, columna):
    suma = 0
    for f in range(len(M)):
        suma += M[f][columna]
    return suma

def suma_diagonal_1(M):
    suma = 0
    for i in range(len(M)):
        suma += M[i][i]
    return suma

def suma_diagonal_2(M):
    suma = 0
    for i in range(len(M)):
        suma += M[i][len(M) - 1 - i]
    return suma

def cuadrado_magico(M):
    """
    Función que valida si una matriz es un cuadro mágico.
    Entradas y restricciones:
    - M: matriz cuadrada de enteros.
    Salidas:
    True si corresponde a un cuadro mágico.
    False si no.
    """
    if not es_matriz_enteros(M) or len(M) != len(M[0]):
        raise Exception("M debe ser una matriz cuadrada de enteros.")
    if not contiene_consecutivos(M):
        return False
    diagonal = suma_diagonal_1(M)
    if diagonal != suma_diagonal_2(M):
        return False
    for i in range(len(M)):
        if diagonal != suma_fila(M, i):
            return False
        if diagonal != suma_columna(M, i):
            return False
    return True
    
