vocales = {
    "a": "",
    "á": "",
    "e": "",
    "é": "",
    "i": "",
    "í": "",
    "o": "",
    "ó": "",
    "u": "",
    "ú": ""
}

## Es vocal

def es_vocal(letra):
    """
    Programa que chequea si una letra es vocal
    - Entradas y restricciones: letra (str == 1).
    - Salida: True (bool) si es vocal.
    """
    if len(str(letra)) != 1:
        raise Exception("Letra debe ser de 1 caracter")

    if str(letra).lower() not in vocales:
        return False
    else:
        return True

# Vocales Primero

def vocales_primero(palabra):
    """
    Programa que reordena un string poniendo vocales primero
    - Entradas y restricciones: palabra (str > 1).
    - Salida: palabra reordenada (str).
    """
    if len(str(palabra)) < 1:
        raise Exception("La palabra debe ser mayor que 1 caracter")
    reordenada_vocal = ""
    reordenada_consonante = ""

    for letra in palabra:
        if es_vocal(letra):
            reordenada_vocal += letra
        else:
            reordenada_consonante += letra

    return reordenada_vocal + reordenada_consonante

if __name__ == "__main__":
    print(es_vocal("a"))
    print(vocales_primero("aDteeoOpxC")) # Esperado: aeeoODtpxC
    print(vocales_primero("QueEsEstoAuxilio"))  # Esperado: ueEEoAuiioQsstxl