"""Repetir el ejemplo simulado de clase 15 con los 20 registros originales."""
import numpy as np
import pandas as pd
from scipy import stats

# 1. Generar los mismos 20 registros del script de clase.
rng = np.random.default_rng(123)
n = 20
fumador = rng.choice(["No", "Sí"], n, p=[0.6, 0.4])
nivel = rng.choice(["Primaria", "Secundaria", "Terciaria"], n)
datos = pd.DataFrame({
    "sexo": rng.choice(["Femenino", "Masculino"], n),
    "fumador": fumador,
    "nivel_educ": pd.Categorical(nivel, ["Primaria", "Secundaria", "Terciaria"]),
    "region": rng.choice(["Norte", "Centro", "Sur"], n),
})
datos["edad"] = np.round(rng.normal(40, 10, n) + np.where(datos["fumador"] == "Sí", 8, 0))
datos["ingreso"] = np.round(rng.lognormal(np.log(30000), 0.4, n) * (datos["nivel_educ"].cat.codes + 1))

# 2. Ver cuántos fuman en cada grupo y comparar las proporciones.
tabla = pd.crosstab(datos["sexo"], datos["fumador"])
print(tabla)
print("Fisher, p:", round(stats.fisher_exact(tabla).pvalue, 4))

# 3. Comparar edad por tabaquismo.
no = datos.loc[datos["fumador"] == "No", "edad"]
si = datos.loc[datos["fumador"] == "Sí", "edad"]
prueba = stats.ttest_ind(si, no, equal_var=False)
ic = prueba.confidence_interval()
print(datos.groupby("fumador")["edad"].agg(["size", "mean"]).round(2))
print(f"Diferencia Sí - No: {si.mean() - no.mean():.2f} años")
print(f"Welch, p = {prueba.pvalue:.4f}, IC95% [{ic.low:.2f}, {ic.high:.2f}]")

# 4. Mirar la distribución de ingreso por educación con mediana y cuartiles.
ingresos = datos.groupby("nivel_educ", observed=True)["ingreso"]
print(ingresos.quantile([0.25, 0.5, 0.75]).unstack().round(0))
grupos = [grupo.to_numpy() for _, grupo in ingresos]
print("Kruskal-Wallis, p:", round(stats.kruskal(*grupos).pvalue, 4))
