# Desafío de clase 3

Ejemplo resuelto con una serie mensual. Queda por confirmar si esta era la estructura del equipo. Para practicar usé 10 valores de ejemplo de un índice de precios, base enero = 100.

| Columna | Tipo | Qué mide | Faltantes |
|---|---|---|---|
| mes | Período mensual | Mes de la observación, de enero a octubre de 2026 | No admite |
| indice | Entero, puntos de índice | Nivel de precios relativo a enero de 2026 | No hay en el ejemplo |

Una fila corresponde a un mes. `mes` es la clave y `indice` es la variable que quiero seguir.

1. `python recetas/clase03_desafio.py guardar` crea `datos/generados/desafio/indice.csv`.
2. `python recetas/clase03_desafio.py revisar` lo abre en otro proceso. El CSV guarda el texto del mes, pero pandas usa un índice numérico al leerlo.
3. Paso `mes` a `PeriodIndex` mensual y lo uso como índice. La comparación verifica las 10 filas, su orden, la frecuencia y los valores.

Si quiero calcular un cambio mensual, primero tengo que mirar que no falte un mes. De otra forma, dos filas seguidas pueden estar separadas por más de un mes.

[Consigna de clase 3](https://github.com/DavytJ/Introduccion-a-la-ciencia-de-datos/blob/56e76c472cf1ec67291eacdf303314eae0218027/clases/clase3/ejercicios.py)
