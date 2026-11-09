# Caja negra: los ocho objetos propios

Fuente: `Actividades-de-clase/data/Objetos_a_ciegas.ipynb`, incorporado el 20/08/2026.
El notebook registra ocho objetos y seis atributos binarios: movimiento, blando,
flexible, plástico, metal y liso. No es el dataset de diez filas que trae el
práctico docente: se conservan ambos casos por separado.

Una fila representa un objeto registrado. `objeto` funciona como identificador
candidato en estas ocho filas; no demuestra que los nombres sirvan como clave
para futuros relevamientos. Los seis atributos se codifican 1 = presencia y
0 = ausencia observada. No son categorías excluyentes: un objeto puede ser
flexible y de plástico al mismo tiempo.

El proceso generador incluye el objeto, lo que se alcanzó a observar, la
interpretación y la codificación. El notebook no documenta el instrumento ni el
tiempo exacto de la medición propia: esos datos no se completan por suposición.
Tampoco se reemplaza un atributo desconocido por 0.

El script `objetos_a_ciegas.py` recupera el diccionario literal del notebook,
comprueba ocho filas y atributos 0/1, y calcula frecuencias. Estas describen los
ocho objetos; no son proporciones representativas de una población de objetos.
