import pandas as pd
import json

# Cargar datos
df = pd.read_csv("C:\\Users\\javie\\OneDrive\\Desktop\\Actividades_IA\\docs\\datos.csv")

# Limpiar datos (quita NA)
df = df.dropna()

# -------------------------
# ESTADÍSTICA
# -------------------------
media = df.mean(numeric_only=True).to_dict()
mediana = df.median(numeric_only=True).to_dict()
moda = df.mode(numeric_only=True).iloc[0].to_dict()

# -------------------------
# FRECUENCIAS (COLOR)
# -------------------------
frecuencia = df["color"].value_counts().to_dict()
relativa = (df["color"].value_counts(normalize=True)).to_dict()
acumulada = df["color"].value_counts().cumsum().to_dict()

# -------------------------
# POLÍGONO (altura ordenada)
# -------------------------
altura_ordenada = df["altura"].sort_values().tolist()

# -------------------------
# GUARDAR JSON
# -------------------------
resultados = {
    "media": media,
    "mediana": mediana,
    "moda": moda,
    "frecuencia": frecuencia,
    "relativa": relativa,
    "acumulada": acumulada,
    "altura": altura_ordenada,
}

with open("resultados.json", "w") as f:
    json.dump(resultados, f)

print("JSON generado correctamente")
