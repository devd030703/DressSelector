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
                        children="⬅️",
                        id="headwear_randomisce",
                        color="primary",
                        className="m-3",
                    ),
                    dbc.Button(
                        children="➡️",
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


user_buttons = (
    dbc.Card(
        [
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Button(
                                    children="Delete",
                                    id="button_generate",
                                    color="primary",
                                    className="m-3",
                                ),
                                width={"size": "auto"},
                            ),
                            dbc.Col(
                                dbc.Button(
                                    children="Download",
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

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink(
                "Dress Selector",
                href="/selector",
                id="dress_selector",
                external_link=True,
            ),
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Saved Outfits", href="/wardrobe", id="wardrobe", external_link=True,
            ),
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Account Details",
                href="/accountdetails",
                id="account_details",
                external_link=True,
            ),
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
                dbc.Row(dbc.Col(navbar,),),
                dbc.Row([dbc.Col(headwear,),]),
                dbc.Row(
                    dbc.Col(user_buttons, width={"size": 4, "offset": 4},),
                    className="m-3",
                    align="center",
                ),
            ]
        )
    ]
)

# ------------------------------------- CALLBACKS --------------------------------------

