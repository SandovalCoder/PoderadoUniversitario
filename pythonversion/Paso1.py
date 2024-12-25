import tkinter as tk
import pythonversion.Ponderado as Ponderado

# Ventana principal para ingresar el nombre
def main():
    ventana = tk.Tk()
    ventana.title("Nombre del universitario")

    # Centrar ventana
    ancho_ventana = 500
    alto_ventana = 200
    ancho_pantalla = ventana.winfo_screenwidth()
    alto_pantalla = ventana.winfo_screenheight()
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - alto_ventana) // 2
    ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    # Crear input y botón
    etiqueta = tk.Label(ventana, text="Ingrese su nombre:")
    etiqueta.pack(pady=10)

    entrada = tk.Entry(ventana)
    entrada.pack(pady=5)

    def continuar():
        nombre = entrada.get()
        if not nombre.strip():
            tk.messagebox.showerror("Error", "El nombre no puede estar vacío.")
            return
        ventana.destroy()
        Ponderado.abrir_nueva_ventana(nombre)

    boton = tk.Button(ventana, text="Continuar", command=continuar)
    boton.pack(pady=10)

    ventana.mainloop()


if __name__ == "__main__":
    main()
