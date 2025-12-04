def main():
    # pedir nombre del archivo .py
    archivo = input("Introduzca el nombre del archivo .py a procesar: ")
    while archivo[-3:] != ".py":
        archivo = input("ERROR: debe ser un archivo .py válido. \nIntenta de nuevo: ")

    # procesar el archivo .py
    with (open(archivo, "r") as archivo_orig,
          open(archivo[:-3] + "-comments.py", "w") as archivo_com,
          open(archivo[:-3] + "-code.py", "w") as archivo_cod):
        contador_lineas = 0
        for linea in archivo_orig:
            contador_lineas += 1
            if linea[0] == "#": # guardar comentarios
                archivo_com.write(f"{contador_lineas}: {linea}")
            else: # guardar código
                archivo_cod.write(linea)





if __name__ == "__main__":
    main()