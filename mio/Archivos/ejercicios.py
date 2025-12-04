# https://www.youtube.com/watch?v=KKsy1Mdrgq4
import os

def busquedaTexto():
    print("Búsqueda en un archivo de texto.")
    nombreArchivo = input("Escriba el nombre del archivo: ")
    coincidencias = 0
    try:
        with open(nombreArchivo, "r") as archivo:
            busqueda = input("Texto a buscar: ")
            print("\nResultados:")
            for i, linea in enumerate(archivo):
                if busqueda.lower() in linea.lower():
                    print(f"Línea {i + 1}: {linea}", end="")
                    coincidencias += 1
            if coincidencias == 0:
                print("No hubo coincidencias.")
            else:
                print(f"Coincidencias encontradas: {coincidencias}.")
    except OSError as e:
        print(f"Error al acceder el archivo: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


def reemplazarTexto():
    print("Reemplazo en un archivo de texto.")
    nombreArchivo = input("Escriba el nombre del archivo: ")
    reemplazos = 0
    try:
        with open(nombreArchivo, "r") as archivoEntrada, \
             open("__" + nombreArchivo, "w") as archivoSalida:
            busqueda = input("Texto a reemplazar: ")
            reemplazo = input("Texto de reemplazo: ")
            for linea in archivoEntrada:
                if busqueda in linea:
                    linea = linea.replace(busqueda, reemplazo)
                    reemplazos += 1
                archivoSalida.write(linea)
        os.remove(nombreArchivo)
        os.rename("__" + nombreArchivo, nombreArchivo)
        print(f"Se realizaron {reemplazos} reemplazos.")
    except OSError as e:
        print(f"Error al acceder un archivo: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def estadisticasArchivo():
    print("Estadísticas de un archivo de texto.")
    nombreArchivo = input("Escriba el nombre del archivo: ")
    lineas = 0
    caracteres = 0
    palabrasDic = {}
    try:
        with open(nombreArchivo, "r") as archivo:
            rutaCompleta = os.path.abspath(nombreArchivo)
            for linea in archivo:
                lineas += 1
                nuevaLinea = ""
                for caracter in linea:
                    caracteres += 1
                    if caracter.isalpha():
                        nuevaLinea += caracter
                    else:
                        nuevaLinea += " "
                listaPalabras = nuevaLinea.split()
                for palabra in listaPalabras:
                    palabra = palabra.lower()
                    if palabra in palabrasDic:
                        palabrasDic[palabra] += 1
                    else:
                        palabrasDic[palabra] = 1
        top10 = [(v, k) for k, v in palabrasDic.items()]
        top10.sort(reverse = True)
        top10 = top10[:10]
        print(f"Ruta completa: {rutaCompleta}")
        print(f"Cantidad de líneas: {lineas}")
        print(f"Cantidad de caracteres: {caracteres}")
        print("Top 10 de palabras más utilizadas:")
        for i, (cantidad, palabra) in enumerate(top10):
            print(f"{i + 1}. {palabra} ({cantidad})")
    except OSError as e:
        print(f"Error al acceder el archivo: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
