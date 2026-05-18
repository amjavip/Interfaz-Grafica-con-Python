import pandas as pd
import json

df = pd.read_csv("C:\\Users\\javie\\OneDrive\\Desktop\\Actividades_IA\\docs\\datos.csv")

# Media, mediana, moda
media = df.mean(numeric_only=True).to_dict()
mediana = df.median(numeric_only=True).to_dict()
moda = df.mode(numeric_only=True).iloc[0].to_dict()

# Frecuencias por tipo
frecuencia = df["tipo"].value_counts().to_dict()
relativa = df["tipo"].value_counts(normalize=True).to_dict()
acumulada = df["tipo"].value_counts().cumsum().to_dict()

# Guardar JSON
resultados = {
    "media": media,
    "mediana": mediana,
    "moda": moda,
    "frecuencia": frecuencia,
    "relativa": relativa,
    "acumulada": acumulada,
}

with open("resultados.json", "w") as f:
    json.dump(resultados, f)
