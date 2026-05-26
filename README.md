# Actividad-DASHboards-y-Plotly_A00573129

## Integrante

| Nombre | Matrícula |
|--------|-----------|
| Eugenio Sánchez Velázquez | A00573129 |

## Descripción

Proyecto de visualización de datos usando un dataset de ventas de café. Se trabajó con Plotly para generar 10 gráficas distintas dentro de un Google Colab Notebook y con Dash para crear un dashboard interactivo que permite explorar las mismas gráficas desde un dropdown.

## Dataset

El archivo `Coffe_sales.csv` contiene registros de ventas de una cafetería. Cada fila es una transacción con datos como el tipo de café, el monto, la hora, el día de la semana y el mes.

## Archivos

- `Actividad_DASHboards_y_Plotly_Borrador.ipynb` — Notebook de Google Colab con las 10 gráficas en Plotly, paletas de color personalizadas y descripciones de cada visualización.
- `act_dash_plotly_A00573129.py` — Dashboard en Dash con un dropdown para seleccionar entre las 10 gráficas. Incluye descripción dinámica debajo de cada una.
- `Coffe_sales.csv` — Dataset utilizado.

## Paletas de color

Se definieron esquemas de color personalizados basados en los colores de Instagram:

- **Logo** — `#F207B2`, `#F8F3F2`, `#FBAD06`, `#FA5014`, `#FA0D5C`, `#940CF5`
- **Monocromática** — `#7b0002`, `#9e011e`, `#c20436`, `#e70a4f`, `#fd396a`, `#ff6588`, `#ff87a7`, `#ffa6c7`
- **Complementaria** — `#FA0D5C`, `#0dfaab`
- **Análoga** — `#fa0d5c`, `#fa340d`, `#fa0dd2`
- **Tríada** — `#fa0d5c`, `#5cfa0d`, `#0d5cfa`
- **Complementarios divididos** — `#fa0d5c`, `#fada0d`, `#0dbbfa`

## Gráficas

1. Barras — ventas totales por tipo de café
2. Histograma con rug — distribución de montos por momento del día
3. Scatter — hora del día vs monto
4. Box plot — precios por tipo de café
5. Strip chart — ventas por día de la semana
6. Sunburst — desglose jerárquico de ventas
7. Treemap — proporción de ventas por café y día
8. Líneas (go.Figure) — ventas mensuales de tres cafés
9. Coordenadas paralelas — vista numérica multivariable
10. Categorías paralelas — flujo entre café, día y momento

## Cómo correr el dashboard

1. Tener instalado Python(la extensión de Visual Studio) y Visual Studio Code
2. Abrir Visual Studio Code y abrir la carpeta donde están los archivos del proyecto
3. Abrir la terminal dentro de VS Code (Terminal, después a New Terminal o usar el comando Ctrl + Ñ)
4. Instalar las librerías necesarias escribiendo en la terminal: `pip install dash dash-bootstrap-components plotly pandas`
5. Asegurarse de que `Coffe_sales.csv` esté en la misma carpeta que `act_dash_plotly_A00573129.py`
6. Correr el archivo escribiendo en la terminal: `python act_dash_plotly_A00573129.py`
7. Va a aparecer un mensaje diciendo que el servidor está corriendo. Abrir el navegador e ir a `http://localhost:8051`
8. Para detener el dashboard, regresar a la terminal y presionar Ctrl + C
