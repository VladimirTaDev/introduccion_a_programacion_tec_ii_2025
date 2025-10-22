from math import sqrt, pi
import math

def es_primo(n):
    """
    Función booleana que dice si n es primo.
    Entradas y restricciones:
    - n: entero mayor o igual a dos.
    Salidas:
    True si es primo, False si no (booleano).
    """
    if type(n) != int or n < 2:
        raise Exception("n debe ser entero mayor o igual a dos")
    m = 2
    primo = True
    while m <= sqrt(n) and primo:
        if n % m == 0:
            primo = False
        m = m + 1
    return primo

def main():
    """
    Programa que dice si un número es primo o no
    """
    try:
        n = int(input("Escriba un número entero: "))
        if es_primo(n):
            print(f"{n} es número primo.")
        else:
            print(f"{n} no es número primo.")
    except Exception as e:
        print(f"ERROR: {e}")
                 
if __name__ == "__main__":
    main()
