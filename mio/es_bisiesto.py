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
  # return año % 4 == 0 and (not año % 100 == 0 or año % 400 == 0)

# ¿Cómo usar esta función para hacer una que diga que una fecha es válida?
# enero = 1..diciembre = 12
def es_fecha_valida(dia, mes, año):
    """
    Valida si una fecha es correcta utilizando la función es_bisiesto.
    """
    if not (1 <= mes <= 12):
            return False

        # 2. Definir días por mes para un año no bisiesto.
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        # 3. Ajustar para febrero en año bisiesto.
    if es_bisiesto(año):
        dias_por_mes[2] = 29
        
        # 4. Validar que el día sea correcto para el mes y año dados.
    return 1 <= dia <= dias_por_mes[mes]
     #  return 1 <= dia and dia <= dias_por_mes[mes]
     

# Imprimir los años bisiestos en un rango especifico
def imprimir_bisiestos_en_rango(inicio, fin):
    """
    Imprime en la consola todos los años bisiestos dentro de un rango.

    - inicio: El primer año del rango a verificar.
    - fin: El último año del rango a verificar.
    """
    print(f"Años bisiestos entre {inicio} y {fin}:")
    # Itera a través de cada año en el rango especificado.
    for ano in range(inicio, fin + 1):
        if es_bisiesto(ano):
                print(ano)
