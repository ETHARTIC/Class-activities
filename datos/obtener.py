"""Obtiene datos sin versionar copias nuevas de los crudos ni usar claves API."""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import urlopen

RAIZ = Path(__file__).resolve().parents[1]
FUENTES = {
    "transito": {
        "archivo": "transito_aire_junio2024.csv",
        "url": "https://raw.githubusercontent.com/DavytJ/Introduccion-a-la-ciencia-de-datos/ee2f4a1e1eb4fb2bd6e38d3b8ec85a73867f6dff/clases/clase10/transito_aire_junio2024.csv",
        "origen": "Material de clase de Joselina Davyt; no se asume una medición nueva propia",
        "licencia": "No se identificó una licencia general en el repositorio del curso",
    },
    "playas": {
        "archivo": "playas.csv",
        "url": "https://ckan-data.montevideo.gub.uy/dataset/b51c24fd-ee40-4eec-a84c-0c4f064859b0/resource/b143b5d2-5721-4efd-8ac5-9edb6e1ae3ac/download/datos_de_calidad_de_agua_en_playas.csv",
        "origen": "Intendencia de Montevideo, monitoreo de agua de playas",
        "licencia": "Licencia de DAG de Uruguay, indicada en el catálogo oficial",
    },
    "residuos": {
        "archivo": "residuos_2023.csv",
        "url": "https://raw.githubusercontent.com/ETHARTIC/Class-activities/a4ea2f724513a3832f17a5c72efc6c808c7299b6/Actividades-de-clase/data/Archivos_de_base_de_datos/cantidad_de_residuos_en_la_estacion_de_transferencia_2023.csv",
        "origen": "Copia histórica usada en clase; origen declarado: catálogo de datos abiertos de Uruguay",
        "licencia": "Pendiente recuperar la ficha exacta de la fuente original; no se presupone licencia",
    },
}


def obtener(nombre, actualizar=False):
    """Descarga explícitamente la fuente elegida y conserva un registro local."""
    import pandas as pd
    fuente = FUENTES[nombre]
    destino = RAIZ / "datos" / "crudos" / fuente["archivo"]
    destino.parent.mkdir(parents=True, exist_ok=True)
    if destino.exists() and destino.read_bytes().strip() and not actualizar:
        return destino
    with urlopen(fuente["url"], timeout=60) as respuesta:
        contenido = respuesta.read()
    if not contenido.strip():
        raise ValueError(f"La descarga de {nombre} está vacía")
    from io import BytesIO
    tabla = pd.read_csv(BytesIO(contenido))
    esperado = {"transito": "hora", "playas": "fecha_muestra", "residuos": "pesada"}[nombre]
    if tabla.empty or esperado not in tabla:
        raise ValueError(f"La descarga de {nombre} no tiene el esquema esperado")
    destino.write_bytes(contenido)
    registro = {**fuente, "obtenido_utc": datetime.now(timezone.utc).isoformat(),
                "filas": len(tabla), "columnas": len(tabla.columns),
                "sha256": hashlib.sha256(contenido).hexdigest()}
    destino.with_suffix(".fuente.json").write_text(json.dumps(registro, ensure_ascii=False, indent=2), encoding="utf-8")
    return destino


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fuentes", nargs="*", choices=list(FUENTES), default=list(FUENTES))
    parser.add_argument("--actualizar", action="store_true", help="Volver a descargar; playas puede cambiar")
    opciones = parser.parse_args()
    for fuente in opciones.fuentes:
        print(fuente, obtener(fuente, opciones.actualizar))
