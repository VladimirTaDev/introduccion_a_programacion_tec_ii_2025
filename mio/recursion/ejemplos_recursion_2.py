fibonacci_memo = {}

def fibonacci_normal(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_normal(n - 1) + fibonacci_normal(n - 2)

def fibonacci_aux(n):
    if n in fibonacci_memo:
        return fibonacci_memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        fibonacci_memo[n] = fibonacci_aux(n - 1) + fibonacci_aux(n - 2)
        return fibonacci_memo[n]

def fibonacci(n):
    """
    Función recursiva que calcula el elemento que
    se encuentra en la posición n de la secuencia
    de Fibonacci.
    Entradas y restricciones:
    - n: entero no negativo.
    Salidas:
    Entero con el elemento.
    """
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    return fibonacci_aux(n)

factorial_memo = {}

def factorial_aux(n):
    if n in factorial_memo:
        return factorial_memo[n]
    if n == 0:
        return 1
    else:
        factorial_memo[n] = n * factorial_aux(n - 1)
        return factorial_memo[n]

def factorial(n):
    """
    Función recursiva que calcula el factorial de un número
    Entradas y restricciones:
    - n: un entero no negativo.
    Salidas:
    Cálculo de n factorial.
    """
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    return factorial_aux(n)

sumar_m_a_n_memo = {}

def sumar_m_a_n_aux(m, n):
    if (m, n) in sumar_m_a_n_memo:
        return sumar_m_a_n_memo[(m, n)]
    if m == n:
        return m
    else:
        mitad = (m + n) // 2
        sumar_m_a_n_memo[(m, n)] = sumar_m_a_n_aux(m, mitad) + sumar_m_a_n_aux(mitad + 1, n)
        return sumar_m_a_n_memo[(m, n)]

def sumar_m_a_n(m, n):
    """
    Función recursiva que calcula la suma desde m hasta n.
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

if __name__ == '__main__':
    print(fibonacci_normal(50))