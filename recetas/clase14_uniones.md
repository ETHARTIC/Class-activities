# Unir tablas (ejercicios 58 a 61)

## 58. Vuelos y aerolíneas

| Vuelo | carrier | Aerolínea |
|---:|---|---|
| 1 | UA | United Air Lines Inc. |
| 2 | AA | American Airlines Inc. |
| 3 | B6 | JetBlue Airways |
| 4 | UA | United Air Lines Inc. |
| 5 | DL | NA |

Con `left` quedan 5 vuelos. Con `inner` quedan 4. Sale el vuelo 5 porque no hay una fila para DL en la tabla de aerolíneas. UA aparece en dos vuelos y en una sola fila de aerolíneas, así que a los dos les toca el mismo nombre.

## 59. Vuelos y destinos

La clave es `dest` en vuelos y `faa` en aeropuertos. Los dos guardan el código del aeropuerto.

| Vuelo | dest | Aeropuerto |
|---:|---|---|
| 1 | IAH | George Bush Intercontinental |
| 2 | MIA | Miami Intl |
| 3 | SJU | NA |
| 4 | ORD | Chicago Ohare Intl |
| 5 | ATL | Hartsfield Jackson Atlanta Intl |

Con `inner` quedan 4 vuelos. El vuelo 3 pierde la coincidencia porque SJU falta en aeropuertos. Si junto las tres tablas, pondría `nombre_aerolinea` y `nombre_destino` en lugar de dejar dos columnas `name`.

## 60. Aeropuerto y hora

Con `origin` y `hour` quedan **3 filas**. Si uso solo `origin`, quedan **6**.

| Vuelo | origin | Hora vuelo | Hora clima | Visibilidad (millas) |
|---:|---|---:|---:|---:|
| 1 | EWR | 5 | 5 | 10 |
| 1 | EWR | 5 | 6 | 2 |
| 2 | EWR | 6 | 5 | 10 |
| 2 | EWR | 6 | 6 | 2 |
| 3 | JFK | 5 | 5 | 10 |
| 3 | JFK | 5 | 6 | 0,5 |

Uso la clave de dos columnas para tomar el clima de la hora de salida. Con solo aeropuerto cada vuelo queda asociado a dos horas, incluso a una que no le corresponde.

Si saco JFK a las 5 de la tabla de clima, `left` mantiene los 3 vuelos y deja la visibilidad del 3 en NA. `inner` deja 2 vuelos.

## 61. Cuántas filas quedan

| Unión | Filas | Comparado con 27.004 |
|---|---:|---|
| A | 27.004 | Igual |
| B | 26.324 | Menos |
| C | 646.428 | Más |
| D | 27.004 | Igual |

- En B se pierden **680 vuelos**.
- En C, 646.428 / 27.004 = **23,94** filas por vuelo en promedio. Falta la hora en la clave del clima y se cruzan las horas disponibles del día.
- En D, `left` mantiene 27.004 filas. Con `inner` quedarían **22.525** porque 4.479 no tienen avión asociado.
- Para calcular antigüedad puedo usar los vuelos con avión identificado. Con `left` puedo contar cuántos quedaron sin coincidencia y mirar si se concentran en ciertas aerolíneas antes de generalizar el resultado.

[Consigna](https://github.com/DavytJ/Introduccion-a-la-ciencia-de-datos/blob/56e76c472cf1ec67291eacdf303314eae0218027/clases/clase14/ejercicios_58_61_papel.pdf) · [Soluciones de clase](https://github.com/DavytJ/Introduccion-a-la-ciencia-de-datos/blob/56e76c472cf1ec67291eacdf303314eae0218027/clases/clase14/soluciones_58_61_papel.pdf)
