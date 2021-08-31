import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from navbar import Navbar
from layouts import bancoLayout, spsLayout, resLayout
import callbacks
from app import app
from app import server as server


# Layout variables, navbar, header, content, and container
nav = Navbar()

header = dbc.Row(
    dbc.Col(
        ),className='banner')

content = html.Div([
    dcc.Location(id='url'),
    html.Div(id='page-content')
])

container = dbc.Container([
    header,
    content,
])


# Menu callback, set and return
# Declair function  that connects other pages with content to container
@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == 'https://sps-cie-imss.herokuapp.com/':
#        return html.Div([
#        html.Iframe(src='assets/SP.html', width='100%', height='1400', 
#                style={'border':'none'},
#                )
#        ],className='home')
    if pathname == '/banco':
        return bancoLayout
#    elif pathname == '/antecedente':
#        return spsLayout
    elif pathname == '/res':
        return resLayout
    else:
        return 'Página en construcción!'


# Main index function that will call and return all layout variables
def index():
    layout = html.Div([
            nav,
            container
        ])
    return layout

# Set layout to index function
app.layout = index()

# Call app server
if __name__ == '__main__':
    # set debug to false when deploying app
    app.run_server()
    



