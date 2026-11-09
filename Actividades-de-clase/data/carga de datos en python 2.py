"""Entrada compatible para la actividad original de carga de residuos."""
from pathlib import Path
import sys
RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ))
from recetas.carga_y_perfilado import analizar_residuos
if __name__ == "__main__":
    analizar_residuos()
