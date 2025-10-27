import turtle

def generar_instrucciones(iteraciones):
    instruccion_nueva = ["D"]

    for _ in range(iteraciones):
        instruccion_anterior = instruccion_nueva.copy()
        instruccion_nueva.clear()
        instruccion_nueva.append("D")
        switch = False
        for elemento in instruccion_anterior:
            instruccion_nueva.append(elemento)
            if switch:
                instruccion_nueva.append("D")
                switch = False
            else:
                instruccion_nueva.append("I")
                switch = True

    return instruccion_nueva

def dibujar_dragon(iteraciones, distancia):
    instrucciones = generar_instrucciones(iteraciones)

    for i in instrucciones:
        turtle.forward(distancia)
        if i == "D":
            turtle.right(90)
        elif i == "I":
            turtle.left(90)


if __name__ == "__main__":
    # Configurar turtle para dibujo rápido
    turtle.tracer(0, 0)
    turtle.speed(0)
    # turtle.hideturtle()
    turtle.colormode(1.0)
    turtle.update()

    dibujar_dragon(50, 50)

    turtle.update()
    turtle.Screen().exitonclick()
    turtle.done()