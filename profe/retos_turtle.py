from turtle import *

def escalera(n, tam):
    hideturtle()
    tracer(0, 0)
    for i in range(n):
        forward(tam)
        right(90)
        forward(tam)
        left(90)
    update()

def cuadro_escalera(n, tam):
    hideturtle()
    tracer(0, 0)
    for i in range(4):
        escalera(n, tam)
        right(90)
    update()

def cuadros_escalera(n):
    hideturtle()
    tracer(0, 0)
    for i in range(n):
        cuadro_escalera(5, 10)
        right(360/n)
    update()

def poligono(n, tam):
    hideturtle()
    tracer(0, 0)
    for i in range(n):
        forward(tam)
        right(360/n)
    update()

def triangulo(tam):
    poligono(3, tam)

def espiral_triangulo():
    for i in range(180):
        triangulo(i)
        right(2)

def estrella(tam):
    hideturtle()
    tracer(0, 0)
    for i in range(5):
        forward(tam)
        right(144)
    update()

def cuadro_45(tam):
    for i in range(8):
        poligono(4, tam)
        right(45)

def estrella2(tam):
    hideturtle()
    tracer(0, 0)
    for i in range(5):
        forward(tam)
        poligono(5, tam/4)
        right(144)
    update()

def cuadro_esquinas(tam):
    for i in range(4):
        triangulo(tam/2)
        forward(tam)
        right(90)
    update()

def pentagono_esquinas(tam):
    for i in range(5):
        poligono(4, -tam/2)
        forward(tam)
        right(360/5)
    update()

def poli_poligono(tam):
    for i in range(3, 10):
        poligono(i, tam)

def escalestrella(tam):
    for i in range(5):
        escalera(15, tam/15)
        right(144)

def triangulitos(tam):
    for i in range(3):
        for t in range(tam // 4, tam, tam // 4):
            triangulo(t)
            forward(t)
        left(120)
    update()
        
        
