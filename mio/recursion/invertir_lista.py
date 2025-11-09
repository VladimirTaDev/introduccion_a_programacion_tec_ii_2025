def invertir(lista):
    """
    Entradas y restricciones:
    - lista: (list, any) la lista que se quiere invertir.
    Salidas:
    - lista (list, any) la lista invertida.
    """
    if not isinstance(lista, list):
        raise TypeError("Debe ser una lista valida")

    def aux_pila(l):
        if len(l) == 0:
            return []
        return l[-1:] + aux_pila(l[:-1])

    def aux_cola(l, invertida):
        if len(l) == 0:
            return invertida
        invertida.append(l[-1])
        return aux_cola((l[:-1]), invertida)

    return aux_cola(lista, [])

if __name__ == '__main__':
    print(invertir([1, 2, 3, 4]))