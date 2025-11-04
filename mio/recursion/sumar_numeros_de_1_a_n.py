def sumar_1_a_n(n):
    """ Programa que calcula números de 1 a n recursivamente
    Entradas y restricciones:
    - n (int): entero no positivo.
    Salida
    - Resultado de sumar de 1 a n.
    """

    # Recursión de Pila (Stack Recursion)
    def aux_pila(n):
        if n == 1:
            return 1
        return aux_pila(n - 1) + n

    # Recursión de Cola (Tail Recursion)
    def aux_cola(a, n):
        if n == 0:
            return a
        return aux_cola(a + n, n - 1)

    # Restricciones.
    if type(n) != int or n < 1:
        raise Exception("n debe ser entero positivo.")
    return aux_cola(0, n) # Se usa la versión de cola que es más óptima



#########################


# Recursión con "Divide y Vencerás"
def sumar_rango_dividiendo(inicio, fin):
    # Caso base: si el rango es un solo número, ese es el resultado.
    if inicio == fin:
        return inicio

    # 1. Dividir: Encontrar el punto medio del rango
    medio = (inicio + fin) // 2

    # 2. Vencer: Llamar recursivamente a cada mitad
    suma_izquierda = sumar_rango_dividiendo(inicio, medio)
    suma_derecha = sumar_rango_dividiendo(medio + 1, fin)

    # 3. Combinar: Sumar los resultados de ambas mitades
    return suma_izquierda + suma_derecha


# Para usarla, la llamarías así desde tu función principal:
# return sumar_rango_dividiendo(1, n)
#########################


if __name__ == '__main__':
    print(sumar_1_a_n(4))
