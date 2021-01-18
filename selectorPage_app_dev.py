from inspect import indentsize

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash_bootstrap_components._components.CardBody import CardBody
from dash_bootstrap_components._components.Col import Col

from app import app, database

# ---------------------------------------- DATA ----------------------------------------

# --------------------------------------- IMAGES ---------------------------------------

# --------------------------------------- CARDS ----------------------------------------
headwear = (
    dbc.Card(
        [
            dbc.CardBody(html.P("Headwear", className="card-text")),
            dbc.CardImg(
                src="/Users/devdeepak/Desktop/GitHub/DressSelector/dash/images/2467.jpg",
                top=True,
            ),
            dbc.Row(
                [
                    dbc.Button(
                        children="🔀",
                        id="headwear_randomisce",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✓",
                        id="headwear_tick",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✖",
                        id="headwear_cross",
                        color="primary",
                        className="m-3",
                    ),
                ],
                justify="center",
            ),
        ]
    ),
)


topwear = (
    dbc.Card(
        [
            dbc.CardBody(html.P("Topwear", className="card-text")),
            dbc.CardImg(
                src="/Users/devdeepak/Desktop/GitHub/DressSelector/dash/images/2467.jpg",
                top=True,
            ),
            dbc.Row(
                [
                    dbc.Button(
                        children="🔀",
                        id="topwear_randomise",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✓",
                        id="topwear_tick",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✖",
                        id="topwear_cross",
                        color="primary",
                        className="m-3",
                    ),
                ],
                justify="center",
            ),
        ]
    ),
)

bottomwear = (
    dbc.Card(
        [
            dbc.CardBody(html.P("Bottomwear", className="card-text")),
            dbc.CardImg(
                src="/Users/devdeepak/Desktop/GitHub/DressSelector/dash/images/2467.jpg",
                top=True,
            ),
            dbc.Row(
                [
                    dbc.Button(
                        children="🔀",
                        id="bottomwear_randomise",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✓",
                        id="bottomwear_tick",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✖",
                        id="bottomwear_cross",
                        color="primary",
                        className="m-3",
                    ),
                ],
                justify="center",
            ),
        ]
    ),
)


footwear = (
    dbc.Card(
        [
            dbc.CardBody(html.P("Footwear", className="card-text")),
            dbc.CardImg(
                src="/Users/devdeepak/Desktop/GitHub/DressSelector/dash/images/2467.jpg",
                top=True,
            ),
            dbc.Row(
                [
                    dbc.Button(
                        children="🔀",
                        id="footwear_randomise",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✓",
                        id="footwear_tick",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✖",
                        id="footwear_cross",
                        color="primary",
                        className="m-3",
                    ),
                ],
                justify="center",
            ),
        ]
    ),
)

user_buttons = (
    dbc.Card(
        [
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Button(
                                    children="generate",
                                    id="button_generate",
                                    color="primary",
                                    className="m-3",
                                ),
                                width={"size": "auto"},
                            ),
                            dbc.Col(
                                dbc.Button(
                                    children="save",
                                    id="button_save",
                                    color="primary",
                                    className="m-3",
                                ),
                                width={"size": "auto"},
                            ),
                        ],
                        justify="center",
                    ),
                ]
            ),
        ]
    ),
)

user_details = (
    (
        dbc.Card(
            dbc.CardBody(
                dbc.Row(
                    [
                        html.H4("User Details", className="card-title"),
                        html.P(
                            "this is the stuff the user sees", className="card-text"
                        ),
                    ],
                    justify="center",
                ),
            ),
        ),
    ),
)

# --------------------------------------- SIDE BAR ----------------------------------------

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        dbc.Button(
            "Open collapse", id="collapse-button", className="mb-3", color="primary",
        ),
        dbc.Collapse(
            [
                html.H2("Sidebar", className="display-4"),
                html.Hr(),
                html.P(
                    "A simple sidebar layout with navigation links", className="lead"
                ),
                dbc.Nav(
                    [
                        dbc.NavLink("Dress Selector", href="/", active="exact"),
                        dbc.NavLink("Saved Dresses", href="/page-1", active="exact"),
                        dbc.NavLink("Account Settings", href="/page-2", active="exact"),
                    ],
                    vertical=True,
                    pills=True,
                ),
            ],
            id="collapse",
            style=SIDEBAR_STYLE,
        ),
    ],
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

# --------------------------------------- LAYOUT ---------------------------------------
app.layout = dbc.Container(
    [
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(headwear,),
                        dbc.Col(topwear,),
                        dbc.Col(bottomwear,),
                        dbc.Col(footwear,),
                    ]
                ),
                dbc.Row(
                    dbc.Col(user_buttons, width={"size": 4, "offset": 4},),
                    className="m-3",
                    align="center",
                ),
                html.Div(id="app-2-display-value"),
                html.Div([(sidebar), (content),],),
            ],
        )
    ],
)

# ------------------------------------- CALLBACKS --------------------------------------
@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


app.run_server(
    debug=True, host="0.0.0.0", port="8080",
)

