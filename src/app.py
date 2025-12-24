from dash import Dash, dash_table, dcc, html, callback, Output, Input, State, MATCH
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from flask import Flask

server = Flask(__name__)

app = Dash(
    __name__,
    server=server,
    url_base_pathname='/',
    pages_folder='./src',
    use_pages=True,    # turn on Dash pages
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        dbc.icons.FONT_AWESOME
    ],  # fetch the proper css items we want
    meta_tags=[
        {   # mobile scaling
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1'
        }
    ],
    suppress_callback_exceptions=True,
    title='One Stop Stock Analysis'
)

def serve_layout():
    '''Define the layout of the application'''
    return html.Div(
        [
            html.H4(['Analysing tweets and blockchain data']),
            html.H4(['Analysing tweets and blockchain data']),

        ]
    )


app.layout = serve_layout   # set the layout to the serve_layout function
server = app.server         # the server is needed to deploy the application

if __name__ == '__main__':
    app.run(debug=True, port=8050)