from copy import deepcopy
from random import choice
import json

def esMatrizSudoku(M):
    if isinstance(M, list) and len(M) == 9:
        for fila in M:
            if isinstance(fila, list) and len(fila) == 9:
                for numero in fila:
                    if not isinstance(numero, int) or numero < 1 or numero > 9:
                        return False
            else:
                return False
        return True
    else:
        return False

def imprimirSudoku(M):
    if not esMatrizSudoku(M):
        raise Exception("No es una matriz sudoku válida.")
    resultado = "┌─────┬─────┬─────┐\n"
    for f in range(9):
        resultado += "│"
        for c in range(9):
            resultado += str(M[f][c])
            if (c + 1) % 3 == 0:
                resultado += "│"
            else:
                resultado += " "
        resultado += "\n"
        if (f + 1) % 3 == 0 and f < 8:
            resultado += "├─────┼─────┼─────┤\n"

    resultado += "└─────┴─────┴─────┘"
    print(resultado)

def es_sudoku_valido():
    nombre_de_archivo = "valido1.txt"

    with open (nombre_de_archivo, "r") as archivo:
        sudoku = json.load(archivo)
        imprimirSudoku(sudoku)



if __name__ == "__main__":
    es_sudoku_valido()




