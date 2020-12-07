import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
import app1
import app2


app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/app1":
        return app1.layout
    elif pathname == "/app2":
        return app2.layout
    else:
        return app2.layout


if __name__ == "__main__":
    app.run_server(debug=True)
