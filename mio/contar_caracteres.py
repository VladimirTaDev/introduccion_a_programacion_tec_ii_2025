def contar_caracteres(s):
    """
    Función que retorna un diccionario con la
    cantidad de veces que aparece cada letra
    en un string.
    Entradas y restricciones:
    - s: un string.
    Salidas:
    Diccionario con los caracteres como llave
    y un entero con la cantidad de apariciones.
    """
    if type(s) != str:
        raise Exception("s debe ser un string.")
    caracteres = {}
    for c in s:
        if c not in caracteres:
            caracteres[c] = 1
        else:
            caracteres[c] += 1
    return caracteres

def main():
    texto = input("Escriba el texto a analizar: ")
    caracteres = contar_caracteres(texto)
    print("Cantidad de veces que aparece cada caracter:")
    for c, veces in caracteres.items():
        print(f"{c}: {veces}")

if __name__ == "__main__":
    main()