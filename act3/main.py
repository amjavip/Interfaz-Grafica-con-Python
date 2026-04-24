import customtkinter as ctk
from login import LoginFrame
from app import MainApp

from db import inicializar_db

inicializar_db()


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x500")
        self.title("Sistema")

        self.mostrar_login()

    def mostrar_login(self):
        self.clear()
        self.login = LoginFrame(self, self.mostrar_app)
        self.login.pack(expand=True)

    def mostrar_app(self):
        self.clear()
        self.app = MainApp(self)
        self.app.pack(expand=True, fill="both")

    def clear(self):
        for w in self.winfo_children():
            w.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
