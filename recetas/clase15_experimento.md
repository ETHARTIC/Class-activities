# Clase 15. Comparar grupos

Repetí el ejemplo simulado de la profesora con semilla 123 y 20 filas. La tabla compara grupos y muestra cómo leer las pruebas. Como el código genera las edades y los ingresos con diferencias incorporadas, los resultados describen el ejemplo.

1. **Sexo y tabaquismo.** En el grupo femenino hay 5 de 8 fumadores y en el masculino 5 de 12. Fisher da p = 0,6499. Con estos datos hay bastante incertidumbre sobre la diferencia.
2. **Edad y tabaquismo.** Hay 10 personas por grupo. La edad media es 48,1 años entre fumadores y 35,4 entre no fumadores. Welch da una diferencia de 12,7 años, IC95% de 6,15 a 19,25 y p ≈ 0,001. El generador ya les suma ocho años a los fumadores. Esa diferencia forma parte de cómo se hizo el ejemplo.
3. **Ingreso y educación.** Las medianas por nivel son 35.523, 56.441 y 80.694. Uso mediana y cuartiles porque el ingreso simulado es asimétrico. Kruskal-Wallis da p = 0,0037. Es una prueba global de rangos y habría que hacer comparaciones por pares para ubicar las diferencias.

Para las pruebas usé las **20 filas**. El bootstrap con ruido del script de clase sirve para probar cómo corre el análisis con más filas. Las copias que produce siguen dependiendo de los mismos registros.

[Código para repetirlo](clase15_experimento.py) · [Script de la profesora](https://github.com/DavytJ/Introduccion-a-la-ciencia-de-datos/blob/56e76c472cf1ec67291eacdf303314eae0218027/clases/clase15/analisis_datos_experimento.py)
