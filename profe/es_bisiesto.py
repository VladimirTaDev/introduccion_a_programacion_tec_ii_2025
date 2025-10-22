def es_bisiesto(año):
    """
    Función booleana que dice si un año es bisiesto.
    Entradas y restricciones:
    - año: un entero mayor o igual a 1582.
    Salidas:
    True si es bisiesto, False si no.
    """
    if type(año) != int or año < 1582:
        raise Exception("año debe ser un entero mayor o igual a 1582.")
    condicion1 = año % 4 == 0
    condicion2 = año % 100 == 0
    condicion3 = año % 400 == 0
    return condicion1 and (not condicion2 or condicion3)

# cómo usar esta función para hacer una que diga si una fecha es válida.
# enero = 1..diciembre = 12

def es_fecha_valida(dia, mes, año):
    pass

# imprimir los años bisiestos en un rango específico
