def discriminante(a, b ,c):
    """
    Función que calcula el discriminante de una ecuación cuadrática
    Entradas y restrticciones:
    - a: real diferente a cero
    - b: real
    - c: real.
    Salidas:
    Valor del descriminante (real).
    """
    
    if type(a) not in (int, float) or a == 0:
        raise Exception("a debe ser diferente a cero.")
    if type(b) not in (int, float):
        raise Exception("b debe ser un real.")
    if type(c) not in (int, float):
        raise Exception("c debe ser un real.")
    d = b**2 - 4 * a * c
    return d
    
def main():
    """
    Programa principal que calcula las soluciones
    de una ecuación cuadrática de la forma
    ax² + bx + c = 0
    """
    try:
        print("Soluciones de una ecuación ax² + bx + c = 0")
        a = float(input("Escriba el valor de a: "))
        b = float(input("Escriba el valor de b: "))
        c = float(input("Escriba el valor de c: "))
        disc = discriminante(a, b, c)
        if disc < 0:
            print(f"La ecuación {a}x² + {b}x + {c} = 0 no tiene soluciones.")
        elif disc == 0:
            print(f"La ecuación {a}x² + {b}x + {c} = 0 tiene 1 solución: ")
            x = -b / (2 * a)
            print(f"x = {x}")
        else: # disc > 0
            print(f"La ecuación {a}x² + {b}x + {c} = 0 tiene 2 soluciones: ")
            x1 = (-b + math.sqrt(disc)) / (2 * a)
            x2 = (-b - math.sqrt(disc)) / (2 * a)
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
    except Exception as e:
        print(f"ERROR: {e}")
