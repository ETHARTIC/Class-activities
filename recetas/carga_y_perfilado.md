# Cargar, perfilar y buscar identificadores

## Residuos: clase 4

La actividad original había producido 1.222 filas y 41 columnas. La ruta apuntaba
a `/content/Class-activities` y a una carpeta anterior al movimiento del CSV.
La versión corregida recupera la copia exacta que estaba en el commit `a4ea2f7`
y trabaja desde la raíz del proyecto. Se verificaron nuevamente sus dimensiones.

La presencia de `matricula_letra` no la vuelve un identificador único. Se prueba
su unicidad y se contrasta con `pesada`. La unidad de observación debe confirmarse
con la fuente: el registro parece corresponder a una pesada, no a un vehículo
único. El perfil informa tipos, faltantes, valores distintos y extremos sin
borrar columnas automáticamente porque tengan muchos faltantes.

## Playas: clase 5

El notebook original informa 27.166 filas y 12 columnas. El archivo subido quedó
vacío: no permite regenerar esa salida histórica. Se recuperó la fuente oficial
de la Intendencia; la descarga verificada durante esta revisión contiene
27.284 filas y 12 columnas. Son versiones distintas, no un resultado idéntico.

Una fila corresponde a un registro de muestra/punto según las columnas disponibles.
La fecha se convierte explícitamente. Se evalúa la pareja `fecha_muestra` y
`desc_abreviada_punto` como clave candidata, exigiendo unicidad y no nulos.
Incluso si cumple, se necesita confirmar con la documentación si identifica una
muestra o si una muestra puede tener varias determinaciones.

Se conserva el análisis extra de salinidad por playa, pero se agrega el número
de mediciones que aporta cada promedio. No se interpreta ese ranking como una
propiedad permanente de las playas: pueden cambiar las fechas, la cobertura y
la composición de las observaciones disponibles.

## Regla de trabajo

Primero importar y perfilar; después decidir qué convertir, limpiar o excluir.
Repetir el perfilado tras limpiar. Un ID candidato no se elige solo porque tiene
muchos valores distintos. No se confunden filas repetidas con mediciones válidas
repetidas: hay que definir la unidad de observación.

Código: `recetas/carga_y_perfilado.py`. Utilidades: `funciones/datos.py`.
