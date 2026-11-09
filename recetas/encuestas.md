# Encuesta de cafetería

Para las compras uso los últimos 30 días. El ID lo asigna el formulario.

1. **¿Cuántas veces compró en la cafetería en los últimos 30 días?** Nunca / 1–3 / 4–8 / Más de 8. `frecuencia`, ordinal. Si pone Nunca, pasa a la 5.
2. **¿Qué productos compró? Marque todos los que correspondan.** Café / Comida / Bebidas frías / Otros. Quedan `prod_cafe`, `prod_comida`, `prod_frias` y `prod_otros`, todas 0/1.
3. **¿Cómo califica la atención?** De 1 (muy mala) a 5 (muy buena), con 3 como punto medio. `atencion`, ordinal.
4. **¿Con qué medios pagó? Marque todos los que usó.** Efectivo / Tarjeta / Transferencia. Quedan `pago_efectivo`, `pago_tarjeta` y `pago_transferencia`, todas 0/1.
5. **¿Es estudiante de esta facultad?** Sí / No. `estudiante`, binaria.
6. **¿Qué mejoraría de la cafetería?** `mejora`, texto libre y opcional.
7. **¿Cuántos años cumplidos tiene?** `edad`, numérica discreta y opcional.

Quedan 13 columnas contando el ID. Si alguien nunca compró, las preguntas 2, 3 y 4 quedan en NA por el salto. En una respuesta múltiple que sí contestó, 0 indica una opción que no marcó.

## Seis preguntas para corregir

1. **Conformidad con comida y transporte.** Hay dos preguntas mezcladas. Haría una sobre cada gasto en los últimos 30 días, con cinco opciones desde muy disconforme hasta muy conforme. Quedan dos columnas ordinales.
2. **Gastar demasiado en salidas.** La pregunta empuja a decir que sí. Pondría «¿Cuánto gastó en salidas en los últimos 30 días, en pesos uruguayos?». Queda una columna numérica. Si quiero medir cómo se siente con lo que gasta, usaría una escala neutral de conformidad.
3. **Gasto en ropa “últimamente”.** Cada persona puede entender un período distinto. Preguntaría «¿Cuánto gastó en ropa en los últimos 30 días, en pesos uruguayos?». Queda una columna numérica. Cero y sin respuesta van separados.
4. **Tramos de transporte.** Los extremos se pisan y falta una opción para más de 6.000. Dejaría 0 / Más de 0 hasta 1.000 / Más de 1.000 hasta 3.000 / Más de 3.000 hasta 6.000 / Más de 6.000, más «No sabe o prefiere no responder». La pregunta usa pesos y últimos 30 días. Queda una columna ordinal.
5. **Medios de pago y “ambos”.** Hay tres medios y “ambos” no dice cuáles. Preguntaría qué medios usó en los últimos 30 días y dejaría marcar efectivo, tarjeta y transferencia por separado. Quedan tres columnas binarias.
6. **Ingreso exacto al empezar.** Es una pregunta sensible. La pondría cerca del final, pediría el ingreso total del hogar del último mes calendario en pesos y usaría tramos. Por ejemplo: hasta 30.000 / más de 30.000 hasta 60.000 / más de 60.000 hasta 100.000 / más de 100.000. Agregaría «Prefiere no responder» y definiría qué se incluye como ingreso. Queda una columna ordinal.
