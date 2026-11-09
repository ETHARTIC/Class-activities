# Diseño de encuestas — clase 6

Resolución del 27/10/2026. Fuente: `clases/clase6/clase_diseno_encuestas.qmd`
del repositorio docente. No se afirma haber aplicado estas preguntas a personas.

## De la tabla al cuestionario de cafetería

Período de referencia: últimos 30 días para compras y experiencia de servicio.
El ID lo asigna el sistema; no se pide un nombre ni otro identificador personal.

1. **En los últimos 30 días, ¿cuántas veces compró en la cafetería?** Nunca / 1–3 / 4–8 / Más de 8. Si responde Nunca, pasar a la pregunta 5. Produce `frecuencia`, ordinal.
2. **En esos 30 días, ¿qué productos compró? Marque todos los que correspondan.** Café / Comida / Bebidas frías / Otros. Produce cuatro binarias: `prod_cafe`, `prod_comida`, `prod_frias`, `prod_otros`.
3. **Pensando en la atención recibida en esos 30 días, ¿cómo la califica?** 1 Muy mala / 2 Mala / 3 Ni buena ni mala / 4 Buena / 5 Muy buena. Produce `atencion`, ordinal.
4. **En esos 30 días, ¿qué medios utilizó para pagar? Marque todos los que correspondan.** Efectivo / Tarjeta / Transferencia. Produce `pago_efectivo`, `pago_tarjeta`, `pago_transferencia`.
5. **Actualmente, ¿es estudiante de esta facultad?** Sí / No. Produce `estudiante`, binaria.
6. **Pensando en la cafetería en los últimos 30 días, ¿qué mejoraría?** Respuesta libre; puede dejarse vacía. Produce `mejora`, texto.
7. **Actualmente, ¿cuántos años cumplidos tiene?** Respuesta numérica opcional. Produce `edad`, cuantitativa discreta registrada en años.

Siete preguntas generan **trece columnas**, contando el ID automático. Los
productos y pagos no se vuelven una columna por pregunta: son selección múltiple.
Si frecuencia es Nunca, productos, atención y pagos quedan NA por filtro, no 0.
Para quien responde la pregunta múltiple, 0 indica opción no seleccionada; una
pregunta completa sin responder no se convierte automáticamente en todos ceros.

## Seis preguntas para corregir

### 1. Conformidad con comida y transporte

Problema: pregunta dos cosas juntas (doble cañón). Se separa:

- “Pensando en los últimos 30 días, ¿qué tan conforme está con su gasto en comida?”
- “Pensando en los últimos 30 días, ¿qué tan conforme está con su gasto en transporte?”

En ambas: Muy disconforme / Disconforme / Ni conforme ni disconforme / Conforme /
Muy conforme. Dos variables ordinales, **dos columnas**.

### 2. “¿No le parece que gasta demasiado en salidas?”

Problema: induce la respuesta y usa una negación. Propuesta: “¿Cuánto gastó en
salidas durante los últimos 30 días, en pesos uruguayos?”. Una variable
cuantitativa, **una columna**. Si se quiere medir conformidad en lugar de monto,
hay que preguntar esa percepción con una escala neutral: no son el mismo concepto.

### 3. Gasto en ropa “últimamente”

Problema: no hay un período compartido. Propuesta: “¿Cuánto gastó en ropa en los
últimos 30 días, en pesos uruguayos?”. Cuantitativa, **una columna**. Una respuesta
desconocida se registra como faltante; gasto 0 es un valor válido.

### 4. Tramos de transporte

Problema: los extremos 1.000 y 3.000 se superponen y falta cubrir montos mayores.
Propuesta: “¿Cuánto gastó en transporte en los últimos 30 días, en pesos uruguayos?”
Opciones: 0 / Más de 0 y hasta 1.000 / Más de 1.000 y hasta 3.000 / Más de 3.000 y
hasta 6.000 / Más de 6.000. Los extremos superiores están incluidos. Agregar
“No sabe / prefiere no responder” como no respuesta. Variable ordinal, **una columna**.

### 5. Medios de pago y “ambos”

Problema: hay más de dos medios; “ambos” es ambiguo y las combinaciones no se
cubren. Propuesta: “En los últimos 30 días, ¿qué medios utilizó para pagar sus
gastos? Marque todos: Efectivo / Tarjeta / Transferencia”. **Tres columnas binarias**.
La falta de respuesta se distingue de no haber seleccionado un medio específico.

### 6. Ingreso exacto del hogar como primera pregunta

Problema: pregunta sensible al inicio y exige precisión innecesaria. Moverla
hacia el final: “Pensando en el último mes calendario completo, ¿en qué tramo
se ubicó el ingreso total de su hogar, en pesos uruguayos?”. Ejemplo de tramos:
Hasta 30.000 / Más de 30.000 y hasta 60.000 / Más de 60.000 y hasta 100.000 /
Más de 100.000 / Prefiere no responder. Aclarar previamente qué ingresos incluye
la definición del estudio. Una variable ordinal, **una columna**; no respuesta
no es el tramo más alto ni un ingreso cero.
