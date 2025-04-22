import tkinter as tk
from tkinter import messagebox, scrolledtext

def calcular_longitud_gui(root, frame_principal):
    # Limpiar el frame principal
    for widget in frame_principal.winfo_children():
        widget.destroy()
    
    # Crear los widgets necesarios
    tk.Label(frame_principal, text="Ingrese una cadena para ver su longitud:").pack(pady=10)
    
    entrada = tk.Entry(frame_principal, width=40)
    entrada.pack(pady=10)
    entrada.focus_set()
    
    resultado_text = tk.StringVar()
    resultado_label = tk.Label(frame_principal, textvariable=resultado_text)
    resultado_label.pack(pady=10)
    
    def calcular():
        texto = entrada.get()
        if not texto:
            messagebox.showwarning("Advertencia", "La cadena no puede estar vacía.")
            return
        
        longitud = len(texto)
        resultado_text.set(f"La longitud de la cadena es: {longitud}")
    
    botones_frame = tk.Frame(frame_principal)
    botones_frame.pack(pady=10)
    
    tk.Button(botones_frame, text="Calcular", command=calcular).pack(side=tk.LEFT, padx=5)
    tk.Button(botones_frame, text="Volver al Menú", command=lambda: mostrar_menu(root, frame_principal)).pack(side=tk.LEFT, padx=5)

def concatenar_cadenas_gui(root, frame_principal):
    # Limpiar el frame principal
    for widget in frame_principal.winfo_children():
        widget.destroy()
    
    # Crear los widgets necesarios
    tk.Label(frame_principal, text="Ingrese la primera cadena:").pack(pady=5)
    entrada1 = tk.Entry(frame_principal, width=40)
    entrada1.pack(pady=5)
    entrada1.focus_set()
    
    tk.Label(frame_principal, text="Ingrese la segunda cadena:").pack(pady=5)
    entrada2 = tk.Entry(frame_principal, width=40)
    entrada2.pack(pady=5)
    
    tk.Label(frame_principal, text="Ingrese la tercera cadena:").pack(pady=5)
    entrada3 = tk.Entry(frame_principal, width=40)
    entrada3.pack(pady=5)
    
    resultado_text = tk.StringVar()
    resultado_label = tk.Label(frame_principal, textvariable=resultado_text, wraplength=400)
    resultado_label.pack(pady=10)
    
    def concatenar():
        cadena1 = entrada1.get()
        cadena2 = entrada2.get()
        cadena3 = entrada3.get()
        
        if not cadena1 or not cadena2 or not cadena3:
            messagebox.showwarning("Advertencia", "Las cadenas no pueden estar vacías.")
            return
        
        concatenada = cadena1 + cadena2 + cadena3
        resultado_text.set(f"La cadena concatenada es: {concatenada}\ny su longitud es: {len(concatenada)}")
    
    botones_frame = tk.Frame(frame_principal)
    botones_frame.pack(pady=10)
    
    tk.Button(botones_frame, text="Concatenar", command=concatenar).pack(side=tk.LEFT, padx=5)
    tk.Button(botones_frame, text="Volver al Menú", command=lambda: mostrar_menu(root, frame_principal)).pack(side=tk.LEFT, padx=5)

