import math

def areaCirculo(radio):
    """
    Función que calcula el área de un círculo.
    Entradas y restricciones:
    - radio: real positivo.
    Salidas:
    Área del círculo (real).
    """
    if type(radio) != float or radio <= 0:
        raise Exception("El radio debe ser un real positivo.")
    area = math.pi * radio**2
    return area

def main():
    """
    Programa que calcula el área de un círculo.
    """
    try:
        radio = float(input("Escriba el radio del círculo: "))
        print("El área es: " + str(areaCirculo(radio)))
    except Exception as e:
        print("ERROR: ocurrió un error. " + str(e))

if __name__ == "__main__":
    main()
