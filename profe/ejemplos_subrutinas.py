def area_rectangulo(base, altura):
    '''
    Función que calcula el area de un rectángulo.
    Entradas y restricciones:
    - base: número (int, float) positivo.
    - altura: número (int, float) positivo.
    Salidas:
    Área del rectángulo (int, float)
    '''
    if type(base) not in (int, float) or base <= 0:
        raise Exception("base debe ser un número positivo.")
    if type(altura) not in (int, float) or altura <= 0:
        raise Exception("altura debe ser un número positivo.")
    area = base * altura
    return area

def factorial(n):
    """
    Función que calcula el factorial de un número.
    Entradas y restricciones:
    - n: entero no negativo.
    Salidas:
    El factorial de n (entero).
    """
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def area_triangulo(base, altura):
    """
    Función que calcula el area de un triángulo
    a partir de la base y la altura.
    Entradas y restricciones:
    - base: real o entero positivo.
    - altura: real o entero positivo.
    Salidas:
    Área del triángulo (real).
    """
    if type(base) not in (float, int) or base <= 0:
        raise Exception("base debe ser número positivo.")
    if type(altura) not in (float, int) or altura <= 0:
        raise Exception("altura debe ser un número positivo.")
    return base * altura / 2

def perimetro_triangulo_rectangulo(base, altura):
    """
    Función que calcula el perímetro de un triángulo
    rectángulo a partir de la base y la altura.
    Entradas y restricciones:
    - base: real o entero positivo.
    - altura: real o entero positivo.
    Salidas:
    Área de un triángulo (real).
    """
    if type(base) not in (float, int) or base <= 0:
        raise Exception("base debe ser un número positivo.")
    if type(altura) not in (float, int) or altura <= 0:
        raise Exception("altura debe ser un número positivo.")
    hipotenusa = math.sqrt(base**2 + altura**2)
    return base + altura + hipotenusa

def mayor_de_tres(a, b, c):
    """
    Función que calcula el mayor de tres números.
    Entradas y restricciones:
    - a, b, c: enteros o reales.
    Salidas:
    El mayor entre a, b y c.
    """
    if type(a) not in (float, int):
        raise Exception("a debe ser un número.")
    if type(b) not in (float, int):
        raise Exception("b debe ser un número.")
    if type(c) not in (float, int):
        raise Exception("c debe ser un número.")
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

def contar_digitos(n):
    """
    Función que calcula la cantida de dígitos de
    un número entero.
    Entradas y restricciones:
    - n: entero no negativo.
    Salidas:
    La cantidad de dígitos de n (entero).
    """
    if type(n) != int or n < 0:
        raise Exception("n debe ser entero no negativo.")
    cantidad = 1
    while n > 9:
        n //= 10
        cantidad += 1
    return cantidad
