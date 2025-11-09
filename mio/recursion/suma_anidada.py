def suma_anidada(L):
    def aux_pila(L):
        print(f"aux_pila({L})")
        if L == []:
            return 0
        elif type(L[0]) in (int, float):
            return L[0] + aux_pila(L[1:])
        elif type(L[0]) == list:
            return aux_pila(L[0]) + aux_pila(L[1:])
        else:
            return aux_pila(L[1:])

    if type(L) != list:
        raise Exception("L debe ser una lista.")
    return aux_pila(L)