# Clase 3. Crear y volver a cargar los datos

Usé las 10 observaciones de la consigna. Primero corro `python datos/generar_caja.py` y después `python recetas/clase03_crear_y_cargar.py`.

## 1. Tipos y significado del cero

Textura es nominal. Rigidez tiene un orden: blando, medio, rígido. Certeza también es ordinal y va de 1 a 5 aunque en el archivo falte un nivel. Peso es continuo, aristas es un conteo y `objeto_id` identifica filas. Hay 6 objetos por encima de blando.

Una esfera puede tener 0 aristas y ese 0 cuenta. Si no se pudieron contar, pondría NA. Si el instrumento deja ese objeto fuera de la pregunta, queda como no aplica.

## 2. Revisar que los valores tengan sentido

Chequeo que el peso sea positivo, la certeza un entero de 1 a 5 y las aristas enteras de 0 en adelante. También que el ID esté completo y no se repita. La tabla original pasa todo. Con un peso negativo, aristas negativas y un ID repetido salen tres errores.

## 3. Diccionario de variables

Una fila por variable, con nombre, tipo, unidad, instrumento, rango válido y cómo se marca un faltante. En aristas anoto que 0 es un conteo válido y dejo vacío lo desconocido. En instrumento escribo cómo se midió el atributo.

## 4. Guardar en CSV y Parquet

Si guardo el índice en el CSV, al leer aparece `Unnamed: 0`. Lo saco con `index=False`. El orden de rigidez también se pierde en CSV, así que lo paso de nuevo a categórica ordenada.

Parquet guardó el orden de rigidez, pero en la prueba la certeza volvió como entero. Comparé los valores y los tipos para detectar esa diferencia.

## 5. Leer el CSV que salió de Excel

La primera lectura dio este error:

```text
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xed in position 107: invalid continuation byte
```

Lo pude leer con `encoding="latin-1", sep=";", decimal=","`. Si saco el decimal, el archivo abre igual pero el peso queda como texto. Revisar `dtypes` me avisa aunque pandas no tire error.

## 6. Ruta del archivo

Una ruta con el usuario y la carpeta de otra computadora falla cuando se mueve el proyecto. Uso `Path(__file__)` para ubicar el script y desde ahí armar la ruta. Probé ejecutarlo desde dos carpetas.

## 7. Faltantes

En el CSV hay `-99`, `s/d`, `NA` y celdas vacías. Pandas ya toma NA y vacío como faltantes. Declaro los otros dos con `na_values`. El peso medio pasa de **48,45 g** a **85,3125 g** al sacar los dos −99 del promedio. El segundo valor resume los pesos que sí se midieron.

## 8. Archivo del equipo vecino

Leí el monto con `thousands="."`, pasé la fecha con `%d/%m/%Y` y saqué espacios de los nombres y las sucursales. De cuatro nombres de sucursal quedaron tres. El promedio de monto pasó de **169,278525** a **1.471,5 UYU**. Chequeé el cálculo convirtiendo el texto después de quitar los puntos.

Por lo que veo en el archivo, hay una transacción por fila con un identificador, fechas en día/mes/año y montos en pesos escritos con punto de miles. Le preguntaría al equipo si el monto incluye impuestos y devoluciones y si el ID identifica una operación en todas las sucursales.

[Desafío de 10 observaciones](clase03_desafio.md) · [Código de los ocho ejercicios](clase03_crear_y_cargar.py)
