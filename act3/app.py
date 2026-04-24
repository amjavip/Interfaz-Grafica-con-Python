import customtkinter as ctk
from db import obtener_consulta


class MainApp(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.menu = ctk.CTkFrame(self)
        self.menu.pack(side="left", fill="y")

        self.resultado = ctk.CTkTextbox(self)
        self.resultado.pack(side="right", expand=True, fill="both")

        for i in range(1, 11):
            btn = ctk.CTkButton(
                self.menu, text=f"Consulta {i}", command=lambda i=i: self.mostrar(i)
            )
            btn.pack(pady=5)

    def mostrar(self, num):
        datos = obtener_consulta(num)

        self.resultado.delete("1.0", "end")

        if not datos:
            self.resultado.insert("end", "Sin resultados")
            return

        # Encabezados según consulta
        headers = {
            1: ["ID", "Nombre", "Edad"],
            2: ["Nombre"],
            3: ["Total pedidos"],
            4: ["ID", "Nombre", "Precio", "Stock"],
            5: ["Cliente", "Total"],
            6: ["Promedio"],
            7: ["ID", "Cliente_ID", "Total"],
            8: ["Nombre"],
            9: ["Máximo"],
            10: ["Mínimo"],
        }

        cols = headers.get(num, [])

        # Imprimir encabezados
        if cols:
            self.resultado.insert("end", " | ".join(cols) + "\n")
            self.resultado.insert("end", "-" * 40 + "\n")

        # Imprimir filas
        for fila in datos:
            fila_str = " | ".join(str(x) for x in fila)
            self.resultado.insert("end", fila_str + "\n")
