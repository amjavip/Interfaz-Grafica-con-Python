import pandas as pd
import json

# Cargar los datos del CSV (Asegúrate de tener la ruta correcta o dejar 'datos.csv' si está en la misma carpeta)
df = pd.read_csv("C:\\Users\\javie\\OneDrive\\Desktop\\Actividades_IA\\docs\\datos.csv")

# 1. Media, mediana y moda de las variables numéricas obligatorias
media = df.mean(numeric_only=True).to_dict()
mediana = df.median(numeric_only=True).to_dict()

# La moda puede devolver múltiples valores, tomamos el primero de cada columna de interés
moda = {
    "peso": float(df["peso"].mode()[0]),
    "altura": float(df["altura"].mode()[0]),
    "velocidad": float(df["velocidad"].mode()[0]),
    "color": str(df["color"].mode()[0]),
}

# 2. Frecuencias basadas en la variable categórica: "color"
frec_abs = df["color"].value_counts()
frec_rel = df["color"].value_counts(normalize=True)
# Mantenemos el orden de la frecuencia absoluta para calcular la acumulada correctamente
frec_acum = frec_abs.cumsum()

# 3. Preparación de datos para el Polígono de Frecuencias (ej. Velocidad o Peso)
# Para un polígono de frecuencias real, agrupamos una variable numérica (ej. velocidad) y contamos sus repeticiones
poligono_datos = df["velocidad"].value_counts().sort_index()

# Guardar todo en el JSON estructurado
resultados = {
    "media": media,
    "mediana": mediana,
    "moda": moda,
    "frecuencia": frec_abs.to_dict(),
    "relativa": frec_rel.to_dict(),
    "acumulada": frec_acum.to_dict(),
    "poligono": {
        "labels": poligono_datos.index.tolist(),
        "valores": poligono_datos.values.tolist(),
    },
}

with open("resultados.json", "w", encoding="utf-8") as f:
    json.dump(resultados, f, ensure_ascii=False, indent=4)

print("¡Archivo resultados.json generado con éxito!")
