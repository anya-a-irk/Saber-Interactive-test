from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from datetime import date
import req

app = Dash(__name__)
all_currency = req.get_assets_symbol()
currency_dict = req.get_assets()

app.layout = html.Div([
    # html.H4(" cryptocurrencies"),
    html.Div([
        "Select an asset:",
        dcc.Dropdown(
            all_currency,
            all_currency[0],
            id='my-input')
    ]),
    dcc.DatePickerRange(
        id='my-date-picker-range',
        # min_date_allowed=date(2020, 8, 5),
        # max_date_allowed=date(2023, 1, 25),
        # initial_visible_month=date(2022, 12, 25),
        start_date=date(2022, 12, 25),
        end_date=date(2023, 1, 25)
    ),
    html.Div(id='output-container-date-picker-range'),
    html.Br(),
    html.Div(id='my-output'),
    dcc.Graph(
        id='example-graph',
    )
])


@app.callback(
    Output(component_id='example-graph', component_property='figure'),
    Input(component_id='my-input', component_property='value'),
    Input(component_id='my-date-picker-range', component_property='start_date'),
    Input(component_id='my-date-picker-range', component_property='end_date')
)
def update_output_div(input_value, start_date, end_date):
    df = req.get_df(currency_dict[input_value], start_date, end_date)
    fig = px.line(df, x="time", y="price")
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
