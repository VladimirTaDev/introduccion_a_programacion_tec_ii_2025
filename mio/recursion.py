def factorial_aux(n):
    """
    Función auxiliar de factorial(n)
    """
    if n == 0:
        return 1
    else:
        return factorial_aux(n - 1) * n

def factorial(n):
    """
    Función recursiva que calcula el factorial de un número

    Entradas y restricciones:
    - n: un entero no negativo.
    Salidas:
    Cáculo de n factorial.
    """
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    return factorial_aux(n)

def sumar_m_a_n_aux(m, n):
    if m == n:
        print(f"sumar_m_a_n_aux({m}, {n}) = {m}")
        return m
    else:
        print(f"sumar_m_a_n_aux({m}, {n}) = sumar_m_a_n_aux({m}, {n - 1}) + {n}")
        return sumar_m_a_n_aux(m, n - 1) + n

def sumar_m_a_n_aux2(m, n):
    if m == n:
        return m
    else:
        print(f"sumar({m}, {n}) = {m} + sumar({m + 1}, {n})")
        return m + sumar_m_a_n_aux2(m + 1, n)

def sumar_m_a_n_aux3(m, n):
    if m == n:
        return m
    else:
        mitad = (m + n) // 2
        print(f"sumar({m}, {n}) = sumar({m}, {mitad}) + sumar({mitad + 1}, {n})")
        return sumar_m_a_n_aux3(m, mitad) + sumar_m_a_n_aux3(mitad + 1, n)

def sumar_m_a_n(m, n):
    """
    Función recursiva que calcula la suma desde m
    hasta n.
    Entradas y restricciones:
    - m: entero.
    - n: entero igual o mayor a m.
    Salidas:
    Resultado de todos los enteros desde m hasta n.
    """
    if type(m) != int:
        raise Exception("m debe ser entero.")
    if type(n) != int or n < m:
        raise Exception("n debe ser entero igual o mayor a m.")
    return sumar_m_a_n_aux(m, n)

# Función principal
def factorial(n):
    # Función auxiliar anidada
    # Sólo la principal puede invocarla
    def factorialAux(n):
        if n == 0:
            return 1
        else:
            return n * factorialAux(n - 1)

    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    return factorialAux(n)

def fibonacci(n):
    def fibonacciAux(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacciAux(n - 1) + fibonacciAux(n - 2)

    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    return fibonacciAux(n)