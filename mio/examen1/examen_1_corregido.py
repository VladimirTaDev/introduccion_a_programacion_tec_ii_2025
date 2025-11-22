def ejecutar_hosoya():
    """
    Programa que le solicita al usuario el número de fila y columnas para generar
    el triángulo de Hosoya y chequea restricciones.
    Entradas y restricciones:
    - filas (int) positivo
    - columnas (int) positivo
    Salida:
    - (list) lista de listas que representa el triángulo de Hosoya.
    """
    # Pide entradas hasta recibir una válida.
    # Pide filas.
    filas = input("Introduzca el número de filas: ")
    while not filas.isdigit() or int(filas) <= 0:
        print("El número de filas debe ser un entero positivo.")
        filas = input("Favor introduzca el número de filas nuevamente: ")
    filas = int(filas)
    # Pide columnas.
    columnas = input("Introduzca el número de columnas: ")
    while not columnas.isdigit() or int(columnas) <= 0:
        print("El número de columnas debe ser un entero positivo.")
        columnas = input("Favor introduzca el número de columnas nuevamente: ")
    columnas = int(columnas)


    # Función auxiliar que construye el triángulo de Hosoya.
    def hosoya(filas, columnas):
        """
        Función que calcula el triángulo de Hosoya.
        Entradas y restricciones:
        - filas (int) positivo
        - columnas (int) positivo
        Salida:
        - (list) lista de listas que representa el triángulo de Hosoya.
        """
        triangulo = [[1, 1], [1, 1]]

        # Calcula primeras dos filas y columnas en ellas.
        for columna in range(columnas - 2):
            triangulo[0].append(triangulo[0][columna] + triangulo[0][columna + 1])
            triangulo[1].append(triangulo[1][columna] + triangulo[1][columna + 1])

        for fila in range(filas - 2):
            fila_nueva = []
            for columna in range(columnas):
                fila_nueva.append(triangulo[fila][columna] + triangulo[fila + 1][columna])
            triangulo.append(fila_nueva.copy())
            fila_nueva.clear()

        return triangulo

    return hosoya(filas, columnas)

def invertir_diccionario(D):
    """
    Función que invierte los elementos de un diccionario, las llaves se convierten en
    valores y valores en llaves, agregando llaves repetidas como un array.
    Entradas y restricciones:
    - D: (dict), diccionario con llaves y valores de cualquier tipo.
    Salidas:
    - dict, diccionario invertido.
    """
    # Validación
    if not isinstance(D, dict):
        raise TypeError("D debe ser un diccionario.")

    invertido = {}

    for llave in D:
        # Chequea si la llave del diccionario ya se agregó cómo valor.
        if D[llave] in invertido:
            invertido[D[llave]] = invertido[D[llave]] + [llave]
        else:
            invertido[D[llave]] = [llave]
    return invertido

def feliz(n):
    """
    Función que calcula si un número es feliz.
    Entradas y restricciones:
    - n: (int), positivo.
    Salidas:
    - (bool) True si el número es feliz, False si no.
    """
    if not isinstance(n, int):
        raise TypeError("n debe ser un entero.")
    if n < 0:
        raise ValueError("n debe ser un entero positivo.")

    suma = 0
    n_nueva = n
    n_elevada = []
    n_calculados = []

    while suma != 1:
        n_elevada.clear()
        suma = 0

        for num in str(n_nueva):
            n_elevada.append(int(num) * int(num))
        for num2 in n_elevada:
            suma += num2

        # Entró en loop
        if suma in n_calculados:
            return False

        n_nueva = suma
        n_calculados.append(suma)

    return True

if __name__ == "__main__":
    #print(ejecutar_hosoya())
    #print(invertir_diccionario({1:10, 2:20, 3:30, 4:40, 5:10, 6:30}))
    print(feliz(82))
