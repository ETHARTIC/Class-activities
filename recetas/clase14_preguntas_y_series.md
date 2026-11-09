# Clase 14 — preguntas, titulares y series de tiempo

Material docente: [PDF fechado el 20/10/2026](https://github.com/DavytJ/Introduccion-a-la-ciencia-de-datos/blob/ee2f4a1e1eb4fb2bd6e38d3b8ec85a73867f6dff/clases/clase14/clase_titulares_y_series-3.pdf).
Notas y receta preparadas el 27/10. No había una resolución personal de este bloque
en el repositorio revisado. No se atribuyen al estudiante intervenciones en clase.

## La pregunta determina el alcance

| Tipo | Qué se busca | Cuidado al interpretar |
|---|---|---|
| Descriptiva | Resumir los registros disponibles | No generalizar automáticamente a toda la población. |
| Exploratoria | Encontrar patrones para investigar | Un patrón descubierto no es una prueba causal. |
| Inferencial | Aprender sobre una población desde una muestra | Importan selección, diseño e incertidumbre. |
| Predictiva | Anticipar valores desconocidos | Evaluar en observaciones que no se usaron para ajustar. |
| Causal | Estimar qué cambiaría al intervenir | Necesita un diseño y supuestos que identifiquen el efecto. |
| Mecanística | Explicar cómo funciona un proceso | Una correlación no describe todos sus pasos. |

El titular por sí solo no fija la categoría: hay que leer la pregunta, los datos
y cómo se obtuvieron. Un cambio de medición puede aparentar un cambio de realidad.
Una diferencia entre estimaciones requiere evaluar su incertidumbre; no basta con
comparar dos números ni con comparar mecánicamente márgenes de error por separado.

## Actividad de las tarjetas

La diapositiva 9 pide analizar tres tarjetas entregadas a cada equipo: pregunta,
tipo de análisis, datos necesarios y dibujo del gráfico, con una posible
reescritura del titular. **Las tres tarjetas asignadas y sus noticias completas
no están en el PDF ni en el repositorio personal.** Su resolución específica queda
pendiente; no se reemplazan con noticias elegidas al azar.

Guía para cada tarjeta: identificar población y unidad de observación; definir
variables y período; decir si se describe, generaliza, predice o estima un efecto;
proponer ejes, unidades y qué representa cada punto; señalar qué afirmación
supera la evidencia. El material pide dibujar el gráfico a mano: una imagen nueva
generada automáticamente no acredita esa actividad.

## Series de tiempo

Una serie conserva orden y frecuencia. Antes de calcular rezagos, elegir una
unidad y ordenar por fecha, comprobar duplicados y verificar que no falten horas
o meses. Mezclar estaciones no produce una sola serie de una unidad.

- **Ruido blanco:** media y varianza constantes y autocovarianzas nulas en rezagos no nulos. El ejemplo de clase usa ruido normal independiente; esa es una construcción más específica.
- **Caminata aleatoria:** el nivel anterior más un paso aleatorio. Con pasos de media cero, el pronóstico ingenuo del próximo nivel es el actual. Una subida visual puede ser azar acumulado.
- **Rezago:** `shift(k)` coloca junto al valor actual el de k períodos antes. Presupone que las filas estén ordenadas y espaciadas como se espera.
- **Diferencia:** `diff(k)` calcula nivel actual menos nivel de k períodos antes. Con k=1, falta la primera diferencia; no se completa con cero.
- **Autocorrelación:** relación lineal entre la serie y su pasado. Una ACF alta no demuestra causalidad ni garantiza buena predicción.
- **Estacionariedad débil:** media constante y covarianza dependiente del rezago, con segundos momentos finitos. La varianza constante está incluida. Un correlograma es un diagnóstico, no una demostración por sí solo.

Comparar junio con junio evita mezclar directamente meses distintos, aunque no
elimina todas las diferencias entre años. `diff(12)` en una serie mensual produce
un cambio interanual **en unidades originales**; una tasa porcentual se calcula
como `100 * (x / x.shift(12) - 1)` y exige revisar valores cero en el denominador.

## Receta verificada

`clase14_series.py` selecciona Curva de Maronias y verifica 720 horas consecutivas.
Calcula rezagos y diferencias, reconstruye los niveles sumando los cambios y
contrasta la ACF propia con statsmodels. También mezcla los valores de PM2.5:
conserva exactamente su distribución, pero cambia su orden y su autocorrelación.
Las simulaciones están identificadas como tales y usan semilla 42.

La banda de referencia del correlograma es aproximada y corresponde a una
referencia de ruido. Al mirar muchos rezagos pueden aparecer barras fuera por azar;
no se considera cada barra una prueba independiente de memoria predictiva útil.
No se eliminan huecos temporales con dropna antes de la ACF: eso cambiaría qué
distancia temporal representa un rezago. Esta receta usa series completas.
