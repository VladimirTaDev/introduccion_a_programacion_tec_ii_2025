from re import L
import json

def merge_sort(L):
    # Merge sort:
    # - Basado en comparaciones y en la técnica divide y vencerás.
    # - Pasos:
    #   - Dividir la lista en sublistas de 1 elemento.
    #   - Repetidamente mezclar las listas para producir nuevas sublistas hasta que
    #     solo haya una lista.
    # Recursivamente:
    # - Base: la lista de 1 elemento -> se retorna igual.
    # - General:
    #   - Divide la lista en 2 (izquierda y derecha).
    #   - Ordenar recursivamente ambas listas.
    #   - Unir las dos listas.

    def merge(izq, der):
        resultado = []
        while izq != [] and der != []:
            if izq[0] >= der[0]:
                resultado.append(izq.pop(0))
            else:
                resultado.append(der.pop(0))
        resultado.extend(izq + der)
        return resultado

    def merge_sort_aux(L):
        if len(L) == 1:
            return L
        else:
            izq = L[:len(L) // 2]
            der = L[len(L) // 2:]
            izq = merge_sort_aux(izq)
            der = merge_sort_aux(der)
            resultado = merge(izq, der)
            return resultado

    if type(L) != list:
        raise Exception("L debe ser una lista.")
    return merge_sort_aux(L)

def repetidos(L):
    def en(e, L):
        if len(L) == 0:
            return False
        if L[0] == e:
            return True
        else:
            return en(e, L[1:])
    
    def aux(L_resto, repetidos=[]):
        if len(L_resto) == 0:
            return repetidos

        if en(L_resto[0], L_resto[1:]) and not en(L_resto[0], repetidos):
            repetidos.append(L_resto[0])

        return aux(L_resto[1:], repetidos)

    if not isinstance(L, list):
        raise TypeError("Debe ser una lista1")

    if type(L) != list:
        raise TypeError("Debe ser una lista")
    if L == []:
        raise TypeError("Debe ser una lista no vacia")
            
    return aux(L)

def quick_sort(L):
    # - Basado en la técnica de "divide y vencerás".
    # - Originalmente recursivo.
    # - Pasos:
    #   - Escoger un elemento llamado pivote.
    #   - Dividir la lista en mayores y menores que el pivote.
    #   - Repetir recursivamente en las dos listas.
    #   - Caso base: si la lista es de 1 elemento, ya está ordenada.
    # - No estable e in-place.

    def quick_sort_aux(L):
        if len(L) <= 1:
            return L
        else:
            pivote = L.pop(len(L) // 2)
            menores = [x for x in L if x > pivote]
            mayores = [x for x in L if x <= pivote]
            return quick_sort_aux(menores) + [pivote] + quick_sort_aux(mayores)

    if type(L) != list:
        raise Exception("L debe ser una lista.")
    return quick_sort_aux(L)

def quick_sort_padron(L, criterio):   
    
    def quick_sort_aux(L):
        if len(L) <= 1:
            return L
        else:
            pivote = L.pop(len(L) // 2)
            menores = [x for x in L if x[crit] < pivote[crit]]
            mayores = [x for x in L if x[crit] >= pivote[crit]]
            return quick_sort_aux(menores) + [pivote] + quick_sort_aux(mayores)


    # elegir criterio
    crit = 5
    match criterio:
        case "nombre":
            crit = 5
        case "apellido1":
            crit = 6
        case "apellido2":
            crit = 7

    # chequea restricciones
    if type(L) != list or type(L[0]) != list:
        raise Exception("L debe ser una lista de listas.")

    return quick_sort_aux(L)

def ordenarPadron(nombreArchivo, criterio):
    with open(nombreArchivo, "r") as archivo:

        padron = json.load(archivo)
        pardon_ordenado = quick_sort_padron(padron, criterio)
        print(pardon_ordenado)
        

    with open(nombreArchivo, "w") as archivo:
        json.dump(pardon_ordenado, archivo)
    
    print("done")

def sumaEstacionaria(n):
    def sumar(n, suma=0):
        if n == 0:
            return suma
        suma += n % 10
        return sumar(n // 10, suma)

    def aux(n):
        if n < 10:
            return n
        return aux(sumar(n))

    return aux(n)

def lucas(a, b, n):

    def aux(n, S=[]):
        if len(S) >= n:
            return S
        siguiente = S[len(S)-2] + S[len(S)-1]
        S.append(siguiente)
        return aux(n, S)

    return aux(n, [a, b])

def mbonacci(n, m):
    def aux(n, m):
        if n == 0:
            return 0
        if n == 1:
            return 1
        return m * aux(n - 1, m) + aux(n - 2, m)

    return aux(n, m)


if __name__ == "__main__":
    LL = [
    ["500660251", "505004", "1", "20200616", "00000", "JORGE", "ABARCA", "ABARCA"],
    ["301180718", "119067", "2", "20201026", "00000", "HORTENSIA", "ZU\u00d1IGA", "ABARCA"],
    ["105520570", "308002", "2", "20220910", "00000", "HILDA MARIA", "ABARCA", "ABARCA"],
    ["304730481", "305010", "1", "20230509", "00000", "CARLOS MANUEL", "ZU\u00d1IGA", "ABARCA"],
    ["301941422", "119071", "2", "20180829", "00000", "DONELIA", "ABARCA", "ABARCA"],
    ["602130052", "609025", "2", "20180702", "00000", "ELIETTE", "VINDAS", "ABARCA"],
    ["113480212", "303005", "1", "20160406", "00000", "FAEZ ISMAEL", "ABDALLA", "ABARCA"],
    ["110750321", "119043", "1", "20250817", "00000", "HECTOR", "VARGAS", "ABARCA"],
    ["104980153", "119088", "1", "20191125", "00000", "EDWIN", "ALFARO", "ABARCA"],
    ["109880309", "103005", "1", "20220705", "00000", "ANDRES", "VARGAS", "ABARCA"]
     ]
    
    L = [2, 5, 6, 8, 2]
    print(mbonacci(6, 3))

