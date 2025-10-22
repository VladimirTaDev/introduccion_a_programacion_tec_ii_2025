from turtle import *

def cuadrado(lado):
    for i in range(4):
        forward(lado)
        right(90)
        
def triangulo(lado):
    for _ in range(3):
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
        forward (lado)
        right (-144)

def estrella_pentagono(lado):
    for i in range(5):
        forward (lado)
        sombrilla(lado / 5)
        right (144)

def tunel(n, lado):
    for i in range(3, n+3):
        poligono(i, lado+i)