def buscar_caracter_gui(root, frame_principal):
    # Limpiar el frame principal
    for widget in frame_principal.winfo_children():
        widget.destroy()
    
    # Crear los widgets necesarios
    tk.Label(frame_principal, text="Ingrese una cadena que desea buscar caracteres:").pack(pady=10)
    
    entrada_cadena = tk.Entry(frame_principal, width=40)
    entrada_cadena.pack(pady=5)
    entrada_cadena.focus_set()
    
    tk.Label(frame_principal, text="Ingrese el caracter que desea buscar:").pack(pady=5)
    entrada_caracter = tk.Entry(frame_principal, width=10)
    entrada_caracter.pack(pady=5)
    
    resultado_text = tk.StringVar()
    resultado_label = tk.Label(frame_principal, textvariable=resultado_text)
    resultado_label.pack(pady=10)
    
    def buscar():
        cadena = entrada_cadena.get()
        caracter = entrada_caracter.get()
        
        if not cadena:
            messagebox.showwarning("Advertencia", "La cadena no puede estar vacía.")
            return
        
        if not caracter:
            messagebox.showwarning("Advertencia", "El caracter no puede estar vacío.")
            return
        
        if caracter in cadena:
            resultado_text.set("El caracter se encuentra en la cadena")
        else:
            resultado_text.set("El caracter no se encuentra en la cadena")
    
    botones_frame = tk.Frame(frame_principal)
    botones_frame.pack(pady=10)
    
    tk.Button(botones_frame, text="Buscar", command=buscar).pack(side=tk.LEFT, padx=5)
    tk.Button(botones_frame, text="Volver al Menú", command=lambda: mostrar_menu(root, frame_principal)).pack(side=tk.LEFT, padx=5)

def reemplazar_cadena_gui(root, frame_principal):
    # Limpiar el frame principal
    for widget in frame_principal.winfo_children():
        widget.destroy()
    
    # Crear los widgets necesarios
    tk.Label(frame_principal, text="Ingrese una cadena:").pack(pady=5)
    entrada_cadena = tk.Entry(frame_principal, width=40)
    entrada_cadena.pack(pady=5)
    entrada_cadena.focus_set()
    
    tk.Label(frame_principal, text="Ingrese la subcadena a reemplazar:").pack(pady=5)
    entrada_viejo = tk.Entry(frame_principal, width=40)
    entrada_viejo.pack(pady=5)
    
    tk.Label(frame_principal, text="Ingrese la nueva subcadena:").pack(pady=5)
    entrada_nuevo = tk.Entry(frame_principal, width=40)
    entrada_nuevo.pack(pady=5)
    
    resultado_frame = tk.Frame(frame_principal)
    resultado_frame.pack(pady=10, fill=tk.BOTH, expand=True)
    
    resultado_text = scrolledtext.ScrolledText(resultado_frame, width=40, height=5, wrap=tk.WORD)
    resultado_text.pack(fill=tk.BOTH, expand=True)
    
    def reemplazar():
        cadena = entrada_cadena.get()
        viejo = entrada_viejo.get()
        nuevo = entrada_nuevo.get()
        
        if not cadena:
            messagebox.showwarning("Advertencia", "La cadena no puede estar vacía.")
            return
        
        resultado_text.delete(1.0, tk.END)
        
        if viejo in cadena:
            cadena_reemplazada = cadena.replace(viejo, nuevo)
            resultado_text.insert(tk.END, f"Cadena original: {cadena}\nCadena reemplazada: {cadena_reemplazada}")
        else:
            resultado_text.insert(tk.END, f"La subcadena '{viejo}' no se encuentra en la cadena original.")
    
    botones_frame = tk.Frame(frame_principal)
    botones_frame.pack(pady=10)
    
    tk.Button(botones_frame, text="Reemplazar", command=reemplazar).pack(side=tk.LEFT, padx=5)
    tk.Button(botones_frame, text="Volver al Menú", command=lambda: mostrar_menu(root, frame_principal)).pack(side=tk.LEFT, padx=5)

