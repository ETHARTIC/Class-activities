# Errores y diagnósticos

Registro elaborado el 27/10/2026. Se distingue lo observado en archivos anteriores
de los errores provocados ahora como parte del práctico.

| Caso | Cómo se manifiesta | Detección y corrección |
|---|---|---|
| Ruta de la profesora en el script de carga | Busca un CSV fuera del repositorio personal | Inspección de la ruta; se reemplaza por obtención y ruta del proyecto. |
| Ruta fija de Colab y CSV movido | El notebook antiguo no encuentra su archivo desde una copia actual | Comparación con el árbol actual; se elimina la dependencia de /content. |
| CSV de playas vacío | Solo contiene un salto de línea; no puede regenerar la tabla guardada | Se verifica el tamaño y se recupera la fuente oficial. |
| Copiar un nombre de columna de otra tabla | matricula_letra no pertenece al dataset de playas | Se perfila el esquema y se buscan claves con columnas de la fuente real. |
| Clave compuesta comprobada solo por duplicados | Puede aceptar una combinación con nulos | Se exige también que las columnas no tengan ausencias. |
| Plantilla de tránsito subida como si fuera resolución | Siete secciones sin código propio de respuesta | Comparación exacta con el archivo docente; se completan y ejecutan. |
| CSV con índice, provocado en el ejercicio 4 | Aparece Unnamed: 0 | Se guarda con index=False. |
| Codificación latin-1 leída como UTF-8, provocada en el ejercicio 5 | UnicodeDecodeError | Se inspecciona el formato y se declara encoding junto con separador y decimal. |
| Decimal no declarado, provocado en el ejercicio 5 | El peso queda como texto sin lanzar error | Se comprueban los tipos y se declara decimal=",". |
| -99 como dato, provocado en el ejercicio 7 | Media 48,45 en lugar de 85,3125 | Se declara el código como faltante y se documenta su significado. |
| Miles interpretados como decimal, ejercicio 8 | Media monetaria 169,278525 en lugar de 1.471,5 | Se declara thousands="." y se contrasta con la representación textual. |
| Suposición de que Parquet conserva todo | Falló una comparación de dtypes en la verificación actual | Se comprobó que rigidez se conserva y certeza numérica requiere reconstrucción. |
| Dependencia de Kaggle y datos ausentes | No se puede verificar de nuevo el gráfico sin train.csv | Se separa lectura de etiquetas de la descarga de imágenes y se declara el pendiente. |

El nombre de un archivo de clave no prueba que su contenido sea una credencial
válida. Se retiraron esos archivos sin abrirlos ni probarlos. Si eran claves
reales, eliminarlos de la versión actual no los revoca ni los borra del historial.
