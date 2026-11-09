# Bitácora personal — Ethan / ETHARTIC

Introducción a la Ciencia de Datos · Universidad de Montevideo · 2026.

Esta bitácora reúne los trabajos de clase, las correcciones y las decisiones que
permiten repetirlos. La organización se regularizó el **27/10/2026**. Las fechas de los commits anteriores
se conservan. Las resoluciones nuevas no se presentan como entregas hechas antes.

## Por dónde empezar

- [Estado de cada actividad y pendientes](ESTADO.md).
- [Diario y cronología comprobable](diario/README.md).
- [Decisiones de limpieza y método](decisiones.md).
- [Errores encontrados y cómo se corrigieron](errores/registro.md).
- [Qué se ejecutó y qué falta verificar](VALIDACION.md).

## Actividades y respuestas

| Bloque | Trabajo y explicación |
|---|---|
| Caja negra propia | [Ocho objetos y medición](recetas/objetos_a_ciegas.md) · [código](recetas/objetos_a_ciegas.py) |
| Fundamentos | [12 respuestas justificadas](recetas/fundamentos.md) |
| Crear y volver a cargar | [Ocho respuestas y resultados](recetas/clase03_respuestas.md) · [código](recetas/clase03_crear_y_cargar.py) |
| Carga y perfilado | [Residuos y playas](recetas/carga_y_perfilado.md) · [código](recetas/carga_y_perfilado.py) |
| Encuestas | [Cuestionario y seis correcciones](recetas/encuestas.md) |
| Visualización RSNA | [Notebook corregido](Actividades-de-clase/scripts/trabajo-creacion-grafico.ipynb) · falta recuperar train.csv |
| IA y extracción de datos, clase 11 | [Procedimiento de validación y alcance](recetas/ia_y_validacion.md) |
| Tránsito y aire | [Siete respuestas y resultados](recetas/transito_resultados.md) · [práctico resuelto](<Actividades-de-clase/scripts/clase12_ejercicios(1).py>) |
| Preguntas y series, clase 14 | [Notas y actividad de tarjetas](recetas/clase14_preguntas_y_series.md) · [código de series](recetas/clase14_series.py) |
| Errores de programación | [12 respuestas del PDF original](recetas/errores_opcion_multiple.md) |
| Recetas complementarias | [Flujo, transformaciones, uniones, gráficos y series](recetas/flujo_y_visualizacion.md) |

## Cómo reproducir

Python 3.11 o superior, desde una copia local del repositorio:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
python3 verificar.py
```

En Windows, activar con `.venv\Scripts\activate` y usar `python` si corresponde.
La primera ejecución descarga los CSV necesarios desde las fuentes documentadas;
no requiere claves de IA. Con los archivos en caché, los prácticos funcionan sin red.
`verificar.py` genera tablas y gráficos en `salidas/`, comprueba los resultados y
contrasta las regresiones con una matriz calculada mediante NumPy.

Para recuperar solo una fuente: `python3 datos/obtener.py playas`. Para actualizar
una descarga: `python3 datos/obtener.py playas --actualizar`.
El archivo de playas se actualiza en origen: su cantidad de filas puede cambiar.

## Organización

- `diario/`: entradas basadas en evidencia del historial y regularización actual.
- `funciones/`: utilidades documentadas y con casos de prueba.
- `recetas/`: soluciones y procedimientos reutilizables.
- `errores/`: diagnóstico, manifestación y corrección de problemas reales.
- `datos/`: código para obtener o generar los datos; crudos y generados ignorados por Git.
- `Actividades-de-clase/`: ubicación conservada para los trabajos originales, con rutas corregidas.
- `salidas/`: se regenera al ejecutar; no se versiona.

## Fuentes y alcance

Referencia principal: [repositorio de Joselina Davyt](https://github.com/DavytJ/Introduccion-a-la-ciencia-de-datos),
versión `ee2f4a1e1eb4fb2bd6e38d3b8ec85a73867f6dff`.
Las consignas y la preparación del práctico de tránsito provienen de la docente.
El generador de caja se adaptó de su material, con atribución en el código.
[Fuentes de datos](datos/FUENTES.md).

El programa pide una bitácora **privada**, con acceso de lectura para la docente.
La visibilidad y el acceso deben verificarse en Settings. La regularización no
reemplaza los commits semanales que faltan ni acredita participación no documentada.
