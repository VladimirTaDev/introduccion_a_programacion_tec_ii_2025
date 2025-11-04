# Ejercicios resueltos con pila y cola.

def sumar_1_a_n_iteracion(n):
    if type(n) != int or n < 1:
        raise Exception("n debe ser entero positivo.")
    suma = 0
    i = 1
    while i <= n:
        suma += i
        i += 1
    return suma

def sumar_1_a_n_pila(n):
    def sumar_aux(n):
        if n == 1:
            return 1
        else:
            return sumar_aux(n - 1) + n

    if type(n) != int or n < 1:
        raise Exception("n debe ser entero positivo.")
    return sumar_aux(n)

def sumar_1_a_n_cola(n):
    def sumar_aux(n, suma, i):
        if i > n:
            return suma
        else:
            return sumar_aux(n, suma + i, i + 1)

    if type(n) != int or n < 1:
        raise Exception("n debe ser entero positivo.")
    return sumar_aux(n, 0, 1)