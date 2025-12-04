def sumar_digitos(n):
    """Función recursiva que suma los dígitos de un número entero positivo n."""
    def sumar_digitos_aux(n):
        if n < 10:
            return n
        else:
            digitos = len(str(n))
            return sumar_digitos_aux(n // 10 ** (digitos // 2)) + sumar_digitos_aux(n % 10 ** (digitos // 2))
    
    
    if type(n) != int or n < 0:
        raise Exception("n debe ser un entero positivo.")
    return sumar_digitos_aux(n)
