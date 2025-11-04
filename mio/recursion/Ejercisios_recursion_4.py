def es_lista_enteros_positivos(L):
    if type(L) != list:
        return False
    if L == []:
        return True
    if type(L[0]) != int or L[0] < 1:
        return False
    else:
        return es_lista_enteros_positivos(L[1:])

def todos_divisores_pila(n, L):
    """
    Función recursiva que dice si n es divisible
    entre todos los números de L.
    Entradas y restricciones:
    - n: entero.
    - L: lista de enteros positivos.
    Salidas:
    Verdadero si n es divisible entre todos los
    elementos de L. Falso si no.
    """
    def aux_pila(n, L):
        print(f"aux_pila({n}, {L})")
        if L == []:
            return True
        else:
            return n % L[0] == 0 and aux_pila(n, L[1:])

    # Se divide por la mitad
    def aux_pila2(n, L):
        if L == []:
            return True
        if len(L) == 1:
            return n % L[0] == 0
        else:
            mitad = len(L) // 2
            return aux_pila2(n, L[:mitad]) and aux_pila2(n, L[mitad:])

    def aux_cola(n, L):
        print(f"aux_cola({n}, {L})")
        if L == []:
            return True
        if n % L[0] != 0:
            return False
        else:
            return aux_cola(n, L[1:])

    if type(n) != int:
        raise Exception("n debe ser un entero.")
    if type(L) != list:
        raise Exception("L debe ser una lista de enteros positivos.")
    return aux_pila(n, L)

def doble_fact(n):
    def aux_pila(n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        else:
            return n * aux_pila(n - 2)

    def aux_iter(n):
        resultado = 1
        while n > 0:
            resultado *= n
            n -= 2
        return resultado

    def aux_cola(n, resultado):
        if n <= 0:
            return resultado
        else:
            return aux_cola(n - 2, resultado * n)

    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    return aux_cola(n, 1)

def es_lista_ordenada(L):
    def aux_pila(L):
        if len(L) <= 1:
            return True
        else:
            mitad = len(L) // 2
            return (
                aux_pila(L[:mitad])
                and aux_pila(L[mitad:])
                and L[mitad - 1] <= L[mitad]
            )

    if type(L) != list:
        raise Exception("L debe ser una lista")
    return aux_pila(L)