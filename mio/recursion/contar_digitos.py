"""
Recursión.
Programa que cuenta la cantidad de dígitos.
Entradas y restricciones:
- n: (int) no negativo.
Salida: La cantidad de números en n: (int)
"""

def contar_digitos(n):

    def aux_cola(d, i):
        if d == 0:
            return i
        i += 1
        d = d // 10
        return aux_cola(d, i)

    def aux_pila(d):
        # caso base
        if d < 10:
            return 1
        # caso general
        return aux_pila(d // 10) + 1


    if not isinstance(n, int) or n < 0:
        raise ValueError("El número debe ser un entero no negativo.")

    return aux_pila(n)


if __name__ == '__main__':
    print(contar_digitos(123))
