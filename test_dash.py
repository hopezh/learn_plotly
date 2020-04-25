import dash
import dash_core_components as dcc
import dash_html_components as html

ext_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(
    __name__, 
    external_stylesheets = ext_stylesheets
)

app.layout = html.Div(children=[
    html.H1(children='Hello Doh...'),
    html.Div(children=
        '''
        Dash, A web application framework for Python
        '''), 
    dcc.Graph(
        id='example_graph', 
        figure={
            'data' : [
                        {'x' : [1, 1, 3],
                         'y' : [4, 1, 9], 
                         'type' : 'bar',
                         'name' : 'SF'}, 
                        {'x' : [1, 5, 3], 
                         'y' : [8, 4, 5], 
                         'type' : 'bar', 
                         'name' : u'Montreal'}, 
                    ], 
            'layout' : {'title' : 'Dash Data Visualization'}
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
