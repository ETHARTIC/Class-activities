# Tránsito y aire

Usé la tabla de junio de 2024. Tiene 2.160 filas. Son 720 horas para cada una de las tres estaciones y la clave es estación + hora.

## 1. Faltantes

| Estación | NO₂ | PM2.5 | Log de PM2.5 |
|---|---:|---:|---:|
| Curva de Maronias | 65 | 0 | 0 |
| Museo Romántico | 720 | 144 | 144 |
| Tres Cruces | 429 | 326 | 326 |

Los números de la tabla son faltantes. Tránsito, franja, tipo de día y tránsito relativo están completos. El log de PM2.5 queda vacío en las mismas filas que PM2.5. En Museo Romántico faltan las 720 mediciones de NO₂.

## 2. Hora pico

Para Tres Cruces de lunes a viernes tomé las seis horas con mayor tránsito medio. Quedaron **8, 9, 12, 15, 16 y 17**. Con esa regla salen 7, 18 y 19 del grupo original y entran 12, 15 y 16.

## 3. PM2.5 por franja

El PM2.5 medio es más alto de noche en las tres estaciones. El tránsito medio llega al máximo de tarde. En el gráfico de concentración saqué la línea en 1 porque marcaba la referencia del tránsito relativo. La concentración está en µg/m³.

## 4. Agregar franja

Con las mismas 291 filas, el R² pasa de **0,473137** a **0,486127**. Son 1,30 puntos porcentuales más dentro de la muestra. Madrugada queda de referencia. Los coeficientes de las demás franjas comparan con madrugada a igual tránsito y PM2.5.

## 5. Indicador de noche

Vale 1 de 18 a 23 y 0 en las demás horas. El modelo da R² = **0,481316**. El coeficiente de noche es **+3,818586 µg/m³** a igual tránsito y PM2.5. Es una diferencia ajustada de estas observaciones y el modelo no identifica un efecto causal.

## 6. Interacción

La recta de madrugada quedó con la mayor pendiente, **2,938380** µg/m³ por mil vehículos/hora. En el modelo con interacción, el resto tiene pendiente 0,583049 y a madrugada se le suman 2,355331. El R² dio 0,397535. Este modelo también cambia las variables, porque no incluye PM2.5, así que el cambio de R² no se puede atribuir solo a la interacción.

## 7. Los dos grupos de la tarde

| Tipo de día | Tránsito medio (miles de vehículos/hora) | NO₂ medio (µg/m³) |
|---|---:|---:|
| Lunes a viernes | 42,18 | 49,99 |
| Fin de semana | 28,90 | 41,79 |

El modelo que deja una pendiente distinta por tipo de día usa 74 filas y da R² = 0,229264. La separación se ve al colorear los puntos. Puede haber otras diferencias entre esos días que no estén en la tabla.

**Chequeo.** Comparé los modelos de los puntos 4 y 5 sobre las mismas filas y repetí la regresión base y la de noche con NumPy. Son observaciones horarias. Antes de interpretar los p-valores revisaría si los errores de horas cercanas se parecen.

[Código del práctico](<../Actividades-de-clase/scripts/clase12_ejercicios(1).py>) · [Fuente](../datos/FUENTES.md)
