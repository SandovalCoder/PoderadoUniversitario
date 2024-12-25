import tkinter as tk
import pythonversion.Dato as Dato
from tkinter import messagebox

def abrir_nueva_ventana(nombre):
    nueva_ventana = tk.Tk()
    nueva_ventana.title("Calculadora de Ponderado")

    # Centrar ventana
    ancho_ventana = 600
    alto_ventana = 500
    ancho_pantalla = nueva_ventana.winfo_screenwidth()
    alto_pantalla = nueva_ventana.winfo_screenheight()
    x = (ancho_pantalla - ancho_ventana) // 2
    y = (alto_pantalla - alto_ventana) // 2
    nueva_ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    etiqueta = tk.Label(nueva_ventana, text=f"Bienvenido, {nombre}!")
    etiqueta.pack(pady=10)

    datos = []

    # Frame para inputs
    frame_inputs = tk.Frame(nueva_ventana)
    frame_inputs.pack(pady=10)

    # Etiqueta y entrada para nota
    tk.Label(frame_inputs, text="Ingrese la nota (0-20):").grid(row=0, column=0, padx=5, pady=5)
    entrada_nota = tk.Entry(frame_inputs)
    entrada_nota.grid(row=0, column=1, padx=5, pady=5)

    # Etiqueta y entrada para peso
    tk.Label(frame_inputs, text="Ingrese el peso (%):").grid(row=0, column=2, padx=5, pady=5)
    entrada_peso = tk.Entry(frame_inputs)
    entrada_peso.grid(row=0, column=3, padx=5, pady=5)

    # Frame para botones
    frame_buttons = tk.Frame(nueva_ventana)
    frame_buttons.pack(pady=5)

    # Tabla para datos
    tabla = tk.Frame(nueva_ventana)
    tabla.pack(pady=10)

    def actualizar_tabla():
        for widget in tabla.winfo_children():
            widget.destroy()

        # Encabezados
        tk.Label(tabla, text="Nota").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(tabla, text="Peso (%)").grid(row=0, column=1, padx=5, pady=5)

        # Filas de datos
        for i, dato in enumerate(datos):
            tk.Label(tabla, text=dato.notadelcurso).grid(row=i+1, column=0, padx=5, pady=5)
            tk.Label(tabla, text=dato.pesodelasnotas).grid(row=i+1, column=1, padx=5, pady=5)

        # Total de pesos
        total_peso = sum(d.pesodelasnotas for d in datos)
        tk.Label(tabla, text="Total Peso").grid(row=len(datos)+1, column=0, padx=5, pady=5)
        tk.Label(tabla, text=f"{total_peso} %").grid(row=len(datos)+1, column=1, padx=5, pady=5)

    def agregar_nota():
        try:
            nota = float(entrada_nota.get())
            peso = float(entrada_peso.get())

            if nota < 0 or nota > 20:
                raise ValueError("La nota debe estar entre 0 y 20.")
            if peso <= 0 or peso > 100:
                raise ValueError("El peso debe estar entre 0 y 100.")
            if sum(d.pesodelasnotas for d in datos) + peso > 100:
                raise ValueError("El peso total no puede exceder 100%.")

            datos.append(Dato(nota, peso))
            entrada_nota.delete(0, tk.END)
            entrada_peso.delete(0, tk.END)
            actualizar_tabla()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    tk.Button(frame_buttons, text="Agregar nota", command=agregar_nota).grid(row=0, column=0, padx=5, pady=5)

    def calcular_promedio_final():
        promedio = Dato.calcular_promedio_final(datos)
        messagebox.showinfo("Promedio Final", f"El promedio ponderado es: {promedio:.2f}")

    tk.Button(frame_buttons, text="Calcular promedio final", command=calcular_promedio_final).grid(row=0, column=1, padx=5, pady=5)

    actualizar_tabla()
    nueva_ventana.mainloop()
