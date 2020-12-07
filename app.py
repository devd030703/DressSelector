from pathlib import Path

import dash
import dash_bootstrap_components as dbc

from database.query import DataBase

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.FLATLY],
)

database = DataBase(
    Path(
        "database",
        "database.db",
    )
)


server = app.server
