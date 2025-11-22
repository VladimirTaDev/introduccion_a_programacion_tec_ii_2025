from random import randrange

VACIA = 0
MANZANA = -1
DORADA = -2
VENENO = -3

class Direccion:
    DERECHA = 0
    IZQUIERDA = 1
    ARRIBA = 2
    ABAJO = 3

matriz = []
filas = 0
columnas = 0
venenos = 10

serpiente = {
    "fila" : 0,
    "col" : 0,
    "dir" : Direccion.DERECHA,
    "cola" : 1,
    "viva" : True,
    "manzanas_comidas" : 0
}

def inicializar_matriz(filas, columnas):
    return [[0 for f in range(filas)] for c in range(columnas)]

def colocar_serpiente():
    matriz[serpiente["fila"]][serpiente["col"]] = serpiente["cola"]

def colocar_manzana():
    colocada = False
    while not colocada:
        fila_manzana = randrange(0, filas)
        col_manzana = randrange(0, columnas)
        if matriz[fila_manzana][col_manzana] == VACIA:
            if randrange(0, 101) > 5:
                matriz[fila_manzana][col_manzana] = MANZANA
            else:
                matriz[fila_manzana][col_manzana] = DORADA
            colocada = True

def colocar_veneno(venenos = 1):
    colocada = False
    while not colocada:
        fila_veneno = randrange(0, filas)
        col_veneno = randrange(0, columnas)
        if matriz[fila_veneno][col_veneno] == VACIA:
            matriz[fila_veneno][col_veneno] = VENENO
            venenos -= 1
        if venenos <= 0:
            colocada = True

def siguiente_posicion():
    match serpiente["dir"]:
        case Direccion.DERECHA:
            return serpiente["fila"], (serpiente["col"] + 1) % columnas
        case Direccion.IZQUIERDA:
            return serpiente["fila"], (serpiente["col"] - 1) % columnas
        case Direccion.ARRIBA:
            return (serpiente["fila"] - 1) % filas, serpiente["col"]
        case Direccion.ABAJO:
            return (serpiente["fila"] + 1) % filas, serpiente["col"]

def cambiar_direccion(nueva_direccion):
    no_permitidas = [
        (Direccion.DERECHA, Direccion.IZQUIERDA),
        (Direccion.IZQUIERDA, Direccion.DERECHA),
        (Direccion.ARRIBA, Direccion.ABAJO),
        (Direccion.ABAJO, Direccion.ARRIBA),
    ]
    if (serpiente["dir"], nueva_direccion) not in no_permitidas:
        serpiente["dir"] = nueva_direccion

def avanzar():
    if serpiente["viva"]:
        nueva_fila, nueva_columna = siguiente_posicion()
        if matriz[nueva_fila][nueva_columna] > VACIA:
            serpiente["viva"] = False
        else:
            if matriz[nueva_fila][nueva_columna] == MANZANA:
                serpiente["cola"] += 1
                colocar_manzana()
                serpiente["manzanas_comidas"] +=1
            elif matriz[nueva_fila][nueva_columna] == DORADA:
                serpiente["cola"] += 15
                colocar_manzana()
                serpiente["manzanas_comidas"] += 1
            elif matriz[nueva_fila][nueva_columna] == VENENO:
                if serpiente["cola"] <= 2:
                    serpiente["viva"] = False
                serpiente["cola"] //= 2
                colocar_veneno()

            for f in range(filas):
                for c in range(columnas):
                    if matriz[f][c] > 0:
                        matriz[f][c] -= 1
            matriz[nueva_fila][nueva_columna] = serpiente["cola"]
            serpiente["fila"] = nueva_fila
            serpiente["col"] = nueva_columna

def init():
    global filas, columnas, matriz, serpiente, venenos
    filas = 50
    columnas = 50
    venenos = 10
    matriz = inicializar_matriz(filas, columnas)
    serpiente["fila"] = filas // 2
    serpiente["col"] = columnas // 2
    serpiente["dir"] = Direccion.DERECHA
    serpiente["cola"] = 1
    serpiente["viva"] = True
    colocar_serpiente()
    colocar_manzana()
    colocar_veneno(venenos)