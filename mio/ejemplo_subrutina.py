def area_rectangulo(base, altura):
    """
    Función que calcula el area de un rectángulo.
    Entradas y restricciones:
    - base: número (int, float) positivo.
    - altura: número (int, float) positivo.
    Salida:
    - Área del triángulo (int, float)
    """
    #if type(base) != int and type(base) != float or base <= 0:
    if type(base) not in (int, float) or base <= 0:
        raise Exception("base debe ser un número positivo.")
    if type(altura) not in (int, float) or altura <= 0:
        raise Exception("altura debe ser un número positivo.")    
    area = base * altura
    return area
