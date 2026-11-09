# Verificación técnica — 27/10/2026

## Ejecuciones completadas

- Los ocho ejercicios de creación/lectura de datos pasaron sus verificaciones.
- La función de validación detecta los tres errores introducidos y acepta la tabla limpia.
- La ida y vuelta CSV/Parquet comprueba valores y tipos; se documentó la reconstrucción de certeza ordinal.
- El perfilado de residuos reproduce 1.222 filas y 41 columnas; la fuente actual de playas produjo 27.284 filas y 12 columnas.
- Los siete ejercicios de tránsito se ejecutaron y generaron seis figuras y un JSON de resultados.
- Las regresiones base y de noche se contrastaron con matrices de mínimos cuadrados mediante NumPy; tolerancias 1e-10 para R² y 1e-9 relativa para coeficientes.
- La receta de series verifica 720 horas consecutivas, reconstrucción de niveles, diferencias de caminata y ACF propia contrastada con statsmodels a tolerancia 1e-12.
- Se ejecutaron las celdas de los cuatro notebooks con un espacio nuevo por notebook. En RSNA solo se verificó la rama de datos ausentes; no se verificó el cálculo con train.csv.
- Una copia limpia, sin crudos, datos generados ni resultados, descargó las tres fuentes y completó `python3 verificar.py` desde fuera de la carpeta del proyecto.
- Se inspeccionaron visualmente el gráfico de series/correlogramas y el gráfico final de tránsito por tipo de día.

## Entorno comprobado

Python 3.12.14.

| Paquete | Versión |
|---|---|
| NumPy | 2.3.5 |
| pandas | 2.2.3 |
| Matplotlib | 3.10.8 |
| SciPy | 1.17.0 |
| statsmodels | 0.15.0 |
| pyarrow | 26.0.0 |

Las dependencias admiten un rango de versiones en requirements.txt. Estos
resultados corresponden al entorno de esta tabla; los comportamientos de tipos
pueden variar. Las verificaciones buscan detectar esas diferencias.

## Huellas de las fuentes en la copia limpia

| Archivo | Filas | Columnas | SHA-256 |
|---|---:|---:|---|
| residuos_2023.csv | 1222 | 41 | `d9c060344a6cc8ace192e80e10ebfb9df4c07bce1bc94364bbe6981edb417e4e` |
| playas.csv | 27284 | 12 | `bf6da09bee72067fc0b5073e815c56ff8746d81a87abdce76937436b45e7757b` |
| transito_aire_junio2024.csv | 2160 | 5 | `df90b9d15ee10f8848c6c2154351075628dc455422389ce9310d26a2f5696b5d` |

La fuente de playas es dinámica y puede cambiar. Los otros dos archivos se
obtienen de commits fijados. Cada descarga nueva guarda localmente su fecha,
dimensiones y huella junto al CSV.

## Límites de la verificación

No se ejecutaron ejemplos específicos de R, solicitudes a servicios de IA ni el
análisis numérico de RSNA sin su CSV. No se dispone de las tarjetas de noticias ni
de información suficiente para resolver el desafío del equipo. La verificación
técnica no acredita la revisión personal ni el dominio del estudiante, que deben
completarse. No se realizaron cambios retrospectivos en las fechas de commits.
