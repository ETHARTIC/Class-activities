"""Reproduce los prácticos y contrasta la regresión con álgebra independiente.

Ejecutar desde la raíz: python3 verificar.py
Requiere las dependencias de requirements.txt y conexión para obtener los crudos
si todavía no están en datos/crudos/. No necesita ninguna clave de IA.
"""
from pathlib import Path
import json
import os
import subprocess
import sys
import numpy as np
import pandas as pd

RAIZ = Path(__file__).resolve().parent


def correr(archivo, *argumentos):
    subprocess.run([sys.executable, str(RAIZ / archivo), *argumentos],
                   cwd=RAIZ, env={**os.environ, "MPLBACKEND": "Agg"}, check=True)


if __name__ == "__main__":
    correr("datos/obtener.py", "transito", "playas", "residuos")
    for archivo in ["datos/generar_caja.py", "funciones/datos.py",
                    "recetas/objetos_a_ciegas.py", "recetas/clase03_crear_y_cargar.py",
                    "recetas/carga_y_perfilado.py", "recetas/clase14_series.py",
                    "Actividades-de-clase/scripts/clase12_ejercicios(1).py"]:
        correr(archivo)
    d = pd.read_csv(RAIZ / "datos/crudos/transito_aire_junio2024.csv")
    d = d[d["estacion"] == "Tres Cruces"].dropna(subset=["transito", "no2", "pm25"])
    x = np.column_stack([np.ones(len(d)), d["transito"]/1000, d["pm25"]])
    y = d["no2"].to_numpy()
    coef = np.linalg.lstsq(x, y, rcond=None)[0]
    r2 = 1 - np.sum((y-x@coef)**2)/np.sum((y-y.mean())**2)
    r = json.loads((RAIZ / "salidas/transito/resultados.json").read_text())
    assert len(d) == r["ej4"]["n"]
    assert abs(r2-r["ej4"]["r2_base"]) < 1e-10
    # Repetir la comparación del ejercicio 5 con una matriz explícita.
    horas = pd.to_datetime(d["hora"]).dt.hour
    x5 = np.column_stack([x, (horas >= 18).astype(int)])
    coef5 = np.linalg.lstsq(x5, y, rcond=None)[0]
    np.testing.assert_allclose(coef5, list(r["ej5"]["coeficientes"].values()), rtol=1e-9)
    # Ejecutar nuevamente desde otra carpeta detecta dependencias de cwd.
    subprocess.run([sys.executable, str(RAIZ / "recetas/clase03_crear_y_cargar.py")],
                   cwd=RAIZ.parent, check=True, stdout=subprocess.DEVNULL)
    print("VERIFICACIÓN CORRECTA: prácticos ejecutados; OLS contrastado con NumPy; rutas portables.")
