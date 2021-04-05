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
outfit_no = len(outfits)


# --------------------------------------- IMAGES ---------------------------------------
def process_binary_image(img):
    img_encoded = base64.b64encode(img)
    return f"data:image/png;base64,{img_encoded.decode()}"


def process_image(img):
    img_encoded = base64.b64encode(open(img, "rb").read())
    return f"data:image/png;base64,{img_encoded.decode()}"


def get_outfit_images(outfit):
    item_headwear = database.get_item_details(outfit[1])
    item_topwear = database.get_item_details(outfit[2])
    item_bottomwear = database.get_item_details(outfit[3])
    item_footwear = database.get_item_details(outfit[4])

    return (
        process_binary_image(item_headwear[5]),
        process_binary_image(item_topwear[5]),
        process_binary_image(item_bottomwear[5]),
        process_binary_image(item_footwear[5]),
    )


# outfits might be an empty list if no outfits exists
# display first outfit images at first visit
if outfits:
    (
        headwear_placeholder,
        topwear_placeholder,
        bottomwear_placeholder,
        shoes_placeholder,
    ) = get_outfit_images(outfits[0])
else:
    headwear_placeholder = process_image(
        Path("images", "Headwear", "PlaceHolder.png"),
    )
    topwear_placeholder = process_image(
        Path("images", "Topwear", "PlaceHolder.png"),
    )
    bottomwear_placeholder = process_image(
        Path("images", "Bottomwear", "PlaceHolder.png"),
    )
    shoes_placeholder = process_image(
        Path("images", "Shoes", "PlaceHolder.png"),
    )


# --------------------------------------- NAVBAR ---------------------------------------
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

# --------------------------------------- CARDS ----------------------------------------
headwear = (
    dbc.Card(
        [
            dbc.CardImg(
                src=headwear_placeholder,
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
                src=topwear_placeholder,
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
                src=bottomwear_placeholder,
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
                src=shoes_placeholder,
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
                        "index": 0,
                        "user_id": outfits[0][0],
                        "headwear_item_id": outfits[0][1],
                        "topwear_item_id": outfits[0][2],
                        "bottomwear_item_id": outfits[0][3],
                        "footwear_item_id": outfits[0][4],
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
        Input("button_delete", "n_clicks"),
    ],
    State("store_outfits", "data"),
)
def display_or_delete_outfit(
    button_left_n_clicks,
    button_right_n_clicks,
    button_delete_n_clicks,
    store_outfits_data,
):
    if button_left_n_clicks or button_right_n_clicks or button_delete_n_clicks:

        print(store_outfits_data)

        pointer = store_outfits_data["index"]
        ctx = callback_context
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

        if button_id == "button_right":

            if pointer == outfit_no:
                pointer = 0
            else:
                pointer = pointer + 1

            outfit = outfits[pointer]

            item_headwear = database.get_item_details(outfit[1])
            item_topwear = database.get_item_details(outfit[2])
            item_bottomwear = database.get_item_details(outfit[3])
            item_footwear = database.get_item_details(outfit[4])

            store_outfits_data["headwear_item_id"] = outfit[1]
            store_outfits_data["topwear_item_id"] = outfit[2]
            store_outfits_data["bottomwear_item_id"] = outfit[3]
            store_outfits_data["footwear_item_id"] = outfit[4]
            store_outfits_data["index"] = pointer
            print(store_outfits_data)

            return (
                process_binary_image(item_headwear[5]),
                process_binary_image(item_topwear[5]),
                process_binary_image(item_bottomwear[5]),
                process_binary_image(item_footwear[5]),
                store_outfits_data,
            )

        elif button_id == "button_left":

            pointer = pointer - 1
            outfit = outfits[pointer]

            item_headwear = database.get_item_details(outfit[1])
            item_topwear = database.get_item_details(outfit[2])
            item_bottomwear = database.get_item_details(outfit[3])
            item_footwear = database.get_item_details(outfit[4])

            store_outfits_data["headwear_item_id"] = outfit[1]
            store_outfits_data["topwear_item_id"] = outfit[2]
            store_outfits_data["bottomwear_item_id"] = outfit[3]
            store_outfits_data["footwear_item_id"] = outfit[4]

            if pointer < 0:
                store_outfits_data["index"] = outfit_no
            else:
                store_outfits_data["index"] = pointer

            return (
                process_binary_image(item_headwear[5]),
                process_binary_image(item_topwear[5]),
                process_binary_image(item_bottomwear[5]),
                process_binary_image(item_footwear[5]),
                store_outfits_data,
            )

        elif button_id == "button_delete":
            user_id = store_outfits_data["user_id"]
            headwear_id = store_outfits_data["headwear_item_id"]
            topwear_id = store_outfits_data["topwear_item_id"]
            bottomwear_id = store_outfits_data["bottomwear_item_id"]
            footwear_id = store_outfits_data["footwear_item_id"]

            print(user_id, headwear_id, topwear_id, bottomwear_id, footwear_id)

            database.delete_outfit(
                user_id,
                headwear_id,
                topwear_id,
                bottomwear_id,
                footwear_id,
            )

            return (
                headwear_placeholder,
                topwear_placeholder,
                bottomwear_placeholder,
                shoes_placeholder,
                store_outfits_data,
            )

    else:
        raise PreventUpdate
