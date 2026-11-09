# Apuntes de carga, uniones y gráficos

## Cómo arranco con una tabla

1. Anoto de dónde viene, cuándo la bajé y qué representa una fila.
2. La leo con el formato correcto y miro `shape`, `dtypes`, nulos y repetidos.
3. Corrijo lo que encontré y repito el perfil. Si se pierden filas, cuento cuántas y por qué.
4. Hago las uniones y calculo las columnas que necesito.
5. Grafico, miro si el resultado tiene sentido y vuelvo atrás si encuentro algo raro.

Ordenar la tabla es dejar una fila por observación y una columna por variable. Limpiar es corregir valores o tipos. En pseudocódigo me sirve escribir qué entra, qué cambio y qué chequeo antes de empezar en Python.

## Unir y agrupar

Antes de un `merge` miro si la clave está completa y cuántas veces aparece de cada lado. Con `validate="many_to_one"` puedo pedir que la tabla derecha tenga una fila por clave. Con `indicator=True` cuento cuáles quedaron sin pareja. Si la tabla de clima tiene una fila por aeropuerto y hora, necesito las dos columnas.

Agrupar por playa cambia la unidad. Cada fila del resumen representa una playa. En tránsito, dividir por la media de la estación hace que 1 signifique el promedio de esa estación.

## Qué gráfico usaría

- **Barras** para conteos por categoría. Si un caso puede estar en varias, lo aclaro.
- **Histograma** para ver la forma de una variable numérica. Los intervalos pueden hacer que se vea distinta.
- **Caja** para mediana, cuartiles y valores alejados. Reviso esos puntos antes de decidir si son errores.
- **Dispersión** para comparar dos variables. Colorear por grupo puede mostrar lo que se mezcla en el total.
- **Línea** para datos en el tiempo. Ordeno por fecha y miro si faltan períodos.

[Uniones 58–61](clase14_uniones.md) · [Series](clase14_preguntas_y_series.md)
