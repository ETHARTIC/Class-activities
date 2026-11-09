"""Clase 14: series, rezagos, diferencias y autocorrelación.

Material: clase_titulares_y_series-3.pdf, fechado 20/10/2026.
Esta receta se preparó el 27/10; no acredita una ejecución previa en clase.
"""
from pathlib import Path
import sys
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import acf
RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))
from funciones.datos import leer_csv


def autocorrelacion(x, rezago):
    """ACF con media global y divisor n en autocovarianzas, como en las diapositivas."""
    valores = np.asarray(x, dtype=float)
    if valores.ndim != 1 or not np.isfinite(valores).all():
        raise ValueError("Se requiere una serie unidimensional sin faltantes")
    if not 0 <= rezago < len(valores):
        raise ValueError("El rezago debe estar entre 0 y n-1")
    centrados = valores - valores.mean()
    denominador = centrados @ centrados
    if denominador == 0:
        raise ValueError("La autocorrelación no se define para una serie constante")
    return float((centrados[:len(valores)-rezago] @ centrados[rezago:]) / denominador)


def resolver():
    tabla = leer_csv(RAIZ / "datos/crudos/transito_aire_junio2024.csv", parse_dates=["hora"])
    serie = tabla[tabla["estacion"] == "Curva de Maronias"].sort_values("hora").set_index("hora")
    assert len(serie) == 720 and serie.index.is_unique
    assert (serie.index.to_series().diff().dropna() == pd.Timedelta(hours=1)).all()
    transito = serie["transito"]
    diferencias = transito.diff()
    # La primera fila no tiene anterior; no se la reemplaza por diferencia cero.
    reconstruida = transito.iloc[0] + diferencias.iloc[1:].cumsum()
    np.testing.assert_allclose(reconstruida, transito.iloc[1:])
    rezagos = serie[["transito"]].copy()
    rezagos["anterior"] = transito.shift(1)
    rezagos["diferencia"] = diferencias
    salida = RAIZ / "salidas/series"
    salida.mkdir(parents=True, exist_ok=True)
    rezagos.head(6).to_csv(salida / "rezagos_y_diferencias.csv")

    pm25 = serie["pm25"].to_numpy()
    assert np.isfinite(pm25).all()
    rng = np.random.default_rng(42)
    mezclada = rng.permutation(pm25)
    np.testing.assert_array_equal(np.sort(pm25), np.sort(mezclada))
    ruido = rng.normal(0, 1, 720)
    caminata = np.r_[0.0, np.cumsum(ruido)]
    np.testing.assert_allclose(np.diff(caminata), ruido, atol=1e-12)

    resultados = {"n_horas": len(serie), "primeras_diferencias": diferencias.iloc[1:6].tolist(),
                   "media_pm25": float(pm25.mean()), "media_mezclada": float(mezclada.mean()),
                   "acf_pm25_1": autocorrelacion(pm25, 1),
                   "acf_mezclada_1": autocorrelacion(mezclada, 1),
                   "acf_transito": {str(k): autocorrelacion(transito, k) for k in [1, 12, 24]},
                   "semilla": 42}
    # Comprobación con una implementación distinta de la ACF.
    referencia = acf(transito.to_numpy(), nlags=72, fft=False, adjusted=False)
    for k in [0, 1, 12, 24, 72]:
        assert abs(autocorrelacion(transito, k) - referencia[k]) < 1e-12

    fig, ejes = plt.subplots(3, 2, figsize=(12, 9))
    for fila, (nombre, x) in enumerate([("Tránsito: Curva de Maronias", transito.to_numpy()),
                                       ("Ruido normal simulado", ruido),
                                       ("Caminata simulada", caminata[1:])]):
        ejes[fila, 0].plot(np.arange(len(x)), x, linewidth=.8)
        ejes[fila, 0].set(title=nombre, xlabel="Hora / paso", ylabel="Vehículos/h" if fila == 0 else "Valor simulado")
        ks = np.arange(73)
        valores = [autocorrelacion(x, int(k)) for k in ks]
        ejes[fila, 1].vlines(ks, 0, valores, linewidth=1)
        banda = 1.96 / np.sqrt(len(x))
        ejes[fila, 1].axhspan(-banda, banda, color="grey", alpha=.2)
        ejes[fila, 1].axhline(0, color="black", linewidth=.5)
        ejes[fila, 1].set(title="Autocorrelación muestral", xlabel="Rezago en horas / pasos", ylabel="ACF")
    fig.suptitle("Clase 14: orden temporal y memoria. Fuente: CSV docente; simulaciones con semilla 42")
    fig.tight_layout()
    fig.savefig(salida / "series_y_correlogramas.png", dpi=150)
    plt.close(fig)
    (salida / "resultados.json").write_text(json.dumps(resultados, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(resultados, ensure_ascii=False, indent=2))
    return resultados


if __name__ == "__main__":
    resolver()
