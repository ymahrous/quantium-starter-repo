import dash
import pandas as pd
from dash import dcc, html
import plotly.express as px

df = pd.read_csv("data/formatted_sales_data.csv")
df['sales'] = pd.to_numeric(df['sales'])
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# sales data sorted by date
daily_sales = df.groupby('date')['sales'].sum().reset_index()
fig = px.line(
    daily_sales,
    x='date',
    y='sales',
    title='Daily Sales Over Time'
)

fig.add_shape(
    type="line",
    x0=pd.Timestamp('2021-01-15'),
    x1=pd.Timestamp('2021-01-15'),
    y0=0,
    y1=1,
    xref='x',
    yref='paper',
    line=dict(color="red", dash="dash"),
)

# Add annotation manually
fig.add_annotation(
    x=pd.Timestamp('2021-01-15'),
    y=max(daily_sales['sales']),
    text="Price Increase (Jan 15, 2021)",
    showarrow=True,
    arrowhead=2,
    ax=40,
    ay=-40
)

# create dash app
app = dash.Dash(__name__)
app.layout = html.Div(children=[
    html.H1("Soul Foods - Sales Visualiser"),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)