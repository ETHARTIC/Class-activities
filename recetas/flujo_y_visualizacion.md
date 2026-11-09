# Flujo de análisis y recetas de consulta

Notas de referencia a partir de las clases 4 a 10. No se presentan como una
entrada histórica semanal ni como evidencia de haber aplicado cada método.

## Importar, perfilar, limpiar y volver a mirar

1. Registrar origen, fecha de obtención, licencia y qué representa una fila.
2. Leer declarando formato; conservar el crudo sin editar y fuera de Git.
3. Perfilar tipos, faltantes, extremos, categorías y claves.
4. Limpiar solo los problemas diagnosticados y registrar cada decisión.
5. Repetir el perfilado; explicar filas perdidas y categorías modificadas.
6. Transformar, visualizar y volver a transformar cuando aparezca algo raro.
7. Comunicar una afirmación concreta, su alcance y su principal limitación.

La limpieza modifica contenidos; ordenar cambia estructura. Un pseudocódigo
útil declara entradas, transformaciones, verificaciones y salidas antes de
escribir detalles del lenguaje.

## Unir tablas sin multiplicar observaciones

Definir la unidad de observación y la clave de cada tabla. Revisar nulos y
repetidos antes de unir. En pandas, una unión con `validate="many_to_one"`
exige que la tabla del lado derecho tenga una fila por clave. `indicator=True`
permite contar las filas que no encontraron correspondencia. Una unión temporal
necesita además la misma frecuencia, definición del período y zona horaria.
No se registra una unión como realizada si no se usó en el trabajo concreto.

## Crear información

Un promedio por grupo cambia el nivel de observación: una tabla por playa ya no
es una tabla por muestra. Un tránsito relativo divide cada valor por la media de
su estación: 1 significa igual a esa media. El logaritmo requiere valores
positivos y mantiene el faltante donde falta el dato original.

## Elegir y leer gráficos

- Barras: comparar categorías y conteos; aclarar si las categorías se superponen.
- Histograma o densidad: forma de una variable numérica; los intervalos o el suavizado cambian su aspecto.
- Caja: mediana, cuartiles y observaciones extremas según una regla; un punto extremo no se elimina automáticamente.
- Dispersión: relación entre dos variables; mirar grupos, rango observado y casos influyentes.
- Serie temporal: ordenar por tiempo y comprobar frecuencia y períodos ausentes antes de unir puntos.

Todo gráfico necesita título, unidades, fuente y una afirmación que pueda
sostenerse. El gráfico RSNA tiene etiquetas superpuestas: sumar sus barras no
cuenta personas o estudios únicos. Los gráficos de tránsito separan franjas y
tipos de día para detectar relaciones que el promedio general oculta.

## Tiempo y autocorrelación

Antes de interpretar una correlación temporal, comprobar orden, regularidad del
intervalo, tendencia y estacionalidad. Una serie con tendencia puede correlacionar
con otra sin que exista un mecanismo entre ambas. Comparar datos de entrenamiento
y prueba respetando el orden temporal evita usar el futuro para explicar el pasado.
Estas son notas de método; falta confirmar qué ejercicios de series se trabajaron.
