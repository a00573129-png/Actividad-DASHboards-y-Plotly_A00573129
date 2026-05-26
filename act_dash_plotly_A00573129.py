from dash import Dash, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Datos
df = pd.read_csv('Coffe_sales.csv')

# Paletas de colores (Instagram)
logo = ['#F207B2', '#F8F3F2', '#FBAD06', '#FA5014', '#FA0D5C', '#940CF5']
monocromatico = ['#7b0002', '#9e011e', '#c20436', '#e70a4f', '#fd396a', '#ff6588', '#ff87a7', '#ffa6c7']
complementario = ['#FA0D5C', '#0dfaab']
analogo = ['#fa0d5c', '#fa340d', '#fa0dd2']
triada = ['#fa0d5c', '#5cfa0d', '#0d5cfa']
complementarios_divididos = ['#fa0d5c', '#fada0d', '#0dbbfa']

#################### APLICACION
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

### Componente entrada
dropdown = dcc.Dropdown(
    options=['Barras', 'Histograma', 'Scatter', 'Box Plot', 'Strip',
             'Sunburst', 'Treemap', 'Líneas', 'Coord. Paralelas', 'Cat. Paralelas'],
    value='Barras', clearable=False)

### Componentes salida
md_name = dcc.Markdown(children='**Dashboard hecho por Eugenio Sánchez Velázquez**')
md_title = dcc.Markdown(children='')
grafica = dcc.Graph(figure={})

# Layout
app.layout = dbc.Container([md_name, dropdown, grafica, md_title])

