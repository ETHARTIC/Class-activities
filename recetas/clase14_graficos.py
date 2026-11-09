"""Graficar los tres ejemplos de titulares con los valores documentados."""
from pathlib import Path

import matplotlib.pyplot as plt

salida = Path(__file__).resolve().parents[1] / "salidas" / "titulares"
salida.mkdir(parents=True, exist_ok=True)

fig, ax = plt.subplots()
ax.plot(["Dic. 2025", "Ene. 2026"], [7.0, 7.4], marker="o")
ax.set(title="Desempleo estimado, total país", ylabel="Tasa (%)", ylim=(0, 9))
fig.text(0.12, 0.01, "Fuente: INE, Encuesta Continua de Hogares")
fig.savefig(salida / "desempleo.png", dpi=140, bbox_inches="tight")
plt.close(fig)

fig, ax = plt.subplots()
ax.plot(["Jun. 2025", "Jun. 2026"], [100, 100.88], marker="o", linestyle="none")
ax.set(title="Índice de salario real", ylabel="Índice (junio 2025 = 100)", ylim=(99, 102))
fig.text(0.12, 0.01, "Fuente: INE, Índice Medio de Salarios")
fig.savefig(salida / "salario_real.png", dpi=140, bbox_inches="tight")
plt.close(fig)

fig, ax = plt.subplots()
barras = ax.bar(["Ene.–jun. 2025", "Ene.–jun. 2026"], [147949, 142541])
ax.bar_label(barras, labels=["147.949", "142.541"], padding=3)
ax.set(title="Delitos registrados en el primer semestre", ylabel="Registros", ylim=(0, 165000))
fig.text(0.12, 0.01, "Fuente: Ministerio del Interior")
fig.savefig(salida / "delitos_registrados.png", dpi=140, bbox_inches="tight")
plt.close(fig)
