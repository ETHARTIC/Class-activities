"""Carga y perfila los dos casos de clase sin copiar rutas de otra máquina."""
from pathlib import Path
import sys
RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))
from funciones.datos import leer_csv, perfil, es_clave
import pandas as pd


def analizar_residuos():
    # Se recupera la misma copia histórica; el crudo ya no se versiona.
    from datos.obtener import obtener
    ruta = obtener("residuos")
    tabla = leer_csv(ruta)
    print("RESIDUOS", tabla.shape, "duplicados", int(tabla.duplicated().sum()))
    print("matricula_letra es clave:", es_clave(tabla, ["matricula_letra"]))
    print("pesada es clave candidata:", es_clave(tabla, ["pesada"]))
    print(perfil(tabla).to_string(index=False))
    return tabla


def analizar_playas():
    # La copia antigua del repositorio está vacía; usar la fuente oficial.
    tabla = leer_csv(RAIZ / "datos/crudos/playas.csv")
    tabla["fecha_muestra"] = pd.to_datetime(tabla["fecha_muestra"], errors="raise")
    clave = ["fecha_muestra", "desc_abreviada_punto"]
    print("PLAYAS", tabla.shape)
    print("Clave compuesta candidata:", es_clave(tabla, clave))
    print(perfil(tabla).to_string(index=False))
    print("\nSalinidad media por playa (descriptivo, sin ajustar por fecha):")
    print(tabla.groupby("playa")["salinidad"].agg(["count", "mean"]).sort_values("mean").to_string())
    return tabla


if __name__ == "__main__":
    analizar_residuos()
    analizar_playas()
