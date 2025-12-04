def cargar_padron(ruta):
    padron = open(ruta, 'r')
    datos = []

    llaves = ["CEDULA", "CODELEC", "SEXO", "FECHACADUC",
              "JUNTA", "NOMBRE", "APELLIDO1", "APELLIDO2"]

    for linea in padron:
        persona = [dato.strip() for dato in linea.split(",")]
        datos.append(dict(zip(llaves, persona)))

    padron.close()
    return datos

def guardar_filtrado(padron, campo, criterio, archivo_salida):
    salida = open(archivo_salida, "w")

    for persona in padron:
        if persona[campo].startswith(criterio):
            linea = ",".join([
                persona["CEDULA"], persona["CODELEC"], persona["SEXO"],
                persona["FECHACADUC"], persona["JUNTA"],
                persona["NOMBRE"], persona["APELLIDO1"], persona["APELLIDO2"]
            ])
            salida.write(linea + "\n")

    salida.close()

def pedir_opcion():
    print("Elija el criterio para filtrar el archivo:")
    print("1. Cédula")
    print("2. Código electoral")
    print("3. Sexo")
    print("4. Fecha de caducidad")
    print("5. Código de junta")
    print("6. Nombre")
    print("7. Apellido 1")
    print("8. Apellido 2")

    while True:
        opcion = input("Seleccione una opción del 1 al 8: ")
        if opcion.isdigit() and 1 <= int(opcion) <= 8:
            return opcion
        print("Opción inválida. Intente de nuevo.")

def main():
    print("Filtrado del padrón electoral de Costa Rica")
    while True:
        ruta = input("Indique el nombre del archivo del padrón electoral: ")
        try:
            if ruta.strip():
                with open(ruta, 'r'):
                    break
        except FileNotFoundError:
            pass
        print("Nombre de archivo no válido o archivo no existe. Intente de nuevo.")

    opcion = pedir_opcion()

    criterios = {
        "1": "CEDULA",
        "2": "CODELEC",
        "3": "SEXO",
        "4": "FECHACADUC",
        "5": "JUNTA",
        "6": "NOMBRE",
        "7": "APELLIDO1",
        "8": "APELLIDO2"
    }

    campo = criterios[opcion]
    texto = input(f"Indique ({campo}) para filtrar: ").strip()
    archivo_salida = input("Indique el nombre del archivo de salida: ").strip()

    print("Procesando archivo...")

    padron = cargar_padron(ruta)
    guardar_filtrado(padron, campo, texto, archivo_salida)

    print(f"Proceso finalizado. Archivo generado: {archivo_salida}")


if __name__ == '__main__':
    main()