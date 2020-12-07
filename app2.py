# %%
# import base64
# import os

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from dash_bootstrap_components._components.CardBody import CardBody
import dash_core_components as dcc

# %%

# %%
# ---------------------------------------- APP -----------------------------------------
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.FLATLY],
)
# --------------------------------------- CARDS ----------------------------------------
fashion_display = dbc.Card(
    [
        dbc.CardImg(
            src="/Users/devdeepak/Desktop/GitHub/DressSelector/dash/images/2467.jpg",
            top=True,
        ),
        dbc.CardBody(html.P("This is the Hat", className="card-text")),
        dbc.CardImg(
            src="/Users/devdeepak/Desktop/GitHub/DressSelector/dash/images/14691.jpg",
            top=True,
        ),
        dbc.CardBody(html.P("This is the Tshirt", className="card-text")),
        dbc.CardImg(
            src="/Users/devdeepak/Desktop/GitHub/DressSelector/dash/images/10858.jpg",
            top=True,
        ),
        dbc.CardBody(html.P("This is the Jeans", className="card-text")),
        dbc.CardImg(
            src="/Users/devdeepak/Desktop/GitHub/DressSelector/dash/images/38775.jpg",
            top=True,
        ),
        dbc.CardBody(html.P("This is the Footwear", className="card-text")),
    ],
    style={"width": "18rem"},
)

user_buttons = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Button(
                    children="generate",
                    id="button_senerate",
                    color="primary",
                    className="m-3",
                ),
                dbc.Button(
                    children="save",
                    id="button_save",
                    color="primary",
                    className="m-3",
                ),
            ]
        ),
    ]
)

# --------------------------------------- LAYOUT ---------------------------------------
layout = dbc.Container(
    [
        html.Div(
            [
                dbc.Row(
                    dbc.Col(
                        fashion_display,
                        width={"size": 6, "offset": 0},
                    ),
                    className="m-3",
                    align="center",
                ),
                dbc.Row(
                    dbc.Col(
                        user_buttons,
                        width={"size": 4, "offset": 0},
                    ),
                    className="m-3",
                    align="center",
                ),
                html.Div(id="app-2-display-value"),
                dcc.Link("Go to App 1", href="/app1"),
            ]
        )
    ]
)


# ------------------------------------- CALLBACKS --------------------------------------
# %%


# %%
if __name__ == "__main__":
    app.run_server(
        debug=True,
        host="0.0.0.0",
        port="8080",
    )
