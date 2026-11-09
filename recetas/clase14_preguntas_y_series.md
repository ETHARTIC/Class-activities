# Clase 14. Preguntas y series de tiempo

## Qué me están preguntando

| Pregunta | Qué buscaría |
|---|---|
| Descriptiva | Un resumen de los datos que tengo |
| Exploratoria | Algo raro o un patrón para seguir mirando |
| Inferencial | Una estimación para la población y su incertidumbre |
| Predictiva | Un valor nuevo y una forma de medir el error |
| Causal | Qué cambiaría si hago una intervención |
| Mecanística | Cómo se produce ese cambio, paso a paso |

Con dos números puedo describir qué cambió en el registro. Para extenderlo a la población tengo que mirar cómo se midieron y con qué incertidumbre. Para explicar una causa necesito además una comparación que sostenga esa interpretación.

[Ejemplos con titulares](clase14_titulares.md)

## Qué pasa si muevo la serie

Primero ordeno por fecha, reviso que no haya horas repetidas ni huecos y me quedo con una estación. En el práctico usé las 720 horas de Curva de Maronias.

- `shift(1)` pone el valor anterior en la misma fila. `diff(1)` calcula cuánto cambió. La primera fila queda sin diferencia.
- Con datos mensuales, `diff(12)` compara con el mismo mes del año anterior en las unidades originales. Para un porcentaje uso `100 * (x / x.shift(12) - 1)` y reviso el denominador.
- La autocorrelación compara la serie con una versión corrida. Al mezclar los valores de PM2.5 siguen siendo los mismos números, pero cambia esa relación porque cambia el orden.
- En una caminata aleatoria cada valor es el anterior más un paso aleatorio. Con pasos de media cero, el pronóstico simple del próximo valor es el actual.
- En ruido blanco la autocorrelación poblacional es cero para rezagos distintos de cero. En una muestra puede salir algo por azar.
- Una serie débilmente estacionaria tiene media y varianza constantes. La covarianza entre dos momentos depende de la distancia entre ellos.

El script suma las diferencias para volver a los valores originales y compara el correlograma con statsmodels. Si borro una hora vacía antes de calcular rezagos, la fila anterior puede quedar a dos horas en vez de una.

[Código](clase14_series.py) · [Presentación de clase](https://github.com/DavytJ/Introduccion-a-la-ciencia-de-datos/blob/56e76c472cf1ec67291eacdf303314eae0218027/clases/clase14/clase_titulares_y_series-3.pdf)
