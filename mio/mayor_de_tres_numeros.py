def main():
    """
    Programa que calcula el mayor de 3 números.
    * Entradas y restricciones:
        - a, b, c: enteros positivos.
    * Salida:
        - número mayor.
    """
    try:
        # Recive entradas.
        a = int(input("Introduzca en número a: "))
        b = int(input("Introduzca en número b: "))
        c = int(input("Introduzca en número c: "))
        
        # Chequea restricción positiva.
        if a < 0 or b < 0 or c < 0:
            raise Exception("El número debe ser positivo")
    except Exception as e:
        print(f"ERROR: {e}")

    else:
        if a > b and a > c:
            print(f"El número mayor es: {a}")
        elif b > a and b > c:
            print(f"El número mayor es: {b}")
        else:
            print(f"El número mayor es: {c}")


if __name__ == "__main__":
    main()
