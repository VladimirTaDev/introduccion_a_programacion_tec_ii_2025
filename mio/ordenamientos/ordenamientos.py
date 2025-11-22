from random import randint
from time import time

def generar_lista(n):
    return [randint(0, 99999) for i in range (n)]

def medir_tiempo(funcion, n):
    L = generar_lista(n)
    inicio = time()
    L = funcion(L)
    final = time()
    delta = final - inicio
    print(f"Función: {funcion.__name__} n = {n}")
    print(f"Tiempo de ejecución: {delta} segundos")

def bubble_sort(L):
    """
    Algoritmo que implementa el ordenamiento de burbuja.
    Entradas y restricciones:
    - L: lista de elementos comparables.
    Salida:
    L ordenada ascendentemente.
    """
    if type(L) != list:
        raise Exception("L debe ser una lista.")
    iteracion = 1
    intercambios = True
    while intercambios and iteracion < len(L):
        intercambios = False
        for i in range(0, len(L) - iteracion):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                intercambios = True
        iteracion += 1
    return L

def selection_sort(L):
    def menor(L, inicio):
        pos_menor = inicio
        for j in range(inicio + 1, len(L)):
            if L[j] < L[pos_menor]:
                pos_menor = j
        return pos_menor

    if type(L) != list:
        raise Exception("L debe ser una lista.")
    for i in range(0, len(L) - 1):
        pos_menor = menor(L, i)
        L[i], L[pos_menor] = L[pos_menor], L[i]
    return L

def insertion_sort(L):
    if type(L) != list:
        raise Exception("L debe ser una lista.")
    for iteracion in range(1, len(L)):
        i = iteracion
        while i > 0 and L[i - 1] > L[i]:
            L[i], L[i - 1] = L[i - 1], L[i]
            i -= 1
    return L

def generar_casi_ordenada(n, porcentaje):
    L = list(range(n))
    intercambios = int(n * porcentaje)
    for i in range(intercambios):
        r1 = randrange(0, n)
        r2 = randrange(0, n)
        L[r1], L[r2] = L[r2], L[r1]
    return L

def medir_tiempo_casi_ordenado(funcion, n):
    L = generar_casi_ordenada(n, 0.20)
    inicio = time()
    L = funcion(L)
    final = time()
    delta = final - inicio
    print(f"Función: {funcion.__name__}, n={n}")
    print(f"Tiempo de ejecución: {delta} s")

def medir_tiempo(funcion, n):
    L = generar_lista(n)
    inicio = time()
    L = funcion(L)
    final = time()
    delta = final - inicio
    print(f"Función: {funcion.__name__}, n={n}")
    print(f"Tiempo de ejecución: {delta} s")

    def merge_sort_descriptivo(L):
        def merge_sort_aux(L):
            if len(L) == 1:
                return L
            else:
                izq = L[:len(L) // 2]
                der = L[len(L) // 2:]
                izq = merge_sort_aux(izq)
                der = merge_sort_aux(der)
                resultado = merge(izq, der)
                return resultado

def merge_sort(L):
    def merge(izq, der):
        resultado = []
        while izq != [] and der != []:
            if izq[0] <= der[0]:
                resultado.append(izq.pop(0))
            else:
                resultado.append(der.pop(0))
        resultado.extend(izq + der)
        return resultado

    def merge_sort_aux(L):
        if len(L) == 1:
            return L
        else:
            izq = merge_sort_aux(L[:len(L) // 2])
            der = merge_sort_aux(L[len(L) // 2:])
            return merge(izq, der)

    if type(L) != list:
        raise Exception("L debe ser una lista.")
    return merge_sort_aux(L)

def quick_sort(L):
    def quick_sort_aux(L):
        if len(L) <= 1:
            return L
        else:
            pivote = L.pop(len(L) // 2)
            menores = [x for x in L if x < pivote]
            mayores = [x for x in L if x >= pivote]
            return quick_sort_aux(menores) + [pivote] + quick_sort_aux(mayores)

    if type(L) != list:
        raise Exception("L debe ser una lista.")
    return quick_sort_aux(L)