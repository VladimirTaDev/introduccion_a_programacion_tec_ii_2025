def histograma(num):
    """Genera un histograma de asteriscos para un número dado.
    Entrada:
        num (int): Un número entero positivo.
    salida:
        str: Una cadena que representa el histograma.
    """
    if num < 0 or not isinstance(num, int):
        raise ValueError("El número debe ser un entero positivo.")

    for digito in str(num):
        estrellas = ""
        for i in range(int(digito)):
            estrellas += "*"
        print(str(digito) + " " + estrellas)

if __name__ == "__main__":
    numero = int(input("Ingrese un número entero positivo: "))
    histograma(numero)