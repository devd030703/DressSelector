from inspect import indentsize
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Col import Col
import dash_core_components as dcc
import dash_html_components as html

from app import app, database

# ---------------------------------------- DATA ----------------------------------------

# --------------------------------------- IMAGES ---------------------------------------

# --------------------------------------- CARDS ----------------------------------------
headwear = dbc.Card(
    [dbc.CardBody(
        html.P(
            "Headwear", className="card-text"
        )
    ),
        dbc.CardImg(
        src="/Users/devdeepak/Desktop/GitHub/DressSelector/dash/images/2467.jpg",
        top=True
    ),


        dbc.Row(
            dbc.Col(
                [
                    dbc.Button(
                        children="🔀",
                        id="headwear_randomise",
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
                ]
            ),
    ),
    ]
),

topwear = dbc.Card(
    [dbc.CardBody(
        html.P(
            "Topwear", className="card-text"
        )
    ),
        dbc.CardImg(
        src="/Users/devdeepak/Desktop/GitHub/DressSelector/dash/images/2467.jpg",
        top=True
    ),



        dbc.Row(
            dbc.Col(
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
                ]
            ),
            align="center",
    ),
    ]
),

bottomwear = dbc.Card(
    [dbc.CardBody(
        html.P(
            "Bottomwear", className="card-text"
        )
    ),
        dbc.CardImg(
        src="/Users/devdeepak/Desktop/GitHub/DressSelector/dash/images/2467.jpg",
        top=True
    ),


        dbc.Row(
            dbc.Col(
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
                ]
            ),
    ),
    ]
),

footwear = dbc.Card(
    [dbc.CardBody(
        html.P(
            "Footwear", className="card-text"
        )
    ),
        dbc.CardImg(
        src="/Users/devdeepak/Desktop/GitHub/DressSelector/dash/images/2467.jpg",
        top=True
    ),

        dbc.Row(
            dbc.Col(
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
                ]
            ),
    ),
    ]
),

user_buttons = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Button(
                                children="generate",
                                id="button_senerate",
                                color="primary",
                                className="m-3",
                            ),
                            align="end",
                        ),

                        dbc.Col(
                            dbc.Button(
                                children="save",
                                id="button_save",
                                color="primary",
                                className="m-3",
                            ),
                            align="end",
                        ),
                    ]

                ),
            ]
        ),
    ]
),

# --------------------------------------- LAYOUT ---------------------------------------
app.layout = dbc.Container(
    [
        html.Div(
            [
                dbc.Row([
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
                html.Div(id="app-2-display-value"),
                dcc.Link("Go to App 1", href="/app1"),
            ]
        )
    ]
)

# ------------------------------------- CALLBACKS --------------------------------------


app.run_server(
    debug=True,
    host="0.0.0.0",
    port="8080",
)
