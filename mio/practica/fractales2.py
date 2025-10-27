import turtle

def crear_regla_l(iteraciones, axioma, reglas):
    cadena_actual = axioma
    for _ in range(iteraciones):
        nueva_cadena = ""
        for caracter in cadena_actual:
            nueva_cadena += reglas.get(caracter, caracter)
        cadena_actual = nueva_cadena

    return cadena_actual

def dibujar_regla_l(t, instrucciones, angulo, distancia):
    for comando in instrucciones:
        if comando == 'F':
            t.forward(distancia)
        elif comando == '+':
            t.left(angulo)
        elif comando == '-':
            t.right(angulo)

def main():
    # Parámetros para la curva de Koch
    axioma = "F"
    reglas = {"F": "F+F--F+F"}
    iteraciones = 3  # Prueba cambiando este valor (e.g., 0, 1, 2, 3)
    angulo = 60
    longitud_segmento = 10

    # 1. Generar la cadena de instrucciones
    instrucciones = crear_regla_l(iteraciones, axioma, reglas)

    # Configurar turtle para dibujo rápido
    turtle.tracer(0, 0)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.colormode(1.0)
    turtle.update()

    # 3. Dibujar
    t = turtle.Turtle()
    dibujar_regla_l(t, instrucciones, angulo, longitud_segmento)

if __name__ == "__main__":
    main()
    turtle.Screen().exitonclick()
    # Mantener la ventana abierta
    turtle.done()
