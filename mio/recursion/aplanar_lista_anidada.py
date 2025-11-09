def aplanar(L):
    def aux_pila(L):
        print(f"aux_pila({L})")
        if L == []:
            return L
        elif type(L[0]) != list:
            return [L[0]] + aux_pila(L[1:])
        else:
            return aux_pila(L[0]) + aux_pila(L[1:])

    if type(L) != list:
        raise Exception("L debe ser una lista.")
    return aux_pila(L)