def extraer_subcadena_gui(root, frame_principal):
    # Limpiar el frame principal
    for widget in frame_principal.winfo_children():
        widget.destroy()
    
    # Crear los widgets necesarios
    tk.Label(frame_principal, text="Ingrese una cadena:").pack(pady=5)
    entrada_cadena = tk.Entry(frame_principal, width=40)
    entrada_cadena.pack(pady=5)
    entrada_cadena.focus_set()
    
    posicion_frame = tk.Frame(frame_principal)
    posicion_frame.pack(pady=5)
    tk.Label(posicion_frame, text="Posición del carácter:").pack(side=tk.LEFT)
    entrada_posicion = tk.Entry(posicion_frame, width=10)
    entrada_posicion.pack(side=tk.LEFT, padx=5)
    
    caracteres_frame = tk.Frame(frame_principal)
    caracteres_frame.pack(pady=5)
    tk.Label(caracteres_frame, text="Número de caracteres:").pack(side=tk.LEFT)
    entrada_caracteres = tk.Entry(caracteres_frame, width=10)
    entrada_caracteres.pack(side=tk.LEFT, padx=5)
    
    resultado_frame = tk.Frame(frame_principal)
    resultado_frame.pack(pady=10, fill=tk.BOTH, expand=True)
    
    resultado_text = scrolledtext.ScrolledText(resultado_frame, width=40, height=5, wrap=tk.WORD)
    resultado_text.pack(fill=tk.BOTH, expand=True)
    
    def extraer():
        cadena = entrada_cadena.get()
        
        if not cadena:
            messagebox.showwarning("Advertencia", "La cadena no puede estar vacía.")
            return
        
        try:
            posicion = int(entrada_posicion.get())
            posicion = posicion - 1  # Ajustar para que la posición sea 0-indexada
            
            if not (0 <= posicion < len(cadena)):
                messagebox.showwarning("Advertencia", f"Posición fuera del rango. Debe ser entre 1 y {len(cadena)}.")
                return
                
            resultado_text.delete(1.0, tk.END)
            resultado_text.insert(tk.END, f"El carácter en la posición {posicion+1} es: {cadena[posicion]}\n")
            
            try:
                numero_caracteres = int(entrada_caracteres.get())
                
                if numero_caracteres <= 0:
                    messagebox.showwarning("Advertencia", "El número debe ser mayor que 0.")
                    return
                
                if posicion + numero_caracteres <= len(cadena):
                    subcadena = cadena[posicion:posicion + numero_caracteres]
                    resultado_text.insert(tk.END, f"La subcadena es: {subcadena}")
                else:
                    resultado_text.insert(tk.END, "No se puede extraer la subcadena: se pasa del final de la cadena.")
            except ValueError:
                messagebox.showwarning("Advertencia", "Debe ingresar un número válido para la cantidad de caracteres.")
                
        except ValueError:
            messagebox.showwarning("Advertencia", "Debe ingresar un número válido para la posición.")
    
    botones_frame = tk.Frame(frame_principal)
    botones_frame.pack(pady=10)
    
    tk.Button(botones_frame, text="Extraer", command=extraer).pack(side=tk.LEFT, padx=5)
    tk.Button(botones_frame, text="Volver al Menú", command=lambda: mostrar_menu(root, frame_principal)).pack(side=tk.LEFT, padx=5)

def mostrar_menu(root, frame_principal):
    # Limpiar el frame principal
    for widget in frame_principal.winfo_children():
        widget.destroy()
    
    # Título
    tk.Label(frame_principal, text="Operaciones con Cadenas", font=("Arial", 14, "bold")).pack(pady=20)
    
    # Botones del menú
    funciones = [
        ("Calcular Longitud", lambda: calcular_longitud_gui(root, frame_principal)),
        ("Concatenar Cadenas", lambda: concatenar_cadenas_gui(root, frame_principal)),
        ("Buscar Carácter", lambda: buscar_caracter_gui(root, frame_principal)),
        ("Reemplazar Cadena", lambda: reemplazar_cadena_gui(root, frame_principal)),
        ("Extraer Subcadena", lambda: extraer_subcadena_gui(root, frame_principal)),
        ("Salir", root.quit)
    ]
    
    for texto, comando in funciones:
        tk.Button(frame_principal, text=texto, width=20, command=comando).pack(pady=5)

def main():
    root = tk.Tk()
    root.title("Manipulación de Cadenas")
    root.geometry("500x500")
    
    # Frame principal
    frame_principal = tk.Frame(root, padx=20, pady=20)
    frame_principal.pack(fill=tk.BOTH, expand=True)
    
    # Mostrar menú principal
    mostrar_menu(root, frame_principal)
    
    root.mainloop()

if __name__ == "__main__":
    main()