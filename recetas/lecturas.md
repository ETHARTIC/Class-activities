# Apuntes de las tres lecturas

## Tukey. The Future of Data Analysis, sección 1

El análisis incluye buscar qué vale la pena mirar, elegir cómo medirlo e interpretar lo que salió. Se apoya en matemática, pero también hay que probar las herramientas con datos y ver qué pasa cuando los supuestos fallan.

Un ejemplo del práctico es el peso medio. Pandas puede hacer bien la cuenta e igual dar un promedio que no tiene sentido si el −99 en realidad significa que falta la medición. Antes de elegir un método tengo que entender qué representa cada columna.

[Artículo de Tukey](https://doi.org/10.1214/aoms/1177704711)

## Hernán, Hsu y Healy. Describir, predecir y estimar un efecto

- **Describir.** ¿Qué se ve en los datos que tengo? Ejemplo, el NO₂ medio por franja.
- **Predecir.** ¿Qué valor espero ver después o en otro caso? Para probarlo puedo entrenar con un período y medir el error en uno posterior.
- **Estimar un efecto.** ¿Qué cambiaría si interviniera? Por ejemplo, cuánto bajaría el NO₂ si disminuyera el tránsito. Necesito definir la intervención y una comparación que se pueda defender.

Las tres preguntas pueden usar las mismas columnas. Lo que cambia es qué evidencia necesito para responder cada una.

[Artículo de Hernán, Hsu y Healy](https://content.sph.harvard.edu/wwwhsph/sites/1268/1268/20/hernan_chance19.pdf)

## Breiman. Statistical Modeling, pp. 199–215

Una forma de trabajar parte de un modelo para explicar cómo se generan los datos. La otra busca un algoritmo que acierte con observaciones nuevas aunque el mecanismo sea complejo. Breiman muestra por qué importa separar datos de entrenamiento y de prueba. Por ejemplo, en el caso del ozono se probó el pronóstico con los últimos dos años, después de ajustar con los cinco anteriores.

Me sirve para leer el práctico de tránsito. El R² de ajuste me dice cuánto explica la recta en las filas que usé. Para saber si pronostica bien tendría que medir el error con horas que el modelo todavía no vio.

[Artículo de Breiman](https://doi.org/10.1214/ss/1009213726)
