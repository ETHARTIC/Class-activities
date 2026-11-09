"""Reutiliza los ocho objetos del notebook original, sin inventar mediciones."""
from pathlib import Path
import json
import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]


def analizar():
    original = RAIZ / "Actividades-de-clase/data/Objetos_a_ciegas.ipynb"
    notebook = json.loads(original.read_text(encoding="utf-8"))
    fuente = notebook["cells"][0]["source"]
    fuente = "".join(fuente) if isinstance(fuente, list) else fuente
    # Solo el literal del diccionario propio; no se ejecuta código del notebook.
    import ast
    asignacion = ast.parse(fuente).body[0]
    tabla = pd.DataFrame(ast.literal_eval(asignacion.value))
    assert tabla.shape == (8, 7)
    columnas = [c for c in tabla if c != "objeto"]
    assert tabla[columnas].isin([0, 1]).all().all()
    assert tabla["objeto"].is_unique
    print(tabla.to_string(index=False))
    print("\nFrecuencias de atributos (pueden coexistir):")
    print(tabla[columnas].sum().to_string())
    return tabla


if __name__ == "__main__":
    analizar()
