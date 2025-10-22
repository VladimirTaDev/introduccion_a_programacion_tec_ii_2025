from es_primo import es_primo

def main():
    """
    Programa que encuentra los número primos en un rango.
    """
    try:
        inicio = int(input("Escriba el inicio del rango: "))
        final = int(input("Escriba el final del rango: "))
        for i in range(inicio, final, 1):
            if es_primo(i):
                print(i)
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    main()
