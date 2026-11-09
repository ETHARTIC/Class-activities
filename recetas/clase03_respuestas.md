# Clase 3 — crear un dataset y volver a cargarlo

Resolución del 27/10/2026. Consignas: clase3/ejercicios.py y
los prácticos A/B del repositorio docente. Se utilizan sus diez observaciones
didácticas, no se inventan mediciones propias. Ejecutar `datos/generar_caja.py`
y `recetas/clase03_crear_y_cargar.py`.

## 1. Tipos y significado del cero

Textura es nominal; rigidez y certeza son ordinales. Rigidez se ordena como
blando < medio < rígido; certeza conserva los niveles 1–5 aunque no aparezca el 1.
Hay seis objetos por encima de blando. El peso es continuo, las aristas son un
conteo y objeto_id es un identificador, aunque se almacene como entero.

Una esfera tiene cero aristas: en un conteo bien definido, ese 0 es una medición
válida. Si el observador no pudo contarlas, el valor es desconocido y debe
registrarse como faltante. “No aplica” solo corresponde si la definición del
instrumento realmente excluye esa observación; no equivale automáticamente a cero.

## 2. Restricciones ejecutables

Se comprueban pesos positivos, certeza entera entre 1 y 5, aristas enteras no
negativas y objeto_id único y no nulo. `validar_caja` devuelve todos los problemas
juntos. La tabla limpia produce cero problemas y la copia con peso negativo,
aristas negativas e identificador repetido produce tres. No se corrigen los
datos silenciosamente para hacer pasar la validación.

## 3. Diccionario de variables

Se genera una tabla de seis filas y seis columnas: variable, tipo, unidad,
instrumento, rango válido y faltante. El instrumento describe el procedimiento,
no solo el significado. Las columnas `rango_valido` y `faltante` aclaran que 0
aristas es válido y que desconocido se deja vacío. Esa distinción evita el error.

## 4. CSV y Parquet

Guardar CSV con el índice agrega `Unnamed: 0` al volver a leerlo. Se corrige con
`index=False`. El CSV tampoco conserva el orden de rigidez: hay que declararlo
al leer. Parquet sí conservó rigidez como categórica ordenada en la verificación.

Se detectó un matiz real: con pandas 2.2.3 y pyarrow 26.0.0 la certeza categórica
numérica volvió como int64. Los valores se conservaron, pero hubo que reconstruir
su escala ordinal. Por eso se comprueban valores **y tipos** después de guardar;
no se afirma que cualquier formato preserve siempre todo.

## 5. El CSV de Excel

Mensaje completo obtenido en esta ejecución:

```text
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xed in position 107: invalid continuation byte
```

El archivo usa latin-1, punto y coma entre columnas y coma decimal. La lectura
correcta declara `encoding="latin-1", sep=";", decimal=","`. Sin declarar el
decimal, el archivo se lee, pero peso queda como texto: es un error silencioso.
El texto exacto del error también se regenera en `salidas/clase03/error_lectura.txt`.

## 6. Dónde está el archivo

Una ruta con el usuario y las carpetas de la profesora presupone una ubicación
que no existe en otra computadora. La solución obtiene la raíz a partir de
`__file__`, construye la ruta con Path y comprueba existencia. El práctico se
verificó desde la raíz y desde otra carpeta.

## 7. Faltantes disfrazados

Los códigos son -99, s/d, NA y celda vacía. Pandas reconoce NA y vacío por
defecto; los otros se declaran con `na_values`. El promedio ingenuo de peso es
48,45 g; después de tratar los dos -99 como faltantes es 85,3125 g.

La confusión es de representación de una ausencia: el código ejecutaba una
operación válida sobre valores con significado incorrecto. Se resuelve con el
diccionario y la lectura. El promedio corregido describe los pesos observados,
no demuestra que los datos falten al azar ni estima los valores ausentes.

## 8. Archivo del equipo vecino

Se declaran los miles con `thousands="."`, se normalizan los nombres, se convierte
la fecha con `%d/%m/%Y` y se quitan espacios de sucursal. Las cuatro etiquetas
originales de sucursal quedan en tres categorías. La media de monto pasa de
169,278525 a 1.471,5 UYU. El parseo se contrastó con una conversión independiente
del texto quitando los puntos de miles.

Tres afirmaciones sustentadas por el archivo: registra transacciones con un
identificador por fila; guarda fechas como día/mes/año; codifica montos en UYU con
puntos de miles y sucursales con espacios inconsistentes. Pregunta al productor:
¿el monto es el total final de cada transacción, incluye impuestos y devoluciones,
y el ID garantiza una operación única? El contenido solo no alcanza para decidirlo.

## Desafío por equipo

Falta confirmar cuál es la estructura asignada al equipo. No se da por completado
este desafío con un dataset inventado ni con el caso didáctico de caja negra.
