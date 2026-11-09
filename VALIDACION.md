# Comprobaciones

Última corrida: 09/11/2026, con Python 3.12.14, pandas 2.2.3 y statsmodels 0.15.0.

- `python verificar.py` descargó o leyó los CSV y corrió los ejercicios de caja negra, carga, tránsito, series, desafío, titulares y comparación de grupos.
- El desafío vuelve a leer el CSV en otro proceso. Coincidieron las 10 filas, el orden de los meses y sus valores.
- En tránsito volví a calcular R² y los coeficientes del modelo de noche con NumPy. Coincidieron con statsmodels.
- Para las uniones 58 a 61 comparé las cuentas con las soluciones y repetí los cruces pequeños con pandas.
- El OCR del ticket encontró dos ítems. Revisé la foto, los montos y el total de 50 UYU.
- Corrí las celdas de los notebooks. En RSNA comprobé las 12 barras contra la imagen anterior. La ruta que lee un CSV se probó con tres filas de prueba. Para repetir esa ruta con los estudios reales falta el archivo de Kaggle.
- Revisé los enlaces a archivos dentro del repo.

| CSV | Filas | Columnas |
|---|---:|---:|
| Residuos | 1.222 | 41 |
| Playas | 27.441 | 12 |
| Tránsito y aire | 2.160 | 5 |

Los ejemplos de R quedaron como respuestas de lectura. Las comprobaciones se hicieron en Python y las descargas se registran en los archivos `.fuente.json` junto a cada CSV.

[Fuentes y fechas de descarga](datos/FUENTES.md)
