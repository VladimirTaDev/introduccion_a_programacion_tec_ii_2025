def encontrar(s):
    """
    Procedimiento que imprime ene pantalla el largo
    de la palabra más larga y la más corta de un mensaje.
    Entradas y restricciones:
    - s: string.
    Salidas:
    Imprime el largo de la palabra más larga y la más corta.
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
    sustituir = "AaÁÁEeÉéIiÍíOoÓóBbTtFfGgMmPp"
    reemplazo = "EeÉéAaÁáOoÓóIiÍíTtBbGgFfPpMm"
    for caracter in mensaje:
        if caracter in sustituir:
            indice = sustituir.index(caracter)
            codificado += reemplazo[indice]
        else:
            codificado += caracter
    return codificado

def alternados(l_numeros):
    """
    Función que recibe una lista de números y devuelve True si los elementos vienen alternados entre pares e impares.
    Entradas y restricciones:
    - l_numeros: lista de enteros.
    Salidas:
    - True si los números están alternados entre pares e impares. False en caso contrario.
    """
    if not isinstance(l_numeros, list):
        raise Exception("Debe ser una lista.")
    if len(l_numeros) < 2:
        raise Exception("Debe tener al menos dos elementos.")
    for numero in l_numeros:
        if type(numero) != int:
            raise Exception("Debe contener solo enteros.")

    for i in range(1, len(l_numeros)):
        # Verifica que ambos sean parea.
        if l_numeros[i] % 2 == 0 and l_numeros[i - 1] % 2 == 0:
            return False

    return True
