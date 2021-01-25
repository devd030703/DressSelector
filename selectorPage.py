import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

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
                        id="button_headwear_randomise",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✓",
                        id="button_headwear_tick",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✖",
                        id="button_headwear_cross",
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
                        id="button_topwear_randomise",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✓",
                        id="button_topwear_tick",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✖",
                        id="button_topwear_cross",
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
                        id="button_bottomwear_randomise",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✓",
                        id="button_bottomwear_tick",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✖",
                        id="button_bottomwear_cross",
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
                        id="button_footwear_randomise",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✓",
                        id="button_footwear_tick",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="✖",
                        id="button_footwear_cross",
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
        ],
        className="card mb-4 border-0",
    ),
)

user_details = (
    dbc.Card(
        dbc.CardBody(
            [
                dbc.Row(
                    html.H4("Account Details", className="card-title"),
                ),
                dbc.Row(
                    html.P("Name:", className="card-text"),
                ),
                dbc.Row(
                    html.P("Gender:", className="card-text"),
                ),
            ],
        ),
    ),
)


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink("Dress Selector", href="#"),
        ),
        dbc.NavItem(
            dbc.NavLink("Saved Outfits", href="#"),
        ),
        dbc.NavItem(
            dbc.NavLink("Account Details", href="#"),
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Options", header=True),
                # dbc.DropdownMenuItem("Saved Outfits", href="#"),
                # dbc.DropdownMenuItem("Account Details", href="#"),
            ],
            nav=True,
            in_navbar=True,
            label="More",
        ),
    ],
    brand="Navigation",
    brand_href="#",
    color="primary",
    dark=True,
)

# --------------------------------------- LAYOUT ---------------------------------------
layout = dbc.Container(
    [
        html.Div(
            [
                dbc.Row(
                    dbc.Col(
                        navbar,
                    ),
                ),
                dbc.Row(
                    dbc.Col(
                        user_details,
                    ),
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            headwear,
                        ),
                        dbc.Col(
                            topwear,
                        ),
                        dbc.Col(
                            bottomwear,
                        ),
                        dbc.Col(
                            footwear,
                        ),
                    ]
                ),
                dbc.Row(
                    dbc.Col(
                        user_buttons,
                        width={"size": 4, "offset": 4},
                    ),
                    className="m-3",
                    align="center",
                ),
            ]
        )
    ]
)

# ------------------------------------- CALLBACKS --------------------------------------
@app.callback(
    [
        Output("alert_login", "is_open"),
        Output("alert_login", "color"),
        Output("alert_login", "children"),
    ],
    [
        Input("button_headwear_randomise", "n_clicks"),
    ],
    [
        State("input_user_name_login", "value"),
        State("input_password_login", "value"),
    ],
)
def randomise_headwear(
    button_login_n_clicks,
    input_user_name_login_value,
    input_password_login_value,
):
pass
