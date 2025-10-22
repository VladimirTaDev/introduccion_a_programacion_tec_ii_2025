def main():
    """
    * Programa que cuenta la cantidad de dígitos en un número.
    * Entradas y restricciones:
        - n: entero positivo.
    * Salida:
        - Cantidad de dígitos: entero.
    """

    try:
        n = int(input("Escriba el valor de n: "))
        if n <= 0:
            raise ValueError("El número debe ser entero positivo")
    except ValueError as e:
        print(f"ERROR: {e}")
    else:
        contador = 1
        while n > 9:
            n = n/9
            contador += 1
        else:
            print(f"la cantidad de dígitos es: {contador}")

if __name__ == "__main__":
    main()
