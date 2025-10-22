def main():
    """
    * Programa que calcula el área de un triángulo.
    * Entradas y restricciones:
        - base, altura: real > 0
    * Salidas:
        - area: real > 0
    """

    # Recive entradas.    
    base = float(input("Introduzca la base: "))    
    altura = float(input("Introduzca la altura: "))
    # Revisa restricciones:
    try:
        if (not isinstance(base, (int, float)) or base <= 0) or (not isinstance(altura, (int, float)) or altura <= 0):
            raise Exception("Base y altura deben ser reales positivos.")
        area = (base * altura) / 2
        print("El área del triángulo es: " + str(area))
    except Exception as e:
        print("ERROR: " + str(e))
        Exception

if __name__ == "__main__":
    main()
