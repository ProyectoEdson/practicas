import tkinter as tk
from tkinter import simpledialog, messagebox

def extraer_subcadena():
    cadena = simpledialog.askstring("Extraer subcadena", "Ingrese una cadena:")
    while not cadena:
        messagebox.showwarning("Error", "La cadena no puede estar vacía.")
        cadena = simpledialog.askstring("Extraer subcadena", "Ingrese una cadena:")
    
    while True:
        try:
            posicion = simpledialog.askinteger("Extraer subcadena", 
                                              f"Ingrese la posición del carácter que desea extraer (1-{len(cadena)}):")
            if posicion is None:  # Si el usuario cancela
                return
            posicion -= 1  # Ajustar para que la posición sea 0-indexada
            if 0 <= posicion < len(cadena):
                messagebox.showinfo("Resultado", 
                                   f"El carácter en la posición {posicion+1} es: {cadena[posicion]}")
                break
            else:
                messagebox.showerror("Error", 
                                   f"Posición fuera del rango. Debe ser entre 1 y {len(cadena)}.")
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un número válido.")
    
    while True:
        try:
            numero_de_caracteres = simpledialog.askinteger("Extraer subcadena", 
                                                          "Ingrese el número de caracteres que desea extraer:")
            if numero_de_caracteres is None:  # Si el usuario cancela
                return
            if numero_de_caracteres <= 0:
                messagebox.showwarning("Error", "El número debe ser mayor que 0.")
                continue
            if posicion + numero_de_caracteres <= len(cadena):
                subcadena = cadena[posicion:posicion + numero_de_caracteres]
                messagebox.showinfo("Resultado", f"La subcadena es: {subcadena}")
                break
            else:
                messagebox.showerror("Error", 
                                    "No se puede extraer la subcadena: se pasa del final de la cadena.")
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un número válido.")

def calcular_longitud():
    lenCadena = simpledialog.askstring("Calcular longitud", "Ingrese una cadena para ver su longitud:")
    while not lenCadena:
        messagebox.showwarning("Error", "La cadena no puede estar vacía.")
        lenCadena = simpledialog.askstring("Calcular longitud", "Ingrese una cadena para ver su longitud:")
    messagebox.showinfo("Resultado", f"La longitud de la cadena es: {len(lenCadena)}")

def concatenar_cadenas():
    cadena1 = simpledialog.askstring("Concatenar cadenas", "Ingrese la primera cadena:")
    while not cadena1:
        messagebox.showwarning("Error", "La cadena no puede estar vacía.")
        cadena1 = simpledialog.askstring("Concatenar cadenas", "Ingrese la primera cadena:")
    
    cadena2 = simpledialog.askstring("Concatenar cadenas", "Ingrese la segunda cadena:")
    while not cadena2:
        messagebox.showwarning("Error", "La cadena no puede estar vacía.")
        cadena2 = simpledialog.askstring("Concatenar cadenas", "Ingrese la segunda cadena:")
    
    cadena3 = simpledialog.askstring("Concatenar cadenas", "Ingrese la tercera cadena:")
    while not cadena3:
        messagebox.showwarning("Error", "La cadena no puede estar vacía.")
        cadena3 = simpledialog.askstring("Concatenar cadenas", "Ingrese la tercera cadena:")
    
    cadenaConcatenada = cadena1 + cadena2 + cadena3
    messagebox.showinfo("Resultado", 
                       f"La cadena concatenada es: {cadenaConcatenada}\nY su longitud es: {len(cadenaConcatenada)}")

def buscar_caracter():
    cadena = simpledialog.askstring("Buscar caracter", "Ingrese una cadena para buscar caracteres:")
    while not cadena:
        messagebox.showwarning("Error", "La cadena no puede estar vacía.")
        cadena = simpledialog.askstring("Buscar caracter", "Ingrese una cadena para buscar caracteres:")
    
    caracter = simpledialog.askstring("Buscar caracter", "Ingrese el caracter que desea buscar:")
    while not caracter:
        messagebox.showwarning("Error", "El caracter no puede estar vacío.")
        caracter = simpledialog.askstring("Buscar caracter", "Ingrese el caracter que desea buscar:")
    
    if caracter in cadena:
        messagebox.showinfo("Resultado", "El caracter se encuentra en la cadena")
    else:
        messagebox.showinfo("Resultado", "El caracter no se encuentra en la cadena")

def mostrar_menu():
    root = tk.Tk()
    root.title("Menú de Operaciones con Cadenas")
    root.geometry("400x300")
    
    label = tk.Label(root, text="Seleccione una operación:", font=("Arial", 14))
    label.pack(pady=20)
    
    btn_frame = tk.Frame(root)
    btn_frame.pack(expand=True)
    
    btn1 = tk.Button(btn_frame, text="1. Extraer subcadena", command=extraer_subcadena, width=20, height=2)
    btn1.pack(pady=5)
    
    btn2 = tk.Button(btn_frame, text="2. Calcular longitud", command=calcular_longitud, width=20, height=2)
    btn2.pack(pady=5)
    
    btn3 = tk.Button(btn_frame, text="3. Concatenar cadenas", command=concatenar_cadenas, width=20, height=2)
    btn3.pack(pady=5)
    
    btn4 = tk.Button(btn_frame, text="4. Buscar caracter", command=buscar_caracter, width=20, height=2)
    btn4.pack(pady=5)
    
    btn_salir = tk.Button(root, text="Salir", command=root.destroy, width=15, height=1)
    btn_salir.pack(pady=10)
    
    root.mainloop()

if __name__ == "__main__":
    mostrar_menu()