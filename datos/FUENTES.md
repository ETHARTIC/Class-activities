# Fuentes de datos

## Caja negra didáctica

Generador adaptado de [Joselina Davyt, clase 3](https://github.com/DavytJ/Introduccion-a-la-ciencia-de-datos/blob/ee2f4a1e1eb4fb2bd6e38d3b8ec85a73867f6dff/clases/clase3/generar_archivos.py).
Diez observaciones didácticas; no son nuevas mediciones del estudiante. La semilla
42 fija la generación del archivo del equipo vecino. Se regeneran los CSV.
No se identificó una licencia general del repositorio docente.

## Ocho objetos propios

Diccionario del notebook personal, incorporado el 20/08/2026. Ocho filas y siete
columnas. Los datos de objetos se conservan en el código original. La documentación
no permite afirmar un instrumento ni tiempo de medición exactos del caso propio.

## Residuos

Copia histórica usada en clase: [commit a4ea2f7](https://github.com/ETHARTIC/Class-activities/tree/a4ea2f724513a3832f17a5c72efc6c808c7299b6/Actividades-de-clase/data/Archivos_de_base_de_datos).
Se recupera por URL fijada a ese commit, no desde una ruta cambiante. 1.222 filas,
41 columnas en la revisión. El material declara como origen el catálogo de datos
abiertos de Uruguay; falta recuperar la ficha específica para completar licencia.
La regularización retira el CSV de la versión actual de Git y conserva su obtención.

## Agua de playas

[Catálogo oficial: Datos de calidad de agua en playas](https://catalogodatos.gub.uy/dataset/monitoreo-de-agua-de-playas/resource/b143b5d2-5721-4efd-8ac5-9edb6e1ae3ac).
Organismo: Intendencia de Montevideo. Licencia indicada: Licencia de DAG de Uruguay.
Descarga verificada en la revisión: 27.284 filas, 12 columnas. El notebook anterior
mostraba 27.166 filas. La fuente se actualiza y esos números no tienen que coincidir.
El script registra fecha de obtención, dimensiones y SHA-256 de cada descarga nueva
en un archivo local junto al CSV.

## Tránsito y aire

[CSV del curso fijado a una versión](https://github.com/DavytJ/Introduccion-a-la-ciencia-de-datos/blob/ee2f4a1e1eb4fb2bd6e38d3b8ec85a73867f6dff/clases/clase10/transito_aire_junio2024.csv).
2.160 filas y cinco columnas originales. Junio de 2024; una fila por estación-hora.
Se conserva el carácter de material docente y no se afirma que sean mediciones
propias. No se identificó licencia general del repositorio del curso.

## RSNA / Kaggle

[Competencia](https://www.kaggle.com/competitions/rsna-knee-abnormality-detection).
Se necesita únicamente train.csv para repetir el filtrado y el gráfico. La obtención
puede requerir cuenta y aceptación de condiciones. No se copian los datos ni las
imágenes al repositorio. El archivo no estaba disponible para esta revisión;
58 estudios completos y 8 con una sola etiqueta positiva son resultados guardados
en el notebook anterior, no cifras recalculadas ahora.
