import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

# -------- CONFIGURACIÓN --------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Funciones Lineales PRO")
app.geometry("900x500")

# -------- FRAME PRINCIPAL --------
frame_main = ctk.CTkFrame(app)
frame_main.pack(fill="both", expand=True, padx=10, pady=10)

# -------- PANEL IZQUIERDO --------
panel_left = ctk.CTkFrame(frame_main, width=250)
panel_left.pack(side="left", fill="y", padx=10, pady=10)

titulo = ctk.CTkLabel(panel_left, text="f(x) = mx + b", font=("Arial", 20, "bold"))
titulo.pack(pady=15)

# Inputs
entry_m = ctk.CTkEntry(panel_left, placeholder_text="Pendiente (m)")
entry_m.pack(pady=8)

entry_b = ctk.CTkEntry(panel_left, placeholder_text="Término (b)")
entry_b.pack(pady=8)

entry_x1 = ctk.CTkEntry(panel_left, placeholder_text="X inicio")
entry_x1.pack(pady=8)

entry_x2 = ctk.CTkEntry(panel_left, placeholder_text="X fin")
entry_x2.pack(pady=8)

ecuacion_label = ctk.CTkLabel(panel_left, text="")
ecuacion_label.pack(pady=10)

# -------- PANEL DERECHO (GRÁFICA) --------
panel_right = ctk.CTkFrame(frame_main)
panel_right.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# Figura matplotlib
fig, ax = plt.subplots(figsize=(5, 4))
fig.patch.set_facecolor("#1e1e1e")  # negro carbón
ax.set_facecolor("#1e1e1e")

canvas = FigureCanvasTkAgg(fig, master=panel_right)
canvas.get_tk_widget().pack(fill="both", expand=True)


# -------- FUNCIÓN --------
def graficar():
    try:
        m = float(entry_m.get())
        b = float(entry_b.get())
        x1 = float(entry_x1.get())
        x2 = float(entry_x2.get())

        if x1 >= x2:
            raise ValueError()

        x = np.linspace(x1, x2, 300)
        y = m * x + b

        ax.clear()

        # Estilo oscuro
        ax.set_facecolor("#1e1e1e")
        ax.plot(x, y, linewidth=2)
        ax.axhline(0)
        ax.axvline(0)
        ax.grid(True, alpha=0.3)

        ax.set_title("Gráfica", color="white")
        ax.tick_params(colors="white")

        for spine in ax.spines.values():
            spine.set_color("white")

        ecuacion_label.configure(text=f"f(x) = {m}x + {b}")

        canvas.draw()

    except:
        messagebox.showerror("Error", "Datos inválidos")


# Botón
btn = ctk.CTkButton(panel_left, text="Graficar", command=graficar, height=40)
btn.pack(pady=15)
import customtkinter as ctk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox

# -------- CONFIGURACIÓN --------
ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("Funciones Lineales")
app.geometry("900x500")
app.configure(fg_color="#0d0d0d")  # fondo negro carbón

# -------- FRAME PRINCIPAL --------
frame_main = ctk.CTkFrame(app, fg_color="#0d0d0d")
frame_main.pack(fill="both", expand=True, padx=10, pady=10)

# -------- PANEL IZQUIERDO --------
panel_left = ctk.CTkFrame(frame_main, fg_color="#1a1a1a", corner_radius=15)
panel_left.pack(side="left", fill="y", padx=10, pady=10)

titulo = ctk.CTkLabel(
    panel_left,
    text="f(x) = mx + b",
    font=("Consolas", 20, "bold"),
    text_color="#00ff88",
)
titulo.pack(pady=20)


# Inputs estilo terminal
def crear_input(placeholder):
    return ctk.CTkEntry(
        panel_left,
        placeholder_text=placeholder,
        fg_color="#0d0d0d",
        text_color="#00ff88",
        border_color="#00ff88",
    )


entry_m = crear_input("Pendiente (m)")
entry_m.pack(pady=8)

entry_b = crear_input("Término (b)")
entry_b.pack(pady=8)

entry_x1 = crear_input("X inicio")
entry_x1.pack(pady=8)

entry_x2 = crear_input("X fin")
entry_x2.pack(pady=8)

ecuacion_label = ctk.CTkLabel(
    panel_left, text="", text_color="#00cc66", font=("Consolas", 14)
)
ecuacion_label.pack(pady=10)

# -------- PANEL DERECHO --------
panel_right = ctk.CTkFrame(frame_main, fg_color="#1a1a1a", corner_radius=15)
panel_right.pack(side="right", fill="both", expand=True, padx=10, pady=10)

# -------- FIGURA --------
fig, ax = plt.subplots(figsize=(5, 4))
fig.patch.set_facecolor("#0d0d0d")
ax.set_facecolor("#0d0d0d")

canvas = FigureCanvasTkAgg(fig, master=panel_right)
canvas.get_tk_widget().pack(fill="both", expand=True)


# -------- FUNCIÓN --------
def graficar():
    try:
        m = float(entry_m.get())
        b = float(entry_b.get())
        x1 = float(entry_x1.get())
        x2 = float(entry_x2.get())

        if x1 >= x2:
            raise ValueError()

        x = np.linspace(x1, x2, 300)
        y = m * x + b

        ax.clear()

        # Estilo negro + verde
        ax.set_facecolor("#0d0d0d")
        ax.plot(x, y, color="#00ff88", linewidth=2)

        ax.axhline(0, color="#00cc66")
        ax.axvline(0, color="#00cc66")

        ax.grid(True, color="#1a1a1a")

        ax.set_title("Gráfica", color="#00ff88")
        ax.tick_params(colors="#00ff88")

        for spine in ax.spines.values():
            spine.set_color("#00ff88")

        ecuacion_label.configure(text=f"f(x) = {m}x + {b}")

        canvas.draw()

    except:
        messagebox.showerror("Error", "Datos inválidos")


# -------- BOTÓN --------
btn = ctk.CTkButton(
    panel_left,
    text="Graficar",
    command=graficar,
    fg_color="#00ff88",
    text_color="black",
    hover_color="#00cc66",
    height=40,
)
btn.pack(pady=20)

# -------- RUN --------
app.mainloop()
