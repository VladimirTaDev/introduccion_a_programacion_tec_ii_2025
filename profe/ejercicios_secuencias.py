def encontrar(s):
    """
    Procedimiento que imprime ene pantalla el largo
    de la palabra más larga y la más corta de un mensaje.
    Entradas y restricciones:
    - s: string.
    Salidas:
    Imprime el largo de la palabra más larga y la más
    corta.
    """
    if type(s) != str:
        raise Exception("s debe ser un string.")
    for caracter in s:
        if not caracter.isalpha():
            s = s.replace(caracter, " ")
    palabras = s.split()
    corta = len(palabras[0])
    larga = len(palabras[0])
    for palabra in palabras[1:]:
        if corta > len(palabra):
            corta = len(palabra)
        if larga < len(palabra):
            larga = len(palabra)
    print(f"Más corta: {corta}")
    print(f"Más larga: {larga}")

def encontrar2(s):
    """
    Procedimiento que imprime ene pantalla el largo
    de la palabra más larga y la más corta de un mensaje.
    Entradas y restricciones:
    - s: string.
    Salidas:
    Imprime el largo de la palabra más larga y la más
    corta.
    """
    if type(s) != str:
        raise Exception("s debe ser un string.")
    for caracter in s:
        if not caracter.isalpha():
            s = s.replace(caracter, " ")
    palabras = s.split()
    largos = [len(palabra) for palabra in palabras]
    corta = min(largos)
    larga = max(largos)
    print(f"Más corta: {corta}")
    print(f"Más larga: {larga}")

def malespin(mensaje):
    """
    Función que codifica un mensaje en malespín.
    Entradas y restricciones:
    - mensaje: string.
    Salidas:
    Mensaje codificado.
    """
    if type(mensaje) != str:
        raise Exception("mensaje debe ser string.")
    codificado = ""
    sustituir = "AaÁáEeÉéIiÍíOoÓóBbTtFfGgMmPp"
    reemplazo = "EeÉéAaÁáOoÓóIiÍíTtBbGgFfPpMm"
    for caracter in mensaje:
        if caracter in sustituir:
            indice = sustituir.index(caracter)
            codificado += reemplazo[indice]
        else:
            codificado += caracter
    return codificado












    
