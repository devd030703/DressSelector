import time
from pathlib import Path

import dash
import dash_bootstrap_components as dbc
from dash import callback_context
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

from database.query import DataBase

# create an object of the database before creating the main app
database = DataBase(
    Path(
        "database",
        "database.db",
    )
)

# create the main app
app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.FLATLY],
)


@app.callback(
    Output("url", "pathname"),
    [
        Input("button_login", "n_clicks"),
        Input("button_signup", "n_clicks"),
        Input("button_back", "n_clicks"),
        Input("button_create", "n_clicks"),
        Input("alert", "color"),
    ],
)
def display(
    button_login_n_clicks,
    button_signup_n_clicks,
    button_back_n_clicks,
    button_create_n_clicks,
    alert_color,
):
    ctx = callback_context

    if not ctx.triggered:
        raise PreventUpdate

    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

        if button_id == "button_login" and alert_color == "success":
            time.sleep(1)
            return "/selector"

        elif button_id == "button_signup":
            return "/signup"

        elif button_id == "button_back":
            return "/login"

        elif button_id == "button_create" and alert_color == "success":
            time.sleep(1)
            return "/login"

        else:
            raise PreventUpdate


server = app.server
