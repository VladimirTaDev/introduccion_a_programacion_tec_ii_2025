def sumar_digitos(n):
    """
    Programa que suma todos los dígitos de un entero.
    Entradas y restricciones:
    - n: (int) no negativo.
    Salida:
    - suma de todos los dígitos: (int)
    """

    def aux_pila(d):
        if d < 10:
            return d
        return aux_pila(d // 10) + d % 10

    def aux_cola(d, c):
        if d <= 0:
            return c
        return aux_cola(d // 10, c + d % 10)

    return aux_cola(n, 0)
    if isinstance(n, int) and n > 0:
        raise Exception("n debe ser un entero no negativo")

if __name__ == "__main__":
    print(sumar_digitos(2123))
