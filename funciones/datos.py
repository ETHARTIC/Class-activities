"""Lectura, perfilado y validación. Ver casos de prueba al final del archivo."""
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]


def leer_csv(ruta, **opciones):
    """Lee un CSV no vacío. Las opciones de formato deben declararse al llamar."""
    ruta = Path(ruta)
    if not ruta.is_file():
        raise FileNotFoundError(f"No existe {ruta}. Ejecutar primero datos/obtener.py.")
    if not ruta.read_bytes().strip():
        raise ValueError(f"El archivo {ruta.name} está vacío; no es una tabla válida.")
    return pd.read_csv(ruta, **opciones)


def perfil(tabla):
    """Devuelve una fila por variable, sin modificar la tabla de entrada."""
    filas = []
    for nombre, serie in tabla.items():
        numerica = pd.api.types.is_numeric_dtype(serie)
        filas.append({
            "variable": nombre, "tipo": str(serie.dtype), "filas": len(tabla),
            "no_nulos": int(serie.notna().sum()),
            "faltantes": int(serie.isna().sum()),
            "porcentaje_faltantes": float(serie.isna().mean() * 100),
            "distintos": int(serie.nunique()),
            "minimo": serie.min() if numerica else None,
            "maximo": serie.max() if numerica else None,
        })
    return pd.DataFrame(filas)


def es_clave(tabla, columnas):
    """Una clave candidata exige filas, columnas presentes, unicidad y no nulos.

    La unicidad observada no demuestra que sea una clave de negocio: eso se
    confirma con la documentación de la fuente.
    """
    if not columnas or tabla.empty or any(c not in tabla for c in columnas):
        return False
    return bool(not tabla[columnas].isna().any().any()
                and not tabla.duplicated(subset=columnas).any())


def validar_caja(tabla):
    """Acumula todas las restricciones incumplidas del práctico de caja negra."""
    problemas = []
    peso = pd.to_numeric(tabla["peso_estimado_g"], errors="coerce")
    certeza = pd.to_numeric(tabla["certeza_observador"].astype(object), errors="coerce")
    aristas = pd.to_numeric(tabla["num_aristas"], errors="coerce")
    verificaciones = [
        (peso.isna() | (peso <= 0), "peso ausente, no numérico o no positivo"),
        (certeza.isna() | ~certeza.between(1, 5) | (certeza % 1 != 0), "certeza fuera de 1–5 o ausente"),
        (aristas.isna() | (aristas < 0) | (aristas % 1 != 0), "aristas ausentes o no enteras no negativas"),
        (tabla["objeto_id"].isna() | tabla["objeto_id"].duplicated(), "identificador ausente o repetido"),
    ]
    for mascara, descripcion in verificaciones:
        cantidad = int(mascara.sum())
        if cantidad:
            problemas.append(f"{cantidad}: {descripcion}")
    return problemas


if __name__ == "__main__":
    # Casos de prueba: repetidos, nulos y una clave compuesta válida.
    ejemplo = pd.DataFrame({"sitio": ["A", "A", "B"], "dia": [1, 2, 1],
                            "valor": [10.0, None, 20.0]})
    assert es_clave(ejemplo, ["sitio", "dia"])
    assert not es_clave(ejemplo, ["sitio"])
    assert not es_clave(pd.DataFrame({"id": [1, None]}), ["id"])
    assert not es_clave(pd.DataFrame({"id": []}), ["id"])
    assert perfil(ejemplo).set_index("variable").loc["valor", "faltantes"] == 1
    print("Funciones: casos de prueba correctos.")
