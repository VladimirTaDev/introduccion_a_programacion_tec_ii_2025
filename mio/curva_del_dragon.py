# Por: Vladimir Tarassenko 2025800696 - TEC 2025
import doctest
from turtle import *
import colorsys

# Constantes
LONGITUD_SEGMENTO = 10
ANGULO = 90

def generar_instrucciones_dragon(iteraciones):
    """
    Función que genera la lista de instrucciones para dibujar la curva del dragón.
    Entradas y restricciones:
    - iteraciones: int, iteraciones >= 0.
    Salidas:
    - list, lista con 'D' (derecha) e 'I' (izquierda) representando los giros.
    """
    if type(iteraciones) != int or iteraciones < 0:
        raise Exception("iteraciones debe ser un entero no negativo.")

    # Primera iteración: solo un giro a la derecha
    instrucciones = ['D']

    # Generar las siguientes iteraciones
    for i in range(iteraciones):
        nuevas_instrucciones = []
        alternar_derecha = True

        # Agregar nuevos ángulos entre cada instrucción existente
        nuevas_instrucciones.append('D' if alternar_derecha else 'I')
        alternar_derecha = not alternar_derecha

        for instruccion in instrucciones:
            nuevas_instrucciones.append(instruccion)
            nuevas_instrucciones.append('D' if alternar_derecha else 'I')
            alternar_derecha = not alternar_derecha

        instrucciones = nuevas_instrucciones

    return instrucciones


def dibujar_curva_dragon(instrucciones, longitud=LONGITUD_SEGMENTO, angulo=ANGULO,
                         usar_colores=True):
    """
    Función que dibuja la curva del dragón a partir de una lista de instrucciones.
    Entradas y restricciones:
    - instrucciones: list, lista con 'D' o 'I' indicando dirección de giro.
    - longitud: int o float, longitud > 0 (por defecto 10).
    - angulo: int o float, angulo de giro en grados.
    - usar_colores: bool, True para usar colores variados.
    Salidas:
    - No, dibuja en la ventana de turtle.
    """
    if type(instrucciones) != list:
        raise Exception("instrucciones debe ser una lista.")
    if type(longitud) not in (int, float) or longitud <= 0:
        raise Exception("longitud debe ser un número positivo.")
    if type(angulo) not in (int, float):
        raise Exception("angulo debe ser un número.")
    if type(usar_colores) != bool:
        raise Exception("usar_colores debe ser un booleano.")

    # Configurar turtle para dibujo rápido
    tracer(0, 0)
    speed(0)
    hideturtle()
    colormode(1.0)

    # Calcular incremento de color
    hue = 0
    incremento_hue = 360 / (len(instrucciones) + 1) if usar_colores else 0

    # Dibujar el primer segmento
    if usar_colores:
        r, g, b = colorsys.hsv_to_rgb(hue / 360, 1.0, 1.0)
        color(r, g, b)
        hue += incremento_hue

    forward(longitud)

    # Recorrer las instrucciones y dibujar
    for instruccion in instrucciones:
        # Girar según la instrucción
        if instruccion == 'D':
            right(angulo)
        else:  # instruccion == 'I'
            left(angulo)

        # Cambiar color si está habilitado
        if usar_colores:
            r, g, b = colorsys.hsv_to_rgb(hue / 360, 1.0, 1.0)
            color(r, g, b)
            hue = (hue + incremento_hue) % 360

        # Dibujar el segmento
        forward(longitud)

    update()


def curva_dragon(iteraciones, longitud=LONGITUD_SEGMENTO, angulo=ANGULO,
                 usar_colores=True):
    """
    Función principal que genera y dibuja la curva del dragón.
    Entradas y restricciones:
    - iteraciones: int, iteraciones >= 0.
    - longitud: int o float, longitud > 0.
    - angulo: int o float, angulo de giro en grados.
    - usar_colores: bool, True para usar colores variados.
    Salidas:
    - No, dibuja la curva del dragón en la ventana de turtle.
    """
    if type(iteraciones) != int or iteraciones < 0:
        raise Exception("iteraciones debe ser un entero no negativo.")
    if type(longitud) not in (int, float) or longitud <= 0:
        raise Exception("longitud debe ser un número positivo.")
    if type(angulo) not in (int, float):
        raise Exception("angulo debe ser un número.")
    if type(usar_colores) != bool:
        raise Exception("usar_colores debe ser un booleano.")

    # Limpiar pantalla
    reset()

    # Generar las instrucciones
    instrucciones = generar_instrucciones_dragon(iteraciones)

    # Dibujar la curva
    dibujar_curva_dragon(instrucciones, longitud, angulo, usar_colores)

if __name__ == '__main__':
    curva_dragon(12, 8, 90,True)

    # Con ángulo de 60:
    # curva_dragon(10, 10, 60,True)

    # Sin colores:
    # curva_dragon(12, 8, 90,FALSE)

    # Mantener la ventana abierta
    done()