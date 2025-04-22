
def calcular_longitud():
    lenCadena = input("Ingrese una cadena para ver su longitud: ")
    while not lenCadena:
        print(" La cadena no puede estar vacía.")
        lenCadena = input("Ingrese una cadena para ver su longitud: ")
    lenCadena = len(lenCadena)
    print("La longitud de la cadena es: ", lenCadena)
def concatenar_cadenas():
    cadena1 = input("Ingrese la primera cadena: ")
    while not cadena1:
        print(" La cadena no puede estar vacía.")
        cadena1 = input("Ingrese la primera cadena: ")
    cadena2 = input("Ingrese la segunda cadena: ")
    while not cadena2:
        print(" La cadena no puede estar vacía.")
        cadena2 = input("Ingrese la segunda cadena: ")
    cadena3 = input("Ingrese la tercera cadena: ")
    while not cadena3:
        print(" La cadena no puede estar vacía.")
        cadena3 = input("Ingrese la tercera cadena: ")
    # Validar que las cadenas no estén vacías
    cadenaConcatenada = cadena1 + cadena2 + cadena3
    print("La cadena concatenada es: ", cadenaConcatenada, "y su longitud es: ", len(cadenaConcatenada))
def buscar_caracter():
    cadena = input("Ingrese una cadena que desea buscar caracteres: ")
    while not cadena:
        print(" La cadena no puede estar vacía.")
        cadena = input("Ingrese una cadena que desea buscar caracteres: ")
    caracter = input("Ingrese el caracter que desea buscar: ")
    while not caracter:
        print(" El caracter no puede estar vacío.")
        caracter = input("Ingrese el caracter que desea buscar: ")
    if caracter in cadena:
        print("El caracter se encuentra en la cadena")
    else:
        print("El caracter no se encuentra en la cadena")
def reemplazar_cadena():
    cadena = input("Ingrese una cadena: ")
    while not cadena:
        print(" La cadena no puede estar vacía.")
        cadena = input("Ingrese una cadena: ")

    viejo = input("Ingrese la subcadena a reemplazar: ")
    nuevo = input("Ingrese la nueva subcadena: ")

    if viejo in cadena:
        cadena_reemplazada = cadena.replace(viejo, nuevo)
        print("Cadena original:", cadena)
        print("Cadena reemplazada", cadena_reemplazada)
    else:
        print("La subcadena ", viejo, "no se encuentra en la cadena original.")

def extraer_subcadena():
    cadena = input("Ingrese una cadena: ")
    while not cadena:
        print("La cadena no puede estar vacía.")
        cadena = input("Ingrese una cadena: ")

    while True:
        try:
            posicion = int(input("Ingrese la posición del carácter que desea extraer: "))
            posicion = posicion - 1  # Ajustar para que la posición sea 0-indexada
            if 0 <= posicion < len(cadena):
                print(f"El carácter en la posición {posicion+1} es: {cadena[posicion]}")
                break
            else:
                print(f" Posición fuera del rango. Debe ser entre 1 y {len(cadena)}.")
        except ValueError:
            print("Debe ingresar un número válido.")

    while True:
        try:
            numero_de_caracteres = int(input("Ingrese el número de caracteres que desea extraer: "))
            if numero_de_caracteres <= 0:
                print(" El número debe ser mayor que 0.")
                continue
            if posicion  + numero_de_caracteres <= len(cadena):
                subcadena = cadena[posicion:posicion + numero_de_caracteres]
                print(f"La subcadena es: {subcadena}")
                break
            else:
                print("No se puede extraer la subcadena: se pasa del final de la cadena.")
        except ValueError:
            print("Debe ingresar un número válido.")
def main():
    while True:
        print("1. Calcular longitud de una cadena")
        print("2. Concatenar cadenas")
        print("3. Buscar un caracter en una cadena")
        print("4. Reemplazar una subcadena por otra")
        print("5. Extraer una subcadena")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            calcular_longitud()
        elif opcion == "2":
            concatenar_cadenas()
        elif opcion == "3":
            buscar_caracter()
        elif opcion == "4":
            reemplazar_cadena()
        elif opcion == "5":
            extraer_subcadena()
        elif opcion == "6":
            break
        else:
            print("Opción no válida, intente nuevamente.")
if __name__ == "__main__":
    main()

