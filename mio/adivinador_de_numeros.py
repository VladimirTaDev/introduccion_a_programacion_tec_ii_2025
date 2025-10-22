from random import randint

class Respuesta:
    """
    Enumaración que representa las posibles respuestas del usuario
    """
    IGUALES = 0
    MENOR = -1
    MAYOR = 1

def leer_respuesta_comparacion(intento):
    """
    Función que pregunta al usuario y dice
    si un intento es menor, igual o mayor
    al número que está pensando.
    Entradas y restricciones:
    - intento: entero entre [minimo, maximo]
    Salidas:
    Si el número del usuario es igual al intento (0),
    menor (-1) o mayor (1).
    """
    print(f"Creo que número que usted está pensando es {intento}.")
    print("A. Sí, adivinó.")
    print("B. Mi número es menor.")
    print("C. Mi número es mayor.")
    respuesta = input("Su opción: ")
    respuesta = respuesta.upper()
    while respuesta not in ("A", "B", "C"):
        respuesta = input("Escriba una opción válida: ")
    if respuesta == "A":
        return Respuesta.IGUALES
    elif respuesta == "B":
        return Respuesta.MENOR
    else:
        return Respuesta.MAYOR

def main():
    """
    Programa de un juego que adivina el número que
    el usuario piense entre 0 y N.
    """
    
    try:
        print("Adivinador de Número")
        maximo = int(input("Escriba el valor máximo del rango a adivinar [0..N]: "))
        minimo = 0
        continuar = True
        while continuar:
            intento = randint(minimo, maximo)
            resultado = leer_respuesta_comparacion(intento)
            if resultado == Respuesta.IGUALES: # adivinamos
                print("¡Enbuenahora he adivinado!")
                print("Gracias por jugar.")
                continuar = False
            elif resultado == Rwspuesta.MENOR: # el número es menor
                maximo = intento - 1
            elif resultado == Respuesta.MAYOR:
                minimo = intento + 1
            if maximo < minimo:
                print("Imposible adivinar, la información es incorrecta.")
                continuar = False
    
    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
