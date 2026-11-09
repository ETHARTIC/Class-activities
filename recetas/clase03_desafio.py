"""Ejemplo de serie mensual para el desafío de clase 3."""
import argparse
from pathlib import Path

import pandas as pd

CARPETA = Path(__file__).resolve().parents[1] / "datos" / "generados" / "desafio"
ARCHIVO = CARPETA / "indice.csv"
VALORES = [100, 101, 102, 102, 103, 104, 104, 106, 105, 107]


def guardar():
    # 1. Una observación por mes. Los valores son de ejemplo.
    meses = pd.period_range("2026-01", periods=len(VALORES), freq="M")
    serie = pd.Series(VALORES, index=meses, name="indice")
    CARPETA.mkdir(parents=True, exist_ok=True)
    serie.to_csv(ARCHIVO, index_label="mes")


def revisar():
    # 2. Ver cómo queda el mes si leo el archivo sin indicar el tipo.
    tabla = pd.read_csv(ARCHIVO)
    print("Índice de la lectura normal:", type(tabla.index).__name__)
    meses = pd.PeriodIndex(tabla.pop("mes"), freq="M")
    serie = tabla.set_index(meses)["indice"]
    serie.index.name = "mes"

    # 3. Comparar el índice, la frecuencia, los valores y el tipo.
    esperado = pd.Series(
        VALORES,
        index=pd.period_range("2026-01", periods=10, freq="M", name="mes"),
        name="indice",
    )
    pd.testing.assert_series_equal(serie, esperado)
    print(serie.to_string())
    print("10 filas, frecuencia mensual y valores iguales al original.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paso", choices=["guardar", "revisar"])
    opciones = parser.parse_args()
    if opciones.paso == "guardar":
        guardar()
    else:
        revisar()
