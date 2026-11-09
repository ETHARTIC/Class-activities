# Clase 14. Tres titulares

Usé los tres casos que aparecen juntos en la presentación para resolver la actividad. Las tarjetas que repartieron a cada equipo pueden ser distintas.

## 1. Desempleo al comienzo de 2026

- **Pregunta.** ¿Cuánto cambió la tasa de desempleo de diciembre a enero? Es descriptiva si comparo las estimaciones publicadas. Si quiero afirmar que la tasa poblacional subió, necesito medir la incertidumbre de la diferencia.
- **Datos y análisis.** Tasa mensual de la ECH con la misma definición y cobertura. Diciembre dio 7,0% y enero 7,4%. La diferencia es de **0,4 puntos porcentuales**. Miraría enero de otros años para ver si el salto coincide con una época del año.
- **Gráfico.** Mes en x, tasa de desempleo (%) en y. Dos puntos unidos en 7,0 y 7,4. Si tengo la serie completa, agrego los meses anteriores. Para inferencia hacen falta errores de estimación.
- **Titular que usaría.** La tasa de desempleo estimada pasó de 7,0% en diciembre a 7,4% en enero.

[INE, diciembre 2025](https://www5.ine.gub.uy/documents/Demograf%C3%ADayEESS/HTML/ECH/Empleo/2025/Bolet%C3%ADn_T%C3%A9cnico_MT%20Diciembre%202025.html) · [INE, enero 2026](https://www.gub.uy/instituto-nacional-estadistica/comunicacion/publicaciones/actividad-empleo-desempleo-ech-enero-2026)

## 2. Salario real de junio

- **Pregunta.** ¿Cuánto cambió el índice de salario real entre junio de 2025 y junio de 2026? Es una comparación descriptiva.
- **Datos y análisis.** Necesito los índices de salarios y precios de ambos meses. El salario nominal subió 5,16% y los precios 4,25%. La cuenta es `(1,0516 / 1,0425 − 1) × 100`, que da cerca de **0,87%** con esos datos redondeados. El valor que publicó el INE fue **0,88%**.
- **Gráfico.** Mes en x, índice de salario real en y. Tomo junio de 2025 como 100 y marco junio de 2026 en 100,88. De tener el resto de los meses, puedo mostrar si el recorrido fue parejo.
- **Titular que usaría.** El índice de salario real subió 0,88% en junio frente al mismo mes del año anterior. Es un cambio del índice y el sueldo de cada persona puede haber cambiado distinto.

[INE, cuadro 2 del boletín de junio](https://www5.ine.gub.uy/documents/Estad%C3%ADsticasecon%C3%B3micas/HTML/IMS/2026/IMS%20Junio%202026.html)

## 3. Delitos en el primer semestre

- **Pregunta.** ¿Cuántos delitos registró la Policía de enero a junio en 2025 y en 2026? Es descriptiva.
- **Datos y análisis.** Necesito los registros de los dos semestres, con igual cobertura, período y criterio de conteo. Se pasó de 147.949 a 142.541. Son **5.408 registros menos**, o **−3,66%**, que se redondea a −3,7%.
- **Gráfico.** Dos barras desde cero. En x van los semestres y en y la cantidad de registros. Si quiero ver si la caída se repite, agrego los mismos semestres de otros años.
- **Titular que usaría.** Los delitos registrados bajaron 3,7% en el primer semestre de 2026 frente al de 2025. El registro depende también de las denuncias y de la forma en que se relevan los hechos.

[Boletín del Ministerio del Interior](https://www.gub.uy/ministerio-interior/comunicacion/publicaciones/boletin-semestral-estadisticas-criminales-enero-junio-2026) · [Cifras de la presentación](https://www.gub.uy/ministerio-interior/comunicacion/noticias/delitos-bajaron-37-primer-semestre-2026-respecto-igual-periodo-2025)

Los tres bocetos se generan con `python recetas/clase14_graficos.py` y quedan en `salidas/titulares/`. Sirven de referencia para el dibujo en papel.
