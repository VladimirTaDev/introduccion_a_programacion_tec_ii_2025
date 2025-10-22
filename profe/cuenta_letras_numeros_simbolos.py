def cuenta(s):
    """
    Subrutina que imprime la cantidad de letras, números
    y símbolos que tiene un string.
    Entradas y restricciones:
    - s: string.
    Salidas:
    Cantidad de letras, cantidad de dígitos, cantidad
    de símbolos.
    """
    if type(s) != str:
        raise Exception("s debe ser un string.")
    letras = 0
    numeros = 0
    simbolos = 0
    i = 0
    while i < len(s):
        caracter = s[i]
        if caracter.isalpha():
            letras += 1
        elif caracter.isdigit():
            numeros += 1
        else:
            simbolos += 1
        i += 1
    print(f"Cantidad de letras:   {letras}")
    print(f"Cantidad de números:  {numeros}")
    print(f"Cantidad de símbolos: {simbolos}")
            
