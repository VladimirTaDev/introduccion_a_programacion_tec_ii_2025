def cargar_distritos(ruta):
    """
    Función que carga el archivo de distritos y lo empaca en un diccionario.
    Entradas: nombre del archivo que está en la carpeta raíz.
    Salidas: un diccionario con los distritos accesibles por el código electoral.
    """
    distritos = open(ruta,'r')
    llaves_dist = ["PROVINCIA", "CANTON", "DISTRITO"]
    # Diccionario con el lugar para votar. Buscar por código electoral.
    lugar_de_votacion = {}

    # Crea diccionario con los lugares de votación.
    for linea in distritos:
        localidad = [dato.strip() for dato in linea.split(",")]
        lugar_de_votacion[localidad[0]] = dict(zip(llaves_dist, localidad[1:]))
    distritos.close()
    return lugar_de_votacion

def cargar_padron(ruta):
    """
    Función que carga el archivo del padrón electoral y lo empaca en un diccionario.
    Entradas: nombre del archivo que está en la carpeta raíz.
    Salidas: un diccionario con los votantes accesibles por el número de cédula.
    """
    padron_electoral = {}
    padron = open(ruta, 'r')
    llaves_padron = ["CODELEC", "SEXO", "FECHACADUC", "JUNTA", "NOMBRE", "APELLIDO1", "APELLIDO2"]
    for linea in padron:
        persona = [dato.strip() for dato in linea.split(",")]
        padron_electoral[persona[0]] = dict(zip(llaves_padron, persona[1:]))
    padron.close()
    return padron_electoral

def main():
    """
    Función principal que une y procesa la búsqueda electoral.
    Entradas:
    - Base electoral (str, input),
    - Cédula de la persona buscada: (int, input) positivo.
    Salidas:
    - (print en consola): Información de la persona buscada.
    """
    print("Búsqueda electoral de Costa Rica")

    # Pide los nombres de archivos de datos y chequea que sean válidos.
    while True:
        distritos_ruta = input("Indique el nombre del archivo de distritos: ")
        try:
            if isinstance(distritos_ruta, str) and distritos_ruta.strip():
                with open(distritos_ruta, 'r'):
                    break
        except FileNotFoundError:
            pass
        print("Nombre de archivo no válido o archivo no existe. Intente de nuevo.")

    while True:
        padron_ruta = input("Indique el nombre del archivo del padrón electoral: ")
        try:
            if isinstance(padron_ruta, str) and padron_ruta.strip():
                with open(padron_ruta, 'r'):
                    break
        except FileNotFoundError:
            pass
        print("Nombre de archivo no válido o archivo no existe. Intente de nuevo.")

    distritos = cargar_distritos(distritos_ruta)
    padron = cargar_padron(padron_ruta)

    # Realiza la búsqueda de la persona votante.
    while True:
        cedula = input("Indique el número de cédula de la persona votante que desea consultar \n o escriba 'salir': ")
        # Buscar persona e imprimir el resultado
        if cedula.strip().isdigit() and isinstance(int(cedula.strip()), int) and int(cedula.strip()) > 0:
            persona = padron.get(cedula.strip())
            if persona:
                lugar = distritos.get(persona['CODELEC'])

                print(f"Código electoral: {persona['CODELEC']}\n"
                      f"Sexo: {persona['SEXO']}\n"
                      f"Caducidad: {persona['FECHACADUC']}\n"
                      f"Junta: {persona['JUNTA']}\n"
                      f"Nombre: {persona['NOMBRE']}\n"
                      f"Apellido 1: {persona['APELLIDO1']}\n"
                      f"Apellido 2: {persona['APELLIDO2']}\n"
                      f"Lugar de votación:\n"
                      f"    Provincia: {lugar['PROVINCIA']}\n"
                      f"    Cantón: {lugar['CANTON']}\n"
                      f"    Distrito: {lugar['DISTRITO']}")
            else:
                print("No se encontró la persona.")

        # Salir.
        elif cedula.strip() == 'salir':
            break

        else:
            print("ERROR: La cédula debe ser un entero positivo o la palabra 'salir' para terminar.")

if __name__ == '__main__':
    main()