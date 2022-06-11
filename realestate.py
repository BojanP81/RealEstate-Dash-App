from dash import dcc, html, Input, Output, callback
from pages import page1, page2
import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.VAPOR],
                meta_tags=[
                    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
                ],
                suppress_callback_exceptions=True)
page1.init_callbacks(app)
page2.init_callbacks1(app)
app.title = 'RealEstatePulaApp.'
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@callback(Output('page-content', 'children'),
          Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return page1.layout
    elif pathname == '/page2':
        return page2.layout
    elif pathname == '/page1':
        return page1.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=False)
