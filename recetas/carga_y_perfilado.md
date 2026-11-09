# Carga de datos y claves

## Clase 4. Residuos

La tabla tiene 1.222 filas y 41 columnas. La ruta de Colab apuntaba a una carpeta que no existe en una copia nueva. Ahora el script baja el CSV de la Intendencia y lo guarda dentro del proyecto. Comparé el archivo oficial con el que se había usado en clase y eran iguales.

Primero miro si `matricula_letra` se repite. Tiene sentido que un vehículo aparezca más de una vez si hace varias pesadas. Para distinguir filas pruebo `pesada` y chequeo tanto repetidos como nulos. El perfil también muestra tipos, faltantes y valores extremos.

## Clase 5. Playas

En el notebook original había 27.166 filas y 12 columnas. La copia del CSV en el repo estaba vacía. Al volver a bajarlo de la Intendencia obtuve 27.284 filas y 12 columnas en octubre. La fuente se actualiza, así que ese número puede volver a cambiar.

Probé juntar `fecha_muestra` con `desc_abreviada_punto` porque importa cuándo y dónde se tomó la muestra. Primero reviso que ninguna de las dos tenga nulos y después veo si alguna combinación se repite. Una clave que funciona en la descarga de hoy puede necesitar otra columna si en el futuro hay más de una medición por punto y fecha.

**Extra por curiosidad.** Ordené las playas por salinidad media y agregué cuántas mediciones entraron en cada promedio. Una playa con pocas muestras puede quedar alta o baja por las fechas en que se midió.

[Código](carga_y_perfilado.py) · [Fuentes](../datos/FUENTES.md)
