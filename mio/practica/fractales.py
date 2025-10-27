import turtle

def crear_sistema_l(axioma, reglas, iteraciones):
    """
    Función que genera una cadena de instrucciones basada en un sistema L.

    Entradas y restricciones:
    - axioma: str, la cadena inicial.
    - reglas: dict, un diccionario con las reglas de reemplazo.
    - iteraciones: int, el número de veces que se aplicarán las reglas. iteraciones >= 0.

    Salidas:
    - str, la cadena de instrucciones generada.
    """

    if type(iteraciones) != int or iteraciones < 0:
        raise Exception("El número de iteraciones debe ser un entero no negativo.")

    cadena_actual = axioma
    for _ in range(iteraciones):
        siguiente_cadena = ""
        for caracter in cadena_actual:
            siguiente_cadena += reglas.get(caracter, caracter)
        cadena_actual = siguiente_cadena
    return cadena_actual



def dibujar_fractal(tortuga, instrucciones, longitud, angulo):
    """
    Función que dibuja un fractal usando Turtle a partir de una cadena de instrucciones.

    Entradas y restricciones:
    - tortuga: objeto Turtle, la tortuga que dibujará.
    - instrucciones: str, la cadena con los comandos de dibujo.
    - longitud: int o float, la longitud de cada segmento. longitud > 0.
    - angulo: int o float, el ángulo de giro.

    Salidas:
    - None (dibuja en la pantalla de Turtle).
    """
    if type(longitud) not in (int, float) or longitud <= 0:
        raise Exception("La longitud debe ser un número positivo.")

    for comando in instrucciones:
        if comando == 'F':
            tortuga.forward(longitud)
        elif comando == 'B':
            tortuga.backward(longitud)
        elif comando == '+':
            tortuga.left(angulo)
        elif comando == '-':
            tortuga.right(angulo)


def main():

    """
    Función principal que configura y dibuja el fractal.
    """

    # --- Configuración del fractal de Koch ---
    # Axioma: El punto de partida del sistema.
    axioma_koch = "F"
    # Reglas: Cómo se transforma cada caracter en la siguiente iteración.
    # 'F' se convierte en 'F+F-F-F+F'
    reglas_koch = {"F": "F+F-F-F+F"}
    # Iteraciones: Cuántas veces aplicamos las reglas. Más iteraciones = más detalle.
    iteraciones = 5 # Puedes cambiar este número (prueba con 0, 1, 2, 3)
    # Ángulo: El ángulo que gira la tortuga. Para la curva de Koch es 90 grados.
    angulo = 90
    # Longitud: La longitud de cada línea. Se hace más pequeña con más iteraciones.
    longitud = 10

    # --- Generación y Dibujo ---
    # 1. Generar la cadena de instrucciones
    instrucciones = crear_sistema_l(axioma_koch, reglas_koch, iteraciones)

    # 2. Configurar la ventana y la tortuga
    ventana = turtle.Screen()
    ventana.bgcolor("white")
    ventana.title(f"Curva de Koch (Iteración {iteraciones})")

    tortuga = turtle.Turtle()
    tortuga.speed(0) # La velocidad más rápida
    tortuga.pencolor("blue")
    tortuga.penup()
    tortuga.goto(-ventana.window_width() / 2 + 50, 0) # Posición inicial
    tortuga.pendown()

    # Configurar turtle para dibujo rápido
    turtle.tracer(0, 0)
    turtle.speed(0)
    turtle.hideturtle()
    turtle.colormode(1.0)
    turtle.update()


    # 3. Dibujar el fractal
    dibujar_fractal(tortuga, instrucciones, longitud, angulo)

    # --- Finalizar ---
    tortuga.hideturtle()
    ventana.mainloop()



if __name__ == "__main__":
    main()