### Callback
@app.callback(
    Output(grafica, component_property='figure'),
    Output(md_title, component_property='children'),
    Input(dropdown, component_property='value')
)
def update(user_input):

    if user_input == 'Barras':
        ventas_cafe = df.groupby('coffee_name')['money'].sum().reset_index()
        fig = px.bar(ventas_cafe, x='coffee_name', y='money',
                     color='coffee_name',
                     color_discrete_sequence=monocromatico,
                     title='Ventas Totales por Tipo de Café')
        description = 'Descripción: esta es una gráfica de barras que muestra las ventas totales en pesos por cada tipo de café.Primero agrupé todas las transacciones y luego se sumó el monto. Se puede ver que el Americano with Milk y el Latte son los que más venden, mientras que el Espresso es el que menos.'

    elif user_input == 'Histograma':
        fig = px.histogram(df, x='money',
                          marginal='rug',
                          color='Time_of_Day',
                          hover_data=['coffee_name', 'Weekday'],
                          color_discrete_sequence=triada,
                          title='Distribución de Montos por Momento del Día')
        description = 'Descripción: Realicé un histogram que muestra cómo se distribuyen los montos de las ventas, separados por momento del día (Morning, Afternoon, Night). El rug plot de arriba permite ver cada transacción individual como una rayita. Se nota que los montos se concentran en valores muy específicos, lo cual tiene sentido porque cada café tiene su precio fijo. Hice uso de la paleta triada'

    elif user_input == 'Scatter':
        fig = px.scatter(df, x='hour_of_day', y='money',
                        color='coffee_name',
                        hover_data=['Weekday', 'Time_of_Day'],
                        opacity=0.5,
                        color_discrete_sequence=logo,
                        title='Hora del Día vs Monto por Tipo de Café')
        description = 'Descripción: Hice un Scatter plot donde cada punto es una venta. En el eje X está la hora y en el Y el monto. El color diferencia el tipo de café. Se puede ver que la mayoría de las ventas se concentran entre las 10am y las 2pm, que son las horas donde más gente compra café. Si pasas el mouse encima se ve el día y el momento del día y aquí usé la paleta del logo original'

    elif user_input == 'Box Plot':
        fig = px.box(df, x='coffee_name', y='money',
                    color='coffee_name',
                    hover_data=['Weekday', 'hour_of_day'],
                    color_discrete_sequence=monocromatico,
                    title='Distribución de Precios por Tipo de Café')
        description = 'Descripción: La siguiente gráfica es un box plot que muestra el rango de precios de cada tipo de café. Las cajas salen muy compactas porque cada producto tiene un precio fijo, entonces no hay mucha variación. Lo útil aquí es ver rápidamente cuál es el más caro (Latte y Hot Chocolate) y cuál el más barato (Espresso). En el hover se puede ver el día y la hora de cada venta.'

    elif user_input == 'Strip':
        fig = px.strip(df, x='Weekday', y='money',
                      color='Time_of_Day',
                      hover_data=['coffee_name'],
                      color_discrete_sequence=triada,
                      category_orders={'Weekday': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']},
                      title='Ventas por día de la semana')
        description = 'Descripción: Usé un strip chart porque es más fácil de visualizar ya que pone cada venta como un punto, organizado por día de la semana. El color separa mañana, tarde y noche. Se ve que entre semana hay más densidad de puntos que el fin de semana, especialmente los lunes y martes. También se nota que en la mañana es cuando más ventas hay.'

    elif user_input == 'Sunburst':
        fig = px.sunburst(df, path=['Time_of_Day', 'Weekday', 'coffee_name'],
                         values='money', color='money',
                         color_continuous_scale=logo,
                         title='Desglose de ventas')
        description = ' **Descripción**: Esta gráfica es la más confusa pero es un sunburst que desglosa las ventas en tres niveles: primero por momento del día, luego por día de la semana y al final por tipo de café y se le puede dar click a cada sección para explorar más a detalle. El color va según el monto vendido. Se ve que la tarde es el momento con más ventas acumuladas.'

    elif user_input == 'Treemap':
        fig = px.treemap(df, path=['coffee_name', 'Weekday'],
                        values='money', color='money',
                        color_continuous_scale=monocromatico,
                        title='Ventas por café y día')
        description = 'Descripción :Realicé un treemap que muestra las ventas agrupadas por tipo de café y después por el día. El tamaño de cada cuadro es proporcional a cuánto se vendió. De un vistazo se puede ver que el Americano with Milk domina bastante, seguido del Latte.'

    elif user_input == 'Líneas':
        ventas_mes = df.groupby(['Monthsort', 'coffee_name'])['money'].sum().reset_index()
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=ventas_mes[ventas_mes['coffee_name'] == 'Latte']['Monthsort'],
                                 y=ventas_mes[ventas_mes['coffee_name'] == 'Latte']['money'], name='Latte'))
        fig.add_trace(go.Scatter(x=ventas_mes[ventas_mes['coffee_name'] == 'Americano']['Monthsort'],
                                 y=ventas_mes[ventas_mes['coffee_name'] == 'Americano']['money'], name='Americano'))
        fig.add_trace(go.Scatter(x=ventas_mes[ventas_mes['coffee_name'] == 'Cappuccino']['Monthsort'],
                                 y=ventas_mes[ventas_mes['coffee_name'] == 'Cappuccino']['money'], name='Cappuccino',
                                 line=dict(color='#FA0D5C', width=4, dash='dot')))
        fig.update_layout(
            title='Ventas mensuales por café', xaxis_title='Mes', yaxis_title='Venta ($)')
        description = 'Realicé una gráfica de líneas(varias) con graphic objects que compara las ventas mensuales de tres cafés: Latte, Americano y Cappuccino. La línea del Cappuccino está punteada y en rosa para resaltarla. Se puede ver cómo varían las ventas a lo largo de los meses y si hay algún patrón estacional.'

    elif user_input == 'Coord. Paralelas':
        fig = px.parallel_coordinates(df,
                                      dimensions=['hour_of_day', 'money', 'Monthsort'],
                                      color='money',
                                      color_continuous_scale=monocromatico)
        description = 'Descripción: Esta es otra gráfica confusa pero necesaria. Es una gráfica de coordenadas paralelas que muestra tres variables numéricas al mismo tiempo: hora, monto y mes. Cada línea es una venta y el color va por monto, las más oscuras son las más caras. Sirve para ver si hay alguna relación entre la hora en que se compra y cuánto se gasta.'

    elif user_input == 'Cat. Paralelas':
        fig = px.parallel_categories(df,
                                     dimensions=['coffee_name', 'Weekday', 'Time_of_Day'],
                                     color='money',
                                     color_continuous_scale=monocromatico)
        description = 'Descripción: Esta es otra de las gráficas confusas en plotly que es un gráfico de categorías paralelas que conecta el tipo de café con el día de la semana y el momento del día. Se pueden seguir los flujos(un poco complicado) para ver por ejemplo que los Lattes se venden bastante parejo entre mañana y tarde, o que el Espresso casi no se vende en la noche.'

    return fig, description

# Ejecutar
if __name__ == '__main__':
    app.run(port=8051)