def sustitucion(L, orig, sust):
    """
    Función que sustituye todas las ocurrencias
    de un elemento por otro.
    Entradas y restricciones:
    - L: lista
    - orig: elemento original, cualquier cosa.
    - sust: elemento sustituto, cualquier cosa.
    Salidas:
    L modificada.
    """
    if type(L) != list:
        raise Exception("L debe ser una lista.")
    pos = 0
    while pos < len(L):
        if L[pos] == orig:
            L[pos] = sust
        pos += 1
    return L
