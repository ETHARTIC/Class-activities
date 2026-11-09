# Bitácora de Ciencia de Datos

Ethan Schcolnik · Universidad de Montevideo · 2026

Acá tengo las actividades, los scripts y las notas de qué hice con cada tabla. Las fechas del [diario](diario/README.md) indican la semana del trabajo. Algunas entradas las armé después a partir de los archivos y commits que quedaron.

## Trabajos

| Clase o tema | Archivo |
|---|---|
| Objetos a ciegas | [Notebook](Actividades-de-clase/data/Objetos_a_ciegas.ipynb) · [Notas](recetas/objetos_a_ciegas.md) |
| Clase 3 | [Fundamentos](recetas/fundamentos.md) · [Ejercicios 1 a 8](recetas/clase03_respuestas.md) · [Desafío](recetas/clase03_desafio.md) |
| Clases 4 y 5 | [Residuos y playas](recetas/carga_y_perfilado.md) · [Preguntas sobre errores](recetas/errores_opcion_multiple.md) |
| Clase 6 | [Encuesta de cafetería](recetas/encuestas.md) |
| Gráfico de rodilla | [Notebook RSNA](Actividades-de-clase/scripts/trabajo-creacion-grafico.ipynb) |
| Clase 11 | [Leer un ticket](recetas/ia_y_validacion.md) |
| Tránsito y aire | [Siete ejercicios](recetas/transito_resultados.md) |
| Clase 14 | [Uniones](recetas/clase14_uniones.md) · [Titulares](recetas/clase14_titulares.md) · [Series](recetas/clase14_preguntas_y_series.md) |
| Clase 15 | [Comparar grupos](recetas/clase15_experimento.md) |
| Apuntes | [Flujo de análisis](recetas/flujo_y_visualizacion.md) · [Lecturas](recetas/lecturas.md) |

## Para correr el código

Desde la carpeta del repositorio, con Python 3.11 o más nuevo:

```bash
python -m pip install -r requirements.txt
python verificar.py
```

La primera vez se descargan los CSV de tránsito, playas y residuos. Los datos se guardan en `datos/crudos/` y los resultados en `salidas/`. Para el ticket hace falta Tesseract y para recalcular RSNA desde las etiquetas originales hace falta el `train.csv` de Kaggle. Cada receta tiene el comando que usé.

[Qué falta confirmar](ESTADO.md) · [Decisiones](decisiones.md) · [Errores](errores/registro.md) · [Fuentes de datos](datos/FUENTES.md) · [Comprobaciones](VALIDACION.md)

[Material de la profesora](https://github.com/DavytJ/Introduccion-a-la-ciencia-de-datos)
