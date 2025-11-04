def valores_repetidos(d):
    from collections import Counter
    valores = Counter(nueva_fila.values())
    repetidos = []
    for c in valores:
        #print(valores)
        if valores[c] > 1:
            #print(c)
            repetidos.append(c)
    return repetidos


if __name__ == '__main__':
    nueva_fila = {1:"a", 2:"b", 3:"a", 4:"d", 5:"e", 6:"b"}
    print(valores_repetidos(nueva_fila))
