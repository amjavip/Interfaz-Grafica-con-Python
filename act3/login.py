import customtkinter as ctk

ctk.set_appearance_mode("dark")

import os


def validar_login(user, password):
    user = user.strip()
    password = password.strip()

    try:
        ruta = os.path.join(os.path.dirname(__file__), "users.txt")

        with open(ruta, "r") as f:
            for line in f:
                u, p = line.strip().split(",")

                if user == u and password == p:
                    return True
    except Exception as e:
        print("ERROR:", e)
        return False

    return False


class LoginFrame(ctk.CTkFrame):
    def __init__(self, master, on_login_success):
        super().__init__(master)

        self.on_login_success = on_login_success

        self.user_entry = ctk.CTkEntry(self, placeholder_text="Usuario")
        self.user_entry.pack(pady=10)

        self.pass_entry = ctk.CTkEntry(self, placeholder_text="Contraseña", show="*")
        self.pass_entry.pack(pady=10)

        self.btn = ctk.CTkButton(self, text="Iniciar sesión", command=self.login)
        self.btn.pack(pady=20)

    def login(self):
        user = self.user_entry.get()
        password = self.pass_entry.get()

        if not user or not password:
            print("Campos vacíos")
            return

        if validar_login(user, password):
            self.on_login_success()
        else:
            print("Credenciales incorrectas")
