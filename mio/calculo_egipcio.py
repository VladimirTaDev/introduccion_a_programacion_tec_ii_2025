NUMEROS_EGIPCIOS = {"|":1, "U": 10, "?": 100, "*": 1000, "i": 10000, "&": 100000, "Y": 1000000}
SIMBOLOS = "|U?*i&Y"

def decimal_egipcio(n):
    global SIMBOLOS
    i = 0
    resultado = ""

    if type(n):
        if type(n) != int or n not in range(1, 10000000):
            raise Exception("n debe ser entero válido")
        
        while n != 0:
            digito = n % 10
            n //= 10

            resultado = SIMBOLOS[i] * digito + resultado
            i += 1       
        return resultado


if __name__ == "__main__":
    print(decimal_egipcio(2027475))

