import pandas as pd

df = None  # variable global para guardar el CSV cargado

def load_csv(file_path):
    global df
    df = pd.read_csv(file_path)
    return f"Archivo cargado con {df.shape[0]} filas y {df.shape[1]} columnas."

def ask_about_csv(question: str) -> str:
    if df is None:
        return "Primero carga un CSV."
    if "filas" in question:
        return f"Hay {df.shape[0]} filas."
    elif "columnas" in question:
        return f"Hay {df.shape[1]} columnas: {', '.join(df.columns)}"
    elif "promedio" in question:
        col = question.split("de")[-1].strip()
        if col in df.columns:
            return f"Promedio de {col}: {df[col].mean():.2f}"
        else:
            return f"La columna {col} no existe."
    else:
        return "No entiendo la pregunta."
