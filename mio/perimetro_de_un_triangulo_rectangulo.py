import math

def main():
    """
    * Programa que calcula el perímetro de un triángulo rectángulo.
    * Entradas y restricciones:
        - base, altura: real positivo.
    * Salida:
        - área: real positivo.
    """
    
    try:
        # Recive entradas.
        base = float(input("Introduzca la base: "))
        altura = int(input("Introduzca la altura: "))

        # Calcula y retorna el resultado.
        perimetro = math.sqrt((base**2 + altura**2)) + base + altura
        print("El perímetro del triángulo es: " + str(perimetro))

    except Exception as e:
        print("ERROR: " + str(e))
    
if __name__ == "__main__":
    main()
