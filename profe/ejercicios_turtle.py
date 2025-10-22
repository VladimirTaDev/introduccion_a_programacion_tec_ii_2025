from turtle import *

def cuadrado(lado):
    for i in range(4):
        forward(lado)
        right(90)

def triangulo(lado):
    for i in range(3):
        forward(lado)
        right(120)

def poligono(n, lado):
    """
    Subrutina que dibuja un polígono regular.
    Entradas y restricciones:
    - n: cantidad de lados. Entero mayor a 2.
    - lado: longitud. Entero o real.
    Salida:
    Dibujo del polígono con turtle.
    """
    angulo = 360 / n
    for i in range(n):
        forward(lado)        
        right(angulo)

def escalera(n, lado):
    for i in range(n):
        forward(lado)
        right(90)
        forward(lado)
        left(90)

def sombrilla(lado):
    for i in range(6):
        poligono(3, lado)
        right(60)

def estrella(lado):
    for i in range(5):
        forward(lado)
        right(144)

def tunel_ignacio(n, lado):
    tracer(0, 0)
    colormode(255)
    r = 0
    b = 255
    actual = 3
    while actual <= n:
        color(r, 0, b)
        r = (r + 2) % 256
        b = (b - 1) % 256
        poligono(actual, lado)
        actual += 1
    update()





def draw_square(side):
    """
    Function draws a square of 'side' side length for each side

    Inputs and restrictions:
    - 'side' numerical value for side length (int or float)

    Outputs:
    - A graphical representation of a square
    """
    if type(side) != float and type(side) != int:
        raise Exception("Error: 'side' value is not numeric")
    
    for i in range(4):
        forward(side)
        right(90)

## =====================================================================
## \\ Trabajo en clase 9/25/2025 -- función cuadrado_relleno(n, lado) //
## =====================================================================

def draw_square_series(amount, separation):
    """
    Function draws a series of expanding 'amount' squares separated by 'separation' units

    Inputs and restrictions:
    - 'amount' integer (int, because how would you have "5.2" copies???)
    - 'separation' numerical value (int or float)

    Outputs:
    - A graphical representation of the series of repeating squares
    """

    if type(amount) != int:
        raise Exception("Error: 'steps' value is not an integer")
    if type(separation) != float and type(separation) != int:
        raise Exception("Error: 'sideLength' value is not numeric")

    separationMemory = separation
    
    for i in range(amount):
        draw_square(separation)
        separation += separationMemory






    
    
