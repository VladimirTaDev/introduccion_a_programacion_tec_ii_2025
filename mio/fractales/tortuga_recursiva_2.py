from turtle import *
from math import sqrt

def fees_aux(prof, tam):
    if prof == 0:
        fd(tam)
        return
    else:
        lt(90)
        fees_aux(prof - 1, tam/2)
        rt(135)
        hip = sqrt(2 * tam**2)
        fees_aux(prof - 1, hip/2)
        fees_aux(prof - 1, hip/2)
        lt(135)
        fees_aux(prof - 1, tam/2)
        rt(90)
        return

def fees(prof, tam):
    tracer(0, 0)
    hideturtle()
    reset()
    fees_aux(prof, tam)
    update()
    done()

def sierpinski_aux(prof, tam):
    if prof == 0:
        return
    else:
        for i in range(4):
            sierpinski_aux(prof - 1, tam / 3)
            forward(tam)
            #forward(tam / 3)
            #sierpinski_aux(prof - 1, tam / 3)
            #forward(2 * tam / 3)
            right(90)
        return

def sierpinski(prof, tam):
    tracer(0, 0)
    hideturtle()
    reset()
    sierpinski_aux(prof, tam)
    update()
    done()

def triangulo_sierpinski_aux(prof, tam):
    if prof == 0:
        return
    else:
        forward(tam / 2)
        left(45)
        forward(tam)
        right(120)
        triangulo_sierpinski_aux(prof - 1, tam / 2)
        return


def canessa_aux(prof, tam):
    if prof == 0:
        return
    else:
        for i in range(4):
            left(90)
            canessa_aux(prof - 1, tam / 3)
            right(90)
            forward(tam)
            right(90)
        return

def canessa(prof, tam):
    reset()
    tracer(0, 0)
    hideturtle()
    canessa_aux(prof, tam)
    update()
    done()

if __name__ == "__main__":
    tracer(0, 0)
    hideturtle()
    reset()
    
    sierpinski(5, 150)

    update()
    done()