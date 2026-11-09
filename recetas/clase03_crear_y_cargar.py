"""Ocho ejercicios de clase 3 resueltos y verificables desde cualquier carpeta.

Consignas: clases/clase3/ejercicios.py y prácticos A/B del repositorio docente.
Ejecutar antes: python3 datos/generar_caja.py
"""
from pathlib import Path
import sys
import json
import numpy as np
import pandas as pd
RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))
from funciones.datos import leer_csv, validar_caja


def resolver():
    carpeta = RAIZ / "datos/generados/caja"
    salida = RAIZ / "salidas/clase03"
    salida.mkdir(parents=True, exist_ok=True)
    resultado = {}

    # 1. El tipo conserva la escala de medición.
    df = leer_csv(carpeta / "caja_negra.csv")
    df["textura"] = df["textura"].astype("category")
    df["rigidez"] = pd.Categorical(df["rigidez"], ["blando", "medio", "rígido"], ordered=True)
    df["certeza_observador"] = pd.Categorical(df["certeza_observador"], [1, 2, 3, 4, 5], ordered=True)
    assert (df["rigidez"] > "blando").sum() == 6
    assert not any(pd.api.types.is_object_dtype(t) for t in df.dtypes)
    resultado["ej1_tipos"] = df.dtypes.astype(str).to_dict()

    # 2. Se acumulan los problemas, no se corta en el primero.
    roto = df.copy()
    roto.loc[0, "peso_estimado_g"] = -12
    roto.loc[3, "num_aristas"] = -1
    roto.loc[7, "objeto_id"] = 1
    assert validar_caja(df) == []
    assert len(validar_caja(roto)) == 3
    resultado["ej2_problemas"] = validar_caja(roto)

    # 3. Se documenta cómo se obtuvo cada valor, además de su significado.
    diccionario = pd.DataFrame([
        ["objeto_id", "identificador entero", "sin unidad", "asignación de un código por objeto", "único y no nulo", "no admite"],
        ["textura", "categórica nominal", "categoría", "tacto durante 15 s, sin ver el objeto", "suave/rugoso/poroso", "vacío si no se pudo clasificar"],
        ["rigidez", "categórica ordinal", "nivel", "tacto durante 15 s, sin ver el objeto", "blando < medio < rígido", "vacío si no se pudo clasificar"],
        ["num_aristas", "numérica discreta", "aristas", "conteo táctil durante 15 s, sin ver el objeto", "entero >= 0; 0 = ninguna arista", "vacío si se desconoce; no usar 0"],
        ["peso_estimado_g", "numérica continua", "gramos", "estimación táctil durante 15 s, sin balanza", "> 0", "vacío"],
        ["certeza_observador", "categórica ordinal", "nivel 1 a 5", "autoevaluación del observador tras el tacto", "1 < 2 < 3 < 4 < 5", "vacío"],
    ], columns=["variable", "tipo", "unidad", "instrumento", "rango_valido", "faltante"])
    assert diccionario.shape == (6, 6) and diccionario["faltante"].ne("").all()
    diccionario.to_csv(salida / "diccionario_variables.csv", index=False)

    # 4. Provocar la columna de índice y comparar CSV con Parquet.
    df.to_csv(salida / "con_indice.csv")
    con_indice = pd.read_csv(salida / "con_indice.csv")
    assert "Unnamed: 0" in con_indice
    df.to_csv(salida / "sin_indice.csv", index=False)
    leido = pd.read_csv(salida / "sin_indice.csv")
    csv_perdio_orden = not isinstance(leido["rigidez"].dtype, pd.CategoricalDtype)
    leido["rigidez"] = pd.Categorical(leido["rigidez"], ["blando", "medio", "rígido"], ordered=True)
    df.to_parquet(salida / "caja.parquet", index=False)
    parquet = pd.read_parquet(salida / "caja.parquet")
    assert list(leido) == list(df) and parquet["rigidez"].cat.ordered
    pd.testing.assert_series_equal(df["rigidez"], parquet["rigidez"])
    # En esta combinación de pandas/pyarrow la categórica numérica certeza
    # vuelve como int64. No afirmar que Parquet conserva TODOS los tipos.
    np.testing.assert_array_equal(df["certeza_observador"].astype(int), parquet["certeza_observador"].astype(int))
    tipo_certeza_parquet = str(parquet["certeza_observador"].dtype)
    parquet["certeza_observador"] = pd.Categorical(parquet["certeza_observador"], [1, 2, 3, 4, 5], ordered=True)
    pd.testing.assert_frame_equal(df, parquet)
    resultado["ej4"] = {"csv_perdio_orden": csv_perdio_orden, "parquet_conserva_orden_rigidez": True,
                         "tipo_certeza_parquet_antes_de_reconstruir": tipo_certeza_parquet}

    # 5. Se registra el mensaje real y se verifica el error silencioso.
    try:
        pd.read_csv(carpeta / "caja_negra_excel.csv")
    except UnicodeDecodeError as error:
        mensaje = f"{type(error).__name__}: {error}"
    else:
        raise AssertionError("Se esperaba un error UTF-8 con el archivo latin-1")
    (salida / "error_lectura.txt").write_text(mensaje, encoding="utf-8")
    bueno = pd.read_csv(carpeta / "caja_negra_excel.csv", sep=";", decimal=",", encoding="latin-1")
    sin_decimal = pd.read_csv(carpeta / "caja_negra_excel.csv", sep=";", encoding="latin-1")
    assert pd.api.types.is_numeric_dtype(bueno["peso_estimado_g"])
    assert not pd.api.types.is_numeric_dtype(sin_decimal["peso_estimado_g"])
    resultado["ej5"] = {"error_real": mensaje, "tipo_bueno": str(bueno["peso_estimado_g"].dtype),
                         "tipo_sin_decimal": str(sin_decimal["peso_estimado_g"].dtype)}

    # 6. Esta ruta sale del archivo del script, no de Path.cwd().
    assert (carpeta / "caja_negra.csv").is_file()
    assert leer_csv(carpeta / "caja_negra.csv").shape == (10, 6)
    resultado["ej6"] = "Lectura relativa al proyecto verificada"

    # 7. Leer literalmente permite ver también NA y la celda vacía.
    literales = pd.read_csv(carpeta / "caja_negra_faltantes.csv", keep_default_na=False)
    ingenuo = pd.read_csv(carpeta / "caja_negra_faltantes.csv")
    declarado = pd.read_csv(carpeta / "caja_negra_faltantes.csv", na_values=[-99, "s/d", "NA", ""])
    assert declarado["peso_estimado_g"].isna().sum() == 2
    resultado["ej7"] = {
        "valores_literales": {c: list(map(str, literales[c].unique())) for c in literales},
        "media_ingenua": float(ingenuo["peso_estimado_g"].mean()),
        "media_declarada": float(declarado["peso_estimado_g"].mean()),
        "faltantes_antes": ingenuo.isna().sum().astype(int).to_dict(),
        "faltantes_despues": declarado.isna().sum().astype(int).to_dict(),
    }

    # 8. Separador de miles, fechas y categorías se deciden explícitamente.
    vecino_ingenuo = pd.read_csv(carpeta / "equipo_vecino.csv")
    vecino = pd.read_csv(carpeta / "equipo_vecino.csv", thousands=".")
    vecino.columns = vecino.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
    vecino["fecha_operacion"] = pd.to_datetime(vecino["fecha_operacion"], format="%d/%m/%Y")
    for c in ["sucursal", "medio_de_pago"]:
        vecino[c] = vecino[c].str.strip().astype("category")
    assert vecino["sucursal"].nunique() == 3
    assert vecino["id_transaccion"].is_unique
    # Comprobación independiente del parseo de miles a partir del texto.
    literal = pd.read_csv(carpeta / "equipo_vecino.csv", dtype=str)
    esperado = literal["Monto UYU"].str.replace(".", "", regex=False).astype(int)
    np.testing.assert_array_equal(esperado, vecino["monto_uyu"])
    resultado["ej8"] = {"media_ingenua": float(vecino_ingenuo["Monto UYU"].mean()),
                         "media_correcta": float(vecino["monto_uyu"].mean()),
                         "categorias_antes": vecino_ingenuo["Sucursal "].unique().tolist(),
                         "categorias_despues": vecino["sucursal"].cat.categories.tolist()}
    vecino.describe(include="all").to_csv(salida / "perfil_vecino.csv")
    (salida / "resultados.json").write_text(json.dumps(resultado, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    return resultado


if __name__ == "__main__":
    resolver()
