# Errores que aparecieron

| Qué vi | Cómo lo revisé y qué cambié |
|---|---|
| El script buscaba el CSV en la carpeta de la profe o en Colab | Revisé la ruta y la armé desde el proyecto. |
| El CSV de playas estaba vacío | Lo abrí y solo tenía un salto de línea. Volví a descargarlo de la Intendencia. |
| Faltaba `matricula_letra` en playas | Ese nombre era de otra tabla. Revisé las columnas y probé fecha + punto. |
| Una supuesta clave podía tener nulos | Agregué el chequeo de nulos además del de repetidos. |
| El CSV tenía una columna `Unnamed: 0` | Era el índice que se guardó con la tabla. Al exportar uso `index=False`. |
| `UnicodeDecodeError` al abrir el CSV de Excel | El archivo estaba en latin-1. Declaré codificación, separador y decimal. |
| El peso quedó como texto sin tirar error | Miré `dtypes` y agregué `decimal=","`. |
| El peso medio me daba 48,45 g | Había dos −99 que indicaban faltantes. Después de marcarlos como NA dio 85,3125 g. |
| El monto medio daba 169,28 UYU | Pandas había leído el punto de miles como decimal. Con `thousands="."` dio 1.471,5 UYU. |
| Certeza volvió como entero al leer Parquet | Comparé los tipos y restauré el orden de 1 a 5. |
| El clima duplicaba vuelos | Faltaba `hour` en la clave. Al sumar la hora volvía a tener una fila por vuelo. |
| El OCR confundió encabezados del ticket | Contrasté los ítems con la foto y la suma con el total. |
| El notebook de rodilla pedía descargar toda la competencia | Separé el caso con `train.csv` y el gráfico que se recupera del notebook anterior. |
