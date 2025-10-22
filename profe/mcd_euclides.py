def mcd(m, n):
    """
    Función que calcula el máximo común divisor según el algoritmo
    de Euclides.
    Entradas y restricciones:
    - m: entero positivo.
    - n: entero positivo.
    Salidas:
    El MCD (entero)
    """
    if type(m) != int or m <= 0:
        raise Exception("m debe ser entero positivo.")
    if type(n) != int or n <= 0:
        raise Exception("n debe ser entero positivo.")
    r = m % n
    while r != 0:
        m = n
        n = r
        r = m % n
    return n

def main():
    """
    Programa que calcula el máximo común divisor.
    """
    try:
        m = int(input("Escriba el valor de m: "))
        n = int(input("Escriba el valor de n: "))
        print("El máximo común divisor es " + str(mcd(m, n)))
    except Exception as e:
        print("ERROR: " + str(e))

if __name__ == "__main__":
    main()

    
