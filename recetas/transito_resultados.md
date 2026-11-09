# Tránsito y calidad del aire — siete ejercicios

Resolución y ejecución: 27/10/2026. Fuente de consignas y preparación: Joselina
Davyt, clase12 (R) y clase13 (Python). El archivo personal de Python era una
plantilla sin resolver; se completó conservando enunciados y preparación.

Datos: junio de 2024, 2.160 filas, tres estaciones y 720 horas por estación.
Una fila es una estación-hora. Se verifica que esa clave no se repita.

## 1. Faltantes

| Estación | Sin NO2 | Sin PM2.5 | Sin log(PM2.5) |
|---|---:|---:|---:|
| Curva de Maronias | 65 | 0 | 0 |
| Museo Romántico | 720 | 144 | 144 |
| Tres Cruces | 429 | 326 | 326 |

No hay faltantes en tránsito, franja, tipo de día ni tránsito relativo. El
logaritmo conserva exactamente los faltantes de PM2.5; los valores observados
son positivos. El NO2 completamente ausente en una estación no equivale a NO2
cero ni se soluciona borrando todas las filas sin documentarlo.

## 2. Hora pico

Se eligió una regla reproducible: las seis horas con mayor tránsito medio de
lunes a viernes en Tres Cruces, manteniendo seis como en la clasificación inicial.
Resultan **8, 9, 12, 15, 16 y 17**. Frente a ese criterio, 7, 18 y 19 estaban
marcadas de más y faltaba marcar 12, 15 y 16. No es una definición universal:
depende de la estación, el período y la regla elegida.

## 3. PM2.5 por franja

El PM2.5 medio es máximo en **noche** en las tres estaciones; el tránsito medio
es máximo en **tarde**. No coinciden. Se retiró la línea en 1 porque era una
referencia del tránsito relativo, no una referencia de concentración de PM2.5.
Los ejes de concentración están en µg/m³.

## 4. Agregar franja

Sobre las mismas 291 observaciones, R² pasa de
**0.473137** a **0.486127**: mejora unos
1,30 puntos porcentuales. Es una mejora descriptiva pequeña dentro de la muestra.
Agregar variables puede subir R² sin mejorar predicción fuera de muestra.
La referencia de franja es madrugada; los coeficientes de las otras franjas se
interpretan manteniendo tránsito y PM2.5 constantes.

## 5. Indicador de noche

Noche vale 1 entre las 18 y 23 horas y 0 en el resto. R² es
**0.481316**. Su coeficiente es **3.818586 µg/m³**:
es la diferencia ajustada asociada a noche, manteniendo tránsito y PM2.5 constantes.
No demuestra un efecto causal de la noche. Seleccionar la variable mirando su
significación vuelve el análisis exploratorio y no una prueba confirmatoria nueva.

## 6. Interacción

La pendiente más alta es madrugada: **2.938380**
µg/m³ de NO2 por mil vehículos/hora en la recta descriptiva de ese grupo.
Se crea el indicador y se ajusta `transito_miles * franja_empinada`.

El modelo tiene R² **0.397535**. La pendiente para el resto es
0.583049; la interacción agrega
2.355331, por lo que la de
madrugada es aproximadamente 2,938380. La interacción permite pendientes distintas;
una variable binaria sumada sin interacción solo cambia el intercepto.

Este modelo no incluye PM2.5, por lo que no se interpreta su R² como el efecto
puro de agregar una interacción al modelo del ejercicio 5.

## 7. Los dos grupos de la tarde

Al colorear por tipo de día aparecen diferencias entre días de semana y fin de
semana. En los registros de la tarde con NO2 observado, el tránsito medio es
42,18146 mil vehículos/hora en días de semana y 28,90271 en fin de semana;
NO2 medio es 49,99224 y 41,79097 µg/m³, respectivamente.

Como extensión, se ajustó `no2 ~ transito_miles * tipo_dia` sobre
74 observaciones de la tarde, con R² 0.229264. Permite
niveles y pendientes diferentes. El gráfico y el resumen describen la separación;
no prueban que el tipo de día sea su única explicación.

## Alcance y verificación

Los modelos 3, 4 y 5 usan las mismas 291 filas, de modo que sus R² son comparables
en la misma muestra. La regresión base y el modelo de noche se contrastaron con
mínimos cuadrados mediante NumPy. Las observaciones son horarias: la independencia
de los errores y los p-valores convencionales no se dan por demostrados; faltantes,
autocorrelación y variables omitidas limitan la inferencia.

Los seis gráficos se regeneran en `salidas/transito/`. Los coeficientes y conteos
completos se regeneran en `salidas/transito/resultados.json`.
