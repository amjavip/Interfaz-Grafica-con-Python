import tkinter as tk
from tkinter import messagebox, ttk


class AppEmpresa:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema Multifuncional - Equipo 5")
        self.root.geometry("600x600")

        # Historiales globales para los reportes
        self.historial_sueldos = []
        self.historial_parque = []
        self.historial_tienda = []
        self.historial_pagos_completo = []

        self.main_menu()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear_screen()
        tk.Label(
            self.root,
            text="Menú Principal de Ejercicios",
            font=("Arial", 16, "bold"),
            pady=20,
        ).pack()

        container = tk.Frame(self.root)
        container.pack()

        # Aquí están los 10 ejercicios vinculados a sus funciones
        btns = [
            ("1. Aumento de Sueldos", self.ejercicio_1),
            ("2. Parque de Diversiones", self.ejercicio_2),
            ("3. Descuentos por Mes", self.ejercicio_3),
            ("4. Validar < 10", self.ejercicio_4),
            ("5. Validar Rango (0-20)", self.ejercicio_5),
            ("6. Registro de Intentos", self.ejercicio_6),
            ("7. Suma de N Números", self.ejercicio_7),
            ("8. Suma Acumulativa (0)", self.ejercicio_8),
            ("9. Suma hasta > 100", self.ejercicio_9),
            ("10. Pago Trabajadores Completo", self.ejercicio_10),
        ]

        for text, command in btns:
            ttk.Button(container, text=text, width=35, command=command).pack(pady=2)

    # --- UTILIDADES ---
    def validar_int(self, valor):
        try:
            return int(valor)
        except:
            return None

    def validar_float(self, valor):
        try:
            return float(valor)
        except:
            return None

    # --- 1. SUELDOS ---
    def ejercicio_1(self):
        self.clear_screen()
        tk.Label(
            self.root, text="Sistema de Aumento de Sueldos", font=("Arial", 12, "bold")
        ).pack(pady=10)
        tk.Label(self.root, text="Nombre:").pack()
        ent_nom = tk.Entry(self.root)
        ent_nom.pack()
        tk.Label(self.root, text="Sueldo Básico:").pack()
        ent_s = tk.Entry(self.root)
        ent_s.pack()

        def procesar():
            s = self.validar_float(ent_s.get())
            if s is None:
                return messagebox.showerror("Error", "Sueldo inválido")
            aumento = s * 0.15 if s < 4000 else (s * 0.10 if s <= 7000 else s * 0.08)
            res = f"{ent_nom.get()}: S/ {s + aumento:.2f}"
            self.historial_sueldos.append(res)
            messagebox.showinfo("Resultado", f"Nuevo Sueldo: S/ {s + aumento:.2f}")

        ttk.Button(self.root, text="Calcular", command=procesar).pack(pady=5)
        ttk.Button(
            self.root,
            text="Ver Historial",
            command=lambda: messagebox.showinfo(
                "Historial", "\n".join(self.historial_sueldos)
            ),
        ).pack()
        ttk.Button(self.root, text="Volver", command=self.main_menu).pack(pady=10)

    # --- 2. PARQUE ---
    def ejercicio_2(self):
        self.clear_screen()
        tk.Label(
            self.root, text="Parque de Diversiones", font=("Arial", 12, "bold")
        ).pack(pady=10)
        tk.Label(self.root, text="Edad:").pack()
        ent_e = tk.Entry(self.root)
        ent_e.pack()
        tk.Label(self.root, text="Juegos:").pack()
        ent_j = tk.Entry(self.root)
        ent_j.pack()

        def calcular():
            e, j = self.validar_int(ent_e.get()), self.validar_int(ent_j.get())
            if e is None or j is None:
                return
            total = j * 50
            desc = 0.25 if e < 10 else (0.10 if e <= 17 else 0)
            final = total * (1 - desc)
            self.historial_parque.append(final)
            messagebox.showinfo("Pago", f"Total a pagar: S/ {final}")

        ttk.Button(self.root, text="Pagar", command=calcular).pack(pady=5)
        ttk.Button(
            self.root,
            text="Recaudación Total",
            command=lambda: messagebox.showinfo(
                "Total", f"S/ {sum(self.historial_parque)}"
            ),
        ).pack()
        ttk.Button(self.root, text="Volver", command=self.main_menu).pack()

    # --- 3. TIENDA POR MES ---
    def ejercicio_3(self):
        self.clear_screen()
        meses_validos = {
            "enero": 0,
            "febrero": 0,
            "marzo": 0,
            "abril": 0,
            "mayo": 0,
            "junio": 0,
            "julio": 0.10,
            "agosto": 0,
            "septiembre": 0,
            "octubre": 0.15,
            "noviembre": 0,
            "diciembre": 0.20,
        }
        tk.Label(self.root, text="Descuento por Mes", font=("Arial", 12, "bold")).pack(
            pady=10
        )
        tk.Label(self.root, text="Mes:").pack()
        ent_m = tk.Entry(self.root)
        ent_m.pack()
        tk.Label(self.root, text="Importe:").pack()
        ent_i = tk.Entry(self.root)
        ent_i.pack()

        def procesar():
            mes = ent_m.get().lower().strip()
            imp = self.validar_float(ent_i.get())
            if mes in meses_validos and imp is not None:
                final = imp * (1 - meses_validos[mes])
                self.historial_tienda.append(final)
                messagebox.showinfo("Tienda", f"Total con descuento: S/ {final}")
            else:
                messagebox.showerror("Error", "Mes o importe incorrecto")

        ttk.Button(self.root, text="Calcular", command=procesar).pack(pady=5)
        ttk.Button(self.root, text="Volver", command=self.main_menu).pack()

    # --- 4, 5, 6. VALIDACIONES ---
    def ejercicio_4(self):
        self.clear_screen()
        self.intentos_ej4 = 0
        tk.Label(
            self.root, text="Validar número < 10", font=("Arial", 12, "bold")
        ).pack(pady=10)
        ent = tk.Entry(self.root)
        ent.pack()

        def validar():
            self.intentos_ej4 += 1
            n = self.validar_int(ent.get())
            if n is not None and n < 10:
                messagebox.showinfo(
                    "Correcto", f"Número: {n}\nIntentos: {self.intentos_ej4}"
                )
                self.main_menu()
            else:
                messagebox.showwarning("Error", "Debe ser menor a 10")

        ttk.Button(self.root, text="Validar", command=validar).pack(pady=5)
        ttk.Button(self.root, text="Volver", command=self.main_menu).pack()

    def ejercicio_5(self):
        self.clear_screen()
        tk.Label(
            self.root, text="Validar Rango (0-20)", font=("Arial", 12, "bold")
        ).pack(pady=10)
        ent = tk.Entry(self.root)
        ent.pack()

        def validar():
            n = self.validar_int(ent.get())
            if n is not None and 0 <= n <= 20:
                messagebox.showinfo("Correcto", f"Número {n} está en rango")
                self.main_menu()
            else:
                messagebox.showwarning("Error", "Fuera de rango (0-20)")

        ttk.Button(self.root, text="Validar", command=validar).pack(pady=5)
        ttk.Button(self.root, text="Volver", command=self.main_menu).pack()

    def ejercicio_6(self):
        self.clear_screen()
        self.lista_intentos = []
        tk.Label(
            self.root, text="Historial de Intentos (0-20)", font=("Arial", 12, "bold")
        ).pack(pady=10)
        ent = tk.Entry(self.root)
        ent.pack()

        def validar():
            n = self.validar_int(ent.get())
            if n is None:
                return
            self.lista_intentos.append(n)
            if 0 <= n <= 20:
                incorrectos = len([x for x in self.lista_intentos if x < 0 or x > 20])
                messagebox.showinfo(
                    "Fin",
                    f"Correcto: {n}\nIncorrectos: {incorrectos}\nHistorial: {self.lista_intentos}",
                )
                self.main_menu()
            else:
                messagebox.showwarning(
                    "Aviso", "Número registrado como incorrecto. Siga intentando."
                )

        ttk.Button(self.root, text="Ingresar", command=validar).pack(pady=5)
        ttk.Button(self.root, text="Volver", command=self.main_menu).pack()

    # --- 7. SUMA N ---
    def ejercicio_7(self):
        self.clear_screen()
        tk.Label(
            self.root, text="Suma de N números positivos", font=("Arial", 12, "bold")
        ).pack(pady=10)
        ent = tk.Entry(self.root)
        ent.pack()

        def calcular():
            n = self.validar_int(ent.get())
            if n and n > 0:
                serie = list(range(1, n + 1))
                messagebox.showinfo("Suma", f"Secuencia: {serie}\nTotal: {sum(serie)}")
            else:
                messagebox.showerror("Error", "Ingrese N positivo")

        ttk.Button(self.root, text="Sumar", command=calcular).pack(pady=5)
        ttk.Button(self.root, text="Volver", command=self.main_menu).pack()

    # --- 8. SUMA ACUMULATIVA ---
    def ejercicio_8(self):
        self.clear_screen()
        self.acumulados = []
        tk.Label(
            self.root,
            text="Suma Acumulativa (0 para parar)",
            font=("Arial", 12, "bold"),
        ).pack(pady=10)
        ent = tk.Entry(self.root)
        ent.pack()
        lbl = tk.Label(self.root, text="Suma actual: 0")
        lbl.pack()

        def agregar():
            n = self.validar_int(ent.get())
            if n == 0:
                messagebox.showinfo(
                    "Final", f"Lista: {self.acumulados}\nTotal: {sum(self.acumulados)}"
                )
                self.main_menu()
            elif n is not None:
                self.acumulados.append(n)
                lbl.config(text=f"Suma actual: {sum(self.acumulados)}")

        ttk.Button(self.root, text="Agregar", command=agregar).pack(pady=5)
        ttk.Button(self.root, text="Volver", command=self.main_menu).pack()

    # --- 9. SUMA > 100 ---
    def ejercicio_9(self):
        self.clear_screen()
        self.lista_9 = []
        tk.Label(
            self.root, text="Sumar hasta superar 100", font=("Arial", 12, "bold")
        ).pack(pady=10)
        ent = tk.Entry(self.root)
        ent.pack()
        lbl = tk.Label(self.root, text="Suma: 0")
        lbl.pack()

        def procesar():
            n = self.validar_int(ent.get())
            if n is not None:
                self.lista_9.append(n)
                actual = sum(self.lista_9)
                lbl.config(text=f"Suma: {actual}")
                if actual > 100:
                    messagebox.showinfo(
                        "Límite superado",
                        f"Cantidad: {len(self.lista_9)}\nSuma: {actual}",
                    )
                    self.main_menu()

        ttk.Button(self.root, text="Sumar", command=procesar).pack(pady=5)
        ttk.Button(self.root, text="Volver", command=self.main_menu).pack()

    # --- 10. PAGO COMPLETO ---
    def ejercicio_10(self):
        self.clear_screen()
        tk.Label(
            self.root,
            text="Sistema de Pago de Trabajadores",
            font=("Arial", 12, "bold"),
        ).pack(pady=5)
        noms = ["Nombre", "Hrs Normales", "Pago x Hr", "Hrs Extras", "Hijos"]
        ents = []
        for n in noms:
            tk.Label(self.root, text=n).pack()
            e = tk.Entry(self.root)
            e.pack()
            ents.append(e)

        def calcular():
            try:
                nom = ents[0].get()
                hn, ph, he, hi = (
                    float(ents[1].get()),
                    float(ents[2].get()),
                    float(ents[3].get()),
                    int(ents[4].get()),
                )
                p_n, p_e, bono = hn * ph, he * (ph * 1.5), hi * 0.5
                total = p_n + p_e + bono
                res = f"{nom}: S/ {total:.2f}"
                self.historial_pagos_completo.append(res)
                messagebox.showinfo("Cálculo", f"Pago Total: S/ {total:.2f}")
            except:
                messagebox.showerror("Error", "Datos inválidos")

        ttk.Button(self.root, text="Calcular", command=calcular).pack(pady=5)
        ttk.Button(
            self.root,
            text="Reporte",
            command=lambda: messagebox.showinfo(
                "Reporte", "\n".join(self.historial_pagos_completo)
            ),
        ).pack()
        ttk.Button(self.root, text="Volver", command=self.main_menu).pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = AppEmpresa(root)
    root.mainloop()
