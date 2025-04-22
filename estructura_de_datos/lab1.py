def extraer_subcadena():
    cadena = input("Ingrese una cadena: ")
    while not cadena:
        print("⚠️ La cadena no puede estar vacía.")
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

def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Extraer subcadena")
        print("2. Calcular longitud de cadena")
        print("3. Concatenar cadenas")
        print("4. Buscar caracter en cadena")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == '1':
            extraer_subcadena()
        elif opcion == '2':
            calcular_longitud()
        elif opcion == '3':
            concatenar_cadenas()
        elif opcion == '4':
            buscar_caracter()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")
if __name__ == "__main__":
    main()

