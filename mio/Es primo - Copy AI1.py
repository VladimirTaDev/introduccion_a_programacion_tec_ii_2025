import math

def esPrimo(n):
    """
    Calcula si n es primo
    """
    primo = True
    m = 2
    while m <= math.sqrt(n) and primo:
        if n % m == 0:
            primo = False
        m = m + 1
    return primo

def main():
    """
    Algoritmo que dice si un número es primo.
    Entradas y restricciones:
    - n: entero mayor o igual a 2.
    Salidas:
    Si es primo o no (mensaje)
    """

    n = int(input("Escriba el valor de m: "))
    if n < 2:
        print("ERROR: el número debe ser mayor o igual a 2.")
    else:
        if esPrimo(n):
            print("Es primo")
        else:
            print("No es primo")

if __name__ == "__main__":
    main()
        
