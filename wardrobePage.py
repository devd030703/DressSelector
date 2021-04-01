import base64
from pathlib import Path

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash import callback_context
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app, database

# ---------------------------------------- DATA ----------------------------------------
user_rowid, first_name, last_name, gender, email, password = database.get_user_details()
outfits = database.get_user_outfits(user_rowid)

# --------------------------------------- IMAGES ---------------------------------------


def process_binary_image(img):
    img_encoded = base64.b64encode(img)
    return f"data:image/png;base64,{img_encoded.decode()}"


def process_image(img):
    img_encoded = base64.b64encode(open(img, "rb").read())
    return f"data:image/png;base64,{img_encoded.decode()}"


headwear_placeholder_men = process_image(
    Path("images", "Headwear", "PlaceHolderMen.png"),
)

topwear_placeholder_men = process_image(
    Path("images", "Topwear", "PlaceHolderMen.png"),
)

bottomwear_placeholder_men = process_image(
    Path("images", "Bottomwear", "PlaceHolderMen.png"),
)

shoes_placeholder_men = process_image(
    Path("images", "Shoes", "PlaceHolderMen.png"),
)


# --------------------------------------- CARDS ----------------------------------------
headwear = (
    dbc.Card(
        [
            dbc.CardImg(
                src=headwear_placeholder_men,
                id="card_img_outfit_headwear",
                top=True,
            ),
        ]
    ),
)


topwear = (
    dbc.Card(
        [
            dbc.CardImg(
                src=topwear_placeholder_men,
                id="card_img_outfit_topwear",
                top=True,
            ),
        ]
    ),
)

bottomwear = (
    dbc.Card(
        [
            dbc.CardImg(
                src=bottomwear_placeholder_men,
                id="card_img_outfit_bottomwear",
                top=True,
            ),
        ]
    ),
)


footwear = (
    dbc.Card(
        [
            dbc.CardImg(
                src=shoes_placeholder_men,
                id="card_img_outfit_footwear",
                top=True,
            ),
        ]
    ),
)

delete_button = (
    dbc.Card(
        [
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Button(
                                    children="Delete",
                                    id="button_delete",
                                    color="primary",
                                ),
                            ),
                        ],
                    ),
                ]
            ),
        ],
        className="border-0",
    ),
)


download_button = (
    dbc.Card(
        [
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Button(
                                    children="Download",
                                    id="button_download",
                                    color="primary",
                                ),
                            ),
                        ],
                    ),
                ]
            ),
        ],
        className="border-0",
    ),
)


left_button = (
    dbc.Card(
        [
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Button(
                                    children="⬅",
                                    id="button_left",
                                    color="primary",
                                ),
                            ),
                        ],
                    ),
                ]
            ),
        ],
        className="border-0",
    ),
)
button_right = (
    dbc.Card(
        [
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Button(
                                    children="➡",
                                    id="button_right",
                                    color="primary",
                                ),
                            ),
                        ],
                    ),
                ]
            ),
        ],
        className="border-0",
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
                "Saved Outfits",
                href="/wardrobe",
                id="wardrobe",
                external_link=True,
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
                # abc.DropdownMenuItem("Saved Outfits", href="#"),
                # abcc.DropdownMenuItem("Account Details", href="#"),
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
                dcc.Store(
                    id="store_outfits",
                    storage_type="session",
                    data={
                        "user_id": None,
                        "headwear_item_id": None,
                        "topwear_item_id": None,
                        "bottomwear_item_id": None,
                        "footwear_item_id": None,
                    },
                ),
                dbc.Row(
                    [
                        dbc.Col(headwear, width=3),
                        dbc.Col(topwear, width=3),
                    ],
                    justify="center",
                    className="mt-3",
                ),
                dbc.Row(
                    [
                        dbc.Col(bottomwear, width=3),
                        dbc.Col(footwear, width=3),
                    ],
                    justify="center",
                    className="mt-3",
                ),
                dbc.Row(
                    dbc.Col(
                        dbc.Row(
                            [
                                dbc.Col(
                                    dbc.Row(
                                        dbc.Col(
                                            left_button,
                                            width={"size": "10%"},
                                        ),
                                        justify="start",
                                        no_gutters=True,
                                    ),
                                ),
                                dbc.Col(
                                    dbc.Row(
                                        dbc.Col(
                                            delete_button,
                                            width={"size": "10%"},
                                        ),
                                        justify="end",
                                        no_gutters=True,
                                    ),
                                ),
                                dbc.Col(
                                    dbc.Row(
                                        dbc.Col(
                                            download_button,
                                            width={"size": "10%"},
                                        ),
                                        justify="start",
                                        no_gutters=True,
                                    ),
                                ),
                                dbc.Col(
                                    dbc.Row(
                                        dbc.Col(
                                            button_right,
                                            width={"size": "10%"},
                                        ),
                                        justify="end",
                                        no_gutters=True,
                                    ),
                                ),
                            ],
                            no_gutters=True,
                            justify="center",
                        ),
                        width={"size": 6, "offset": 3},
                    ),
                ),
            ],
        )
    ]
)


# ------------------------------------- CALLBACKS --------------------------------------
@app.callback(
    [
        Output("card_img_outfit_headwear", "src"),
        Output("card_img_outfit_topwear", "src"),
        Output("card_img_outfit_bottomwear", "src"),
        Output("card_img_outfit_footwear", "src"),
        Output("store_outfits", "data"),
    ],
    [
        Input("button_left", "n_clicks"),
        Input("button_right", "n_clicks"),
    ],
    State("store_outfits", "data"),
)
def display_outfit(
    button_left_n_clicks,
    button_right_n_clicks,
    store_outfits_data,
):
    if button_left_n_clicks or button_right_n_clicks:

        ctx = callback_context
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

        if button_id == "button_left":

            outfit = outfits[0]

            item_headwear = database.get_item_details(outfit[1])
            item_topwear = database.get_item_details(outfit[2])
            item_bottomwear = database.get_item_details(outfit[3])
            item_footwear = database.get_item_details(outfit[4])

            store_outfits_data["headwear_item_id"] = outfit[1]
            store_outfits_data["topwear_item_id"] = outfit[2]
            store_outfits_data["bottomwear_item_id"] = outfit[3]
            store_outfits_data["footwear_item_id"] = outfit[4]
            print(store_outfits_data)

        return (
            process_binary_image(item_headwear[5]),
            process_binary_image(item_topwear[5]),
            process_binary_image(item_bottomwear[5]),
            process_binary_image(item_footwear[5]),
            store_outfits_data,
        )
    else:
        raise PreventUpdate
