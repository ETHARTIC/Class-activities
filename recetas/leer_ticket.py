"""Extraer y comprobar los dos ítems del ticket de clase 11."""
import argparse
import csv
from decimal import Decimal
from pathlib import Path
import re
import subprocess

RAIZ = Path(__file__).resolve().parents[1]


def leer_ticket(foto):
    # 1. Pasar la foto a texto.
    try:
        texto = subprocess.run(
            ["tesseract", str(foto), "stdout", "--psm", "6"],
            capture_output=True, text=True, check=True,
        ).stdout
    except FileNotFoundError as error:
        raise SystemExit("Instalá Tesseract y agregalo al PATH.") from error

    # 2. Buscar solo las líneas de producto del ticket de clase.
    filas = re.findall(r"^(LECHE .+?|PAN .+?)\s+(\d+[.,]\d{2})\b", texto, re.M)
    productos = [(nombre.strip(), Decimal(monto.replace(",", "."))) for nombre, monto in filas]

    # 3. Comparar con los dos montos y el total impresos.
    if [monto for _, monto in productos] != [Decimal("18.00"), Decimal("32.00")]:
        raise ValueError("La lectura no coincide con los productos del ticket. Revisá la imagen.")
    total = sum(monto for _, monto in productos)
    assert total == Decimal("50.00")
    return productos, total


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("foto", type=Path)
    productos, total = leer_ticket(parser.parse_args().foto)
    salida = RAIZ / "salidas" / "ticket.csv"
    salida.parent.mkdir(exist_ok=True)
    with salida.open("w", newline="", encoding="utf-8") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["descripcion", "monto"])
        writer.writerows(productos)
    print(f"{len(productos)} productos. Total: {total} UYU.")
