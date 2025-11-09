def busquedaAnidada(L, e):
    """
    Programa que chequea si un elemento cualquiera se encuentra en la lista,
    utilizando recursión de pila y retorna verdadero o falso.
    """
    if L == []:
        return False
    elif isinstance(L[0], list):
        return busquedaAnidada(L[0] + L[1:], e)
    elif L[0] == e:
        return True
    else:
        return busquedaAnidada(L[1:], e)

def borradoAnidado(L, e):
    """
    Algoritmo que elimina una ocurrencia de cualquier tipo de la lista
    sin modificar su estructura.
    """
    if L == []:
        return []
    elif isinstance(L[0], list):
        return [borradoAnidado(L[0], e)] + borradoAnidado(L[1:], e)
    elif L[0] == e:
        return [] + borradoAnidado(L[1:], e)
    else:
        return [L[0]] + borradoAnidado(L[1:], e)

def unicos(L):
    """
    Algoritmo que recibe una lista, y retorna otra lista solo con los elementos únicos.
    """
    def aux(resto, nueva, repetidos):
        if resto == []:
            return nueva
        elif resto[0] in resto[1:] or resto[0] in repetidos:
            repetidos.append(resto[0])
            return aux(resto[1:], nueva, repetidos)
        else:
            nueva.append(resto[0])
            return aux(resto[1:], nueva, repetidos)

    if not isinstance(L, list):
        raise TypeError("Entrada debe ser una lista.")

    return aux(L, [], [])

def primeros(L):
    def aux(l, primer=[], i=0):
        if i >= len(l):
            return primer
        primer.append(l[i][0])
        return aux(l, primer, i + 1)

    def esListaDeListas(l, i=0):
        if i >= len(l):
            return True
        elif isinstance(l[i], list) and l[i] != []:
            return esListaDeListas(l, i + 1)
        return False

    if not isinstance(L, list):
        raise TypeError("Entrada debe ser una lista.")
    if len(L) != 0 and not esListaDeListas(L):
        raise TypeError("Entrada debe ser una lista de listas no vacías.")

    return aux(L)

if __name__ == "__main__":
    print(primeros([]))