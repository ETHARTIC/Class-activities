# Preguntas del PDF original sobre errores

Fuente: `Actividades-de-clase/doc/preguntas multiple opcion.pdf`, ya presente en
el repositorio. Respuestas añadidas el 27/10/2026. No había respuestas marcadas
visibles en el texto extraído. Los ejemplos específicos de R no se ejecutaron
en este entorno; se explican según las consignas y el material de clase.

| Nº | Opción | Explicación |
|---|---|---|
| 1 | b | Si no se creó df en R, ese nombre puede resolver a una función; una función no se indexa como tabla. |
| 2 | b | Ambos fallan al convertir “45,0”; Python corta con ValueError y R produce NA y una advertencia. |
| 3 | b | datos$pesos puede devolver NULL si la columna no existe; sum(NULL) devuelve 0, sin demostrar que los pesos reales sumen cero. |
| 4 | b | La media de pandas omite faltantes por defecto; mean() de R necesita na.rm=TRUE. |
| 5 | b | La fila tiene más campos que los esperados según la estructura interpretada; inspeccionar el delimitador y las comillas. |
| 6 | b | Se intentó decodificar como UTF-8 un archivo con otra codificación. No cambiarla a ciegas: revisar el origen. |
| 7 | b | Acceder fuera del largo de ese vector de R devuelve NA; no equivale al IndexError de una lista de Python. |
| 8 | b | El operador $ de R admite coincidencias parciales no ambiguas; es preferible una selección exacta para evitar errores silenciosos. |
| 9 | b | En el caso planteado, se descartó el resultado de dropna(); asignarlo a un nombre conserva la tabla filtrada. |
| 10 | b | Python delimita bloques con indentación; R usa llaves. |
| 11 | b | El signo + suele indicar una expresión incompleta. Cancelar y revisar comillas, paréntesis o llaves. |
| 12 | b | R recicla el vector corto y, si las longitudes son múltiplos, no avisa. Resultado: 2, 4, 4, 6. |

En un caso real, df sin cambios tras dropna() también puede significar que no
había faltantes: hay que inspeccionar la tabla. La opción 9 responde al mecanismo
que busca el ejercicio; no convierte cualquier observación similar en un diagnóstico único.
