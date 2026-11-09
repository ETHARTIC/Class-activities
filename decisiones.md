# Registro de decisiones

Decisiones adoptadas o formalizadas en la regularización del 27/10/2026.
No se atribuyen retrospectivamente a las clases si no hay evidencia.

| Decisión | Alternativa descartada | Motivo y efecto |
|---|---|---|
| Conservar ocho objetos propios y diez didácticos separados | Presentarlos como un solo relevamiento | Evita atribuir mediciones ajenas o ficticias al trabajo propio. |
| Construir rutas desde la raíz del proyecto | Mantener C:/Users/... o /content/... | Permite ejecutar en otra computadora. |
| Usar la fuente oficial de playas y registrar la versión | Dar por válido el CSV vacío o copiar resultados viejos como nuevos | La fuente actual cambió: se distinguen 27.166 filas históricas y 27.284 verificadas ahora. |
| Exigir no nulos y unicidad a una clave candidata | Contar solo valores distintos | Una clave con nulos no identifica todas las filas. |
| Declarar tipos nominales y ordinales | Confiar en tipos inferidos del CSV | Conserva el significado y orden de la medición. |
| Tratar -99 y s/d como faltantes documentados | Incluir -99 en la media | Evita sesgar un resumen por una codificación de ausencia. |
| Conservar 0 aristas como medición válida | Usar 0 para desconocido | Distingue ausencia observada de falta de información. |
| Revisar tipos tras leer Parquet | Suponer que todos los categóricos sobreviven | En esta versión, certeza numérica necesita reconstrucción. |
| Corregir miles y espacios antes de resumir | Aceptar una lectura sin errores como correcta | Repara montos y categorías sin modificar el crudo. |
| Tomar seis horas con mayor media en Tres Cruces entre semana | Elegir visualmente horas sin regla escrita | Define una clasificación explícita y reproducible, limitada al período. |
| Comparar modelos sobre las mismas filas | Comparar R² sin comprobar n | Evita confundir mejora de ajuste con cambio de muestra. |
| Leer solo train.csv para RSNA | Descargar toda la competencia y sus imágenes | El gráfico requiere etiquetas, no todas las imágenes; no se eluden las condiciones de Kaggle. |
| No versionar nuevas copias de crudos ni salidas | Subir CSV, imágenes de estudios y gráficos regenerables | Sigue la pauta del curso y mantiene origen y obtención en código. |
| Retirar la carpeta de claves de la versión actual | Conservar credenciales como material de clase | No se leyeron ni usaron esas claves. Su revocación queda a cargo del titular si son reales. |
| Reconstruir el diario solo con evidencia y fecha de elaboración | Crear commits con fechas pasadas o inventar dificultades | Conserva el historial real y hace visibles los huecos. |
