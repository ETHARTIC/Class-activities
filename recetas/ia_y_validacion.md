# Clase 11. Leer un ticket

Para repetir el práctico usé la foto del material de clase. Pasé la imagen por OCR, miré las líneas que sacó y comparé los números con la foto.

| Descripción | Monto (UYU) |
|---|---:|
| LECHE FRESCA DESC. C | 18,00 |
| PAN FRANCES GR.X UN | 32,00 |

Una fila es un producto. En el CSV queda `18.00` y `32.00`, con punto decimal. Las líneas que dicen cantidad por precio corresponden al mismo producto, así que contarlas de nuevo duplicaría el monto.

**Chequeo con la foto.** 18,00 + 32,00 = **50,00 UYU**, lo mismo que dice en TOTAL. El pago quedó en **48,36 UYU** por un descuento de **1,64 UYU**. Son dos números que responden a preguntas distintas. Para la tabla de productos me quedo con el total antes del descuento.

**Qué falló.** El OCR leyó mal algunos encabezados, pero encontró las dos líneas de productos. Por eso revisé las líneas contra la imagen y usé la suma como otro chequeo. El práctico de clase usa Gemini para extraer el CSV. Esta repetición usa OCR local y el mismo control de montos.

Para generar el CSV desde la imagen, instalar Tesseract y ejecutar `python recetas/leer_ticket.py ruta/al/ticket.jpg`. Queda en `salidas/ticket.csv`.

[Foto de clase](https://github.com/DavytJ/Introduccion-a-la-ciencia-de-datos/blob/56e76c472cf1ec67291eacdf303314eae0218027/clases/clase11/clase_ia/ticket.jpg) · [Ejemplo de Gemini](https://github.com/DavytJ/Introduccion-a-la-ciencia-de-datos/blob/56e76c472cf1ec67291eacdf303314eae0218027/clases/clase11/clase_ia/leer_ticket.py)
