def es_bisiesto(año):
    """
    Función booleana que dice si sun año es bisiesto
    - año: un entero mayor o igual al 1582.
    Salida
    - True si es bisiesto, False si no.
    """
    if type(año) != int or año < 1582:
        raise Exception("Año debe ser un entero mayor o igual a 1582.")
    condicion1 = año % 4 == 0
    condicion2 = año % 100 == 0
    condicion3 = año % 400 == 0
    bisiesto = condicion1 and (not condicion2 or condicion3)
    return bisiesto
  #  return año % 4 == 0 and (not año % 100 == 0 or año % 400 == 0)

# Cómo usar esta función para hacer una que diga que una fecha es válida.
# enero = 1..diciembre = 12

def es_fecha_valida(dia, mes, año):
    pass

# Imprimir los años bisiestos en un rango especifico
