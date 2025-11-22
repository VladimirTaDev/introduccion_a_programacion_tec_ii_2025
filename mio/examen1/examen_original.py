from math import *

def hosoya(filas, columnas):
    triangulo = [[1, 1], [1, 1]]

    anterior = 1
    actual = 1

    # Calcula primeras dos filas y columnas en ellas.
    for columna in range(columnas - 2):
            triangulo[0].append(triangulo[0][columna] + triangulo[0][columna + 1])
            triangulo[1].append(triangulo[1][columna] + triangulo[1][columna + 1])
    
    for fila in range(filas - 2):
        fila_nueva = []
        for columna in range(columnas):
            fila_nueva.append(triangulo[fila][columna] + triangulo[fila + 1][columna])
        triangulo.append(fila_nueva.copy())
        fila_nueva.clear()

    return triangulo


def feliz(n):
    suma = 0
    n_nueva = n
    n_elevada = []

    while suma != 1:
        n_elevada.clear
        suma = 0
        for num in str(n_nueva):
            n_elevada.append(int(num) * int(num))
            #print(n_elevada)
            for num2 in n_elevada:
                suma += num2
        n_nueva = suma
        ##print(n_nueva)

    return True


if __name__ == "__main__":
    print(feliz(7))
    #print(hosoya(5, 7))