import math

def perimetro(base, altura):
    """
    Función que calcula el perímetro de un triángulo rectángulo.
    Entradas y restricciones:
    - base: real positivo.
    - altura: real positivo.
    Salidas:
    Perímetro del triángulo (real).
    """
    if type(base) not in (float, int) or base <= 0:
        raise Exception("base debe ser un real positivo.")
    if type(altura) not in (float, int) or altura <= 0:
        raise Exception("altura debe ser un real positivo.")
    hipotenusa = math.sqrt(base**2 + altura**2)
    perimetro = base + altura + hipotenusa
    return perimetro

def main():
    """
    Programa que calcula el perímetro de un triángulo rectángulo.
    """
    try:
        base = float(input("Escriba la base del triángulo: "))
        altura = float(input("Escriba la altura del triángulo: "))
        p = perimetro(base, altura)
        print("El perímetro es " + str(p))
    except Exception as e:
        print("ERROR: " + str(e))

if __name__ ==  "__main__":
    main()
    
