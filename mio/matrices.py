from random import randint
from tabulate import tabulate

def crear_matriz_nula(filas, columnas):
    """
    Función que crea una matriz con ceros.
    Entradas y restyricciones:
    - filas: entero positivo.
    - columnas: entero positivo.
    Salidas:
    Matriz de las dimensiones indicadas
    con ceros en cada posición.
    """
    if type(filas) != int or filas < 1:
        raise Exception("Fila debe ser un entero positivo.")
    if type(columnas) != int or columnas < 1:
        raise Exception("columna debe ser entero positivo")
    M = []
    for f in range(filas):
        fila = []
        for c in range(columnas):
            fila.append(0)
        M.append(fila)
    return M

def crear_matriz_aleatoria(filas, columnas, minimo, maximo):
    if type(filas) != int or filas < 1:
        raise Exception("filas debe ser entero positivo.")
    if type(columnas) != int or columnas < 1:
        raise Exception("columnas debe ser entero positivo.")
    if type(minimo) != int:
        raise Exception("minimo debe ser un entero.")
    if type(maximo) != int or maximo < minimo:
        raise Exception("maximo debe ser un entero mayor o igual a minimo.")
    M = []
    for f in range(filas):
        fila = []
        for c in range(columnas):
            fila.append(randint(minimo, maximo))
        M.append(fila)
    return M

def es_matriz_numerica(M):
    if type(M) != list:
        return False
    for fila in M:
        if type(fila) != list:
            return False
        if len(fila) != len(M[0]):
            return False
        for elemento in fila:
            if type(elemento) not in (int, float):
                return False
    return True

def imprimir(M):
    if not es_matriz_numerica(M):
        raise Exception("M debe ser una matriz numérica.")
    print(tabulate(M, tablefmt="simple_grid"))

def columnas(M):
    if not es_matriz_numerica(M):
        raise Exception("M debe ser una matriz numérica.")
    return len(M[0])

def filas(M):
    if not es_matriz_numerica(M):
        raise Exception("M debe ser una matriz numérica.")
    return len(M)

def suma(A, B):
    if not es_matriz_numerica(A):
        raise Exception("A debe ser una matriz válida.")
    if not es_matriz_numerica(B):
        raise Exception("B debe ser una matriz válida.")
    if filas(A) != filas(B) or columnas(A) != columnas(B):
        raise Exception("las matrices deben tener las mismas dimensiones.")
    C = crear_matriz_nula(filas(A), columnas(B))
    for f in range(filas(A)):
        for c in range(columnas(A)):
            C[f][c] = A[f][c] + B[f][c]
    return C
            
## resta
def resta(A, B):
    return suma(A, mult_escalar(-1, B))

## multiplicaciuón por escalar
def mult_escalar(e, M):
    if type(e) not in (float, int):
        raise Exception("e debe ser un número")
    if not es_matriz_numerica(M):
        raise Exception ("M debe ser una matriz vaáida")
    A = crear_nula(fila(M), columnas(M))
    for f in range(filas(M)):
        for c in range(columnas(M)):
            A[f][c] = e * M[f][c]
    return A

## división por escalar
def div_escalar(e, M):
    return mult_escalar(1/e, M)

## transpuesta de una matriz
def transpuesta(M):
    if not es_matriz_numerica(M):
        raise Exception("M debe ser una matriz válida.")
    T = crear_nula (columnas(M), filas(M))
    for f in range(filas(M)):
        for c in range(columnas(M)):
            T[c][f] = M[f][c]
    return T

## multiplicación de matrices
def mult_matrices(A, B):
    if not es_matriz_numerica(A):
        raise Exception("A debe ser una matriz válida.")
    if not es_matriz_numerica(B):
        raise Exception("B debe ser una matriz válida.")
    if columnas(A) != filas(B):
        raise Exception("La cantidad de columnas de A debe ser igual a la cantidad de filas de B.")
    C = crear_nula(filas(A), columnas(B))
    for f in range(filas(A)):
        for c in range(columnas(B)):
            suma = 0
            for e in range(columnas(A)):
                suma += A[f][e] * B[e][c]
            c[f][c] = suma
    return C
