import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import app1
import app2
from app import app

# define the main app layout
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),
        html.Div(id="page-content"),
    ]
)


# change the main app page layout to either app1/app2 layout depending on the pathname
# if the pathname is not defined, use app1 layout
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
)
def display_page(pathname):
    if pathname == "/app1":
        return app1.layout
    elif pathname == "/app2":
        return app2.layout
    else:
        return app1.layout


if __name__ == "__main__":
    app.run_server(
        debug=True,
        host="0.0.0.0",
        port="8080",
    )
