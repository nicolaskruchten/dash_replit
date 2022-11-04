from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

app.layout = html.Div(children=[dcc.Input(id="in"), html.H1(id="out")])


@app.callback(Output('out', 'children'), Input('in', 'value'))
def cb(input_value):
  return f"Hello {input_value or ''}"


app.run_server(host='0.0.0.0', debug=True)
