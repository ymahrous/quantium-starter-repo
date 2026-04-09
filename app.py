import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html, Input, Output

df = pd.read_csv("data/formatted_sales_data.csv")
df['sales'] = pd.to_numeric(df['sales'])
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

# create dash app
app = dash.Dash(__name__)
app.layout = html.Div(
    style={
        'font-family': 'Arial, sans-serif',
        'text-align': 'center',
        'background-color': '#f0f8ff',
        'padding': '20px'
    },
    children=[
        html.H1(
            "Soul Foods - Pink Morsels Sales Visualiser",
            style={'color': '#ff4500', 'margin-bottom': '30px'}
        ),
        
        # Radio button for region selection
        html.Div([
            html.Label("Select Region:", style={'font-size': '20px', 'margin-right': '10px'}),
            dcc.RadioItems(
                id='region-selector',
                options=[
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'},
                    {'label': 'All', 'value': 'all'}
                ],
                value='all',
                inline=True,
                inputStyle={"margin-right": "5px", "margin-left": "15px"},
                style={'font-size': '18px'}
            )
        ], style={'margin-bottom': '30px'}),
        
        # Graph
        dcc.Graph(id='sales-line-chart')
    ]
)

@app.callback(Output('sales-line-chart', 'figure'), Input('region-selector', 'value'))
def update_graph(selected_region):
    if selected_region == 'all':
        filtered_df = df
    else:
        filtered_df = df[df['region'].str.lower() == selected_region]
    
    daily_sales = filtered_df.groupby('date')['sales'].sum().reset_index()
    fig = px.line(
        daily_sales,
        x='date',
        y='sales',
        title=f'Daily Sales Over Time ({selected_region.capitalize()})',
        markers=True
    )

    if not daily_sales.empty and pd.Timestamp('2021-01-15') in daily_sales['date'].values:
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
        fig.add_annotation(
            x=pd.Timestamp('2021-01-15'),
            y=max(daily_sales['sales']),
            text="Price Increase (Jan 15, 2021)",
            showarrow=True,
            arrowhead=2,
            ax=40,
            ay=-40
        )
    
    fig.update_layout(
        plot_bgcolor='#ffffff',
        paper_bgcolor='#f0f8ff',
        font=dict(color='#333333'),
        title_font_size=22
    )
    return fig

if __name__ == '__main__':
    app.run(debug=True)