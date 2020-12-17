import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import loginPage
import selectorPage;
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
        return loginPage.layout
    elif pathname == "/app2":
        return selectorPage.layout
    else:
        return selectorPage.layout


if __name__ == "__main__":
    app.run_server(
        debug=True,
        host="0.0.0.0",
        port="8080",
    )
