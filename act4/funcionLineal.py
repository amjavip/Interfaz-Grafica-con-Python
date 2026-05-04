import customtkinter as ctk
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox

# Configuración de apariencia
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Crear ventana principal
app = ctk.CTk()
app.title("Generador de Funciones Lineales")
app.geometry("400x300")


# Función para graficar
def graficar():
    try:
        # Obtener valores
        m = float(entry_m.get())
        b = float(entry_b.get())

        # Generar valores de x
        x = np.linspace(-10, 10, 100)
        y = m * x + b

        # Graficar
        plt.figure()
        plt.plot(x, y, label=f"f(x) = {m}x + {b}")
        plt.axhline(0)
        plt.axvline(0)
        plt.grid(True)
        plt.legend()
        plt.title("Función Lineal")
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Ingresa valores numéricos válidos para m y b")


# Título
titulo = ctk.CTkLabel(app, text="f(x) = mx + b", font=("Arial", 20))
titulo.pack(pady=10)

# Input pendiente m
label_m = ctk.CTkLabel(app, text="Pendiente (m):")
label_m.pack()
entry_m = ctk.CTkEntry(app)
entry_m.pack(pady=5)

# Input término b
label_b = ctk.CTkLabel(app, text="Término independiente (b):")
label_b.pack()
entry_b = ctk.CTkEntry(app)
entry_b.pack(pady=5)

# Botón graficar
btn = ctk.CTkButton(app, text="Graficar función", command=graficar)
btn.pack(pady=20)

# Ejecutar app
app.mainloop()
