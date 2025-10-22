import math

def calcularPi():
    """
    Función que aproxima el valor de pi.
    Entradas y restricciones: no tiene.
    Salidas: aproximación de pi (float).
    """
    resultado = 0
    k = 0
    while k <= 30:
        resultado += 2 * (-1)**k * 3**(0.5 - k) / (2 * k + 1)
        k += 1
    return resultado

def main():
    """
    Programa que calcula y muestra una aproximacón de pi.
    Entradas y restricciones:
    - No tiene.
    Salidas:
    Aproximación de pi (real)
    """
    print(f"Aproximación calculada: {calcularPi()}")
    print(f"Constante de uhhh Python: {math.pi}")

if __name__ == "__main__":
    main()
