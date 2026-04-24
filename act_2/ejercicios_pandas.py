# -*- coding: utf-8 -*-
"""
Segura Lozano Javier Amado
"""

import pandas as pd

df_profesores = pd.DataFrame(
    {
        "nombre": ["Jaime", "Armando", "Oscar"],
        "apellido_paterno": ["Miñor", "Alvarez", "Gomez"],
        "apellido_materno": ["Gomez", "Galvan", "Sanchez"],
    }
)

print(df_profesores)
print(type(df_profesores))
df_archivo = pd.read_csv(
    r"C:\Users\javie\OneDrive\Desktop\Actividades_IA\act_2\sacramento.csv"
)
print(df_profesores)


print(df_archivo)

print(df_archivo.head())

print(df_archivo.head(20))

print(df_archivo.tail())

print(df_archivo.dtypes)

print(df_archivo.describe())

print(df_archivo.loc[30])
print(df_archivo["city"])
print(df_archivo["city"] == "SACRAMENTO")
city = "SACRAMENTO"
print(df_archivo.query("city == @city"))
# ciudades con mas registroa
print(df_archivo["city"].value_counts())
# ciudad con mas regustris
print(df_archivo["city"].value_counts().idxmax())
print(df_archivo["city"].value_counts().max())
#promedio de precio por ciudad
print(df_archivo.groupby("city")["price"].mean().sort_values(ascending=False))
print(df_archivo.to_excel(r"C:\Users\javie\OneDrive\Desktop\Actividades_IA\act_2\sacramento.xlsx", index=False) )
print(df_archivo.query("citiy == 'SACRAMENTO' and price > 300000"))
