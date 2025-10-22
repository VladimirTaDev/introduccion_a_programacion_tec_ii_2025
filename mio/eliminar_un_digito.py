## Eliminar dígito
def elimina(n, d):
    """
    Función que elimina toda ocurrencia del dígito d en n.
    Entradas y restricciones:
    - n: int, n >= 0.
    - d: int, 0 <= d <= 9.
    Salidas:
    - int, número resultante de eliminar toda ocurrencia
      del dígito d en n. Si d no está en n, devuelve n.
    """
    if type(n) != int or n < 0:
        raise Exception("n debe ser un entero no negativo.")
    if type(d) != int or d < 0 or d > 9:
        raise Exception("d debe ser un entero entre 0 y 9.")

    resultado = 0
    posicion = 1
    while n > 0:
        digito = n % 10
        if digito != d:
            resultado += digito * posicion
            posicion *= 10
        n //= 10
    return resultado

## Eliminar dígitos
def eliminaTodos(n, m):
    """
        Función que elimina todas las ocurrencias de los dígitos de m en n.
        Entradas y restricciones:
        - n: int, n >= 0.
        - m: int, m >= 0. Cada dígito de m será eliminado de n.
        Salidas:
        - int, número resultante de eliminar todas las ocurrencias
          de los dígitos de m en n. Si ningún dígito de m está en n, devuelve n.
        """
    if type(n) != int or n < 0:
        raise Exception("n debe ser un entero no negativo.")
    if type(m) != int or m < 0:
        raise Exception("m debe ser un entero no negativo.")
    lista_m = [int(numero) for numero in str(m)] # Separa los números m en una lista.
    for individual in lista_m:
        n = elimina(n, individual)
    return n

# Pruebas:
if __name__ == "__main__":
    print(elimina(6549846, 4))  # Debería imprimir 65986
    print(elimina(55555, 5))    # Debería imprimir 0
    print(elimina(100001, 0))   # Debería imprimir 11
    print(eliminaTodos(621654, 65))    # Debería imprimir 214
    print(eliminaTodos(7239186, 1234)) # Debería imprimir 7986