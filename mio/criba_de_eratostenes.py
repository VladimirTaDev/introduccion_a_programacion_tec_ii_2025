import math

def criba(M):
    if type(M) != int or M < 2:
        raise ValueError("El valor debe ser un entero mayor o igual a 2")
    L = list(range(2, M + 1))
    primos = []
    while L[0] <= math.sqrt(M):
        actual = L.pop(0)
        L = [x for x in L if x % actual != 0]
        primos.append(actual)
    primos.extend(L)
    return primos


"""
def maina(m):
    primos = range(2, m + 1)
    criba_primer_Paso(primos)


    while raiz
    m = range(2, m + 1)

def criba_primer_Paso(m): ## paso 1-3
    rango = [2]
    for numero in range(2, m + 1):
        if numero % 2 != 0:
            rango.append(numero)

    return rango

def criba_segundo_paso(m): ## paso 2-3
    rango = []
    for numero in m:
        if numero % 2 != 0:
            rango.append(numero)

    return rango

def raiz(m): ## paso 4
    if 30 <= math.sqrt(m[0]):
        return criba_segundo_paso(m)
    ## todos los que quedan son primos
    return True


if __name__ == "__main__":
    print(raiz(range(2, 30 + 1)))
    ## print(criba(range(2, 30 + 1)))
"""