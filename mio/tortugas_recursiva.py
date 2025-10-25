# Una forma de hacer repeticiones
# Repeticiones autosimilares
# Dividir el problema en problemas más simples
# Subrutinas que se invocan a sí mismas
# Caso base y caso general
# Subrutinas se dividen en principal y auxiliar
# Principal: chequeo de restricciones y trabajo que se
# hace una sola vez
# Auxiliar: resolver algún problema con recursión.
from math import sqrt
from turtle import *

TAM_MINIMO = 3
ANGULO = 47
RELACION = 0.68

def arbol_aux(tam):
    pensize(tam * 0.10)
    if tam <= TAM_MINIMO:
        circle(tam)
        return
    else:
        forward(tam)
        left(ANGULO)
        arbol_aux(tam * RELACION)
        right(ANGULO * 2)
        arbol_aux(tam * RELACION)
        left(ANGULO)
        back(tam)
        return

def arbol(tam):
    if type(tam) not in (float, int):
        raise Exception("tam debe ser un número.")
    tracer(0, 0)
    reset()
    speed(0)
    left(90)
    hideturtle()
    arbol_aux(tam)
    update()

def koch_aux(tam):
    if tam <= TAM_MINIMO:
        forward(tam)
        return
    else:
        koch_aux(tam / 3)
        left(60)
        koch_aux(tam / 3)
        right(120)
        koch_aux(tam / 3)
        left(60)
        koch_aux(tam / 3)
        return

def koch(tam):
    if type(tam) not in (float, int):
        raise Exception("tam debe ser un número")
    tracer(0, 0)
    # reset()
    speed(0)
    hideturtle()
    koch_aux(tam)
    update()

def koch_snowflake(tam):
    for i in range(3):
        koch(tam)
        right(120)

def levy_c_aux(tam):
    if tam <= TAM_MINIMO:
        forward(tam)
        return
    else:
        hip = sqrt(2 * (tam / 2) ** 2)
        left(45)
        levy_c_aux(hip)
        right(90)
        levy_c_aux(hip)
        left(45)

def levy_c(tam):
    if type(tam) not in (float, int) or tam <= 0:
        raise Exception("tam debe ser un número positivo.")
    tracer(0, 0)
    speed(0)
    hideturtle()
    levy_c_aux(tam)
    update()

def curva_propia_aux(tam):
    if tam <= TAM_MINIMO:
        forward(tam)
        return
    else:
        left(90)
        curva_propia_aux(tam / 2)
        right(90)
        curva_propia_aux(tam / 2)
        forward(tam)
        left(90)
        curva_propia_aux(tam / 2)
        left(90)
        curva_propia_aux(tam / 2)
        return

def curva_propia(tam):
    if type(tam) not in (float, int) or tam <= 0:
        raise Exception("tam debe ser un número positivo.")
    tracer(0, 0)
    reset()
    speed(0)
    hideturtle()
    curva_propia_aux(tam)
    update()

# reset()

if __name__ == '__main__':
    curva_propia(100)