import base64
import time

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash import callback_context
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app, database

# ---------------------------------------- DATA ----------------------------------------
logo_image = "logo.png"
user_rowid, first_name, last_name, gender, email, password = database.get_user_details()
gender_values = {"Female": 1, "Male": 2}

# --------------------------------------- IMAGES ---------------------------------------
ds_logo_encoded = base64.b64encode(open(logo_image, "rb").read())
ds_logo_decoded = f"data:image/png;base64,{ds_logo_encoded.decode()}"

# --------------------------------------- CARDS ----------------------------------------
account_card = dbc.Card(
    [
        dbc.CardImg(src=ds_logo_decoded, top=True),
        dbc.CardBody(
            [
                dbc.Input(
                    id="input_user_name_account",
                    value="{}".format(database.email),
                    type="text",
                    className="mb-3",
                ),
                dbc.Input(
                    id="input_password_account",
                    value="{}".format(database.password),
                    type="text",
                    className="mb-3",
                ),
                dbc.Input(
                    id="input_first_name_account",
                    value="{}".format(database.first_name),
                    type="text",
                    className="mb-3",
                ),
                dbc.Input(
                    id="input_last_name_account",
                    value="{}".format(database.last_name),
                    type="text",
                    className="mb-3",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupAddon(
                            "Gender",
                            addon_type="prepend",
                        ),
                        dbc.Select(
                            id="input_gender_select_account",
                            value=gender_values[database.gender],
                            options=[
                                {"label": "Female", "value": 1},
                                {"label": "Male", "value": 2},
                            ],
                        ),
                    ],
                    className="mb-3",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            dbc.Button(
                                children="back",
                                id="button_back_account",
                                color="primary",
                                className="m-3",
                                href="/selector",
                                external_link=True,
                            ),
                        ),
                        dbc.Col(
                            dbc.Button(
                                children="delete",
                                id="button_delete_account",
                                color="primary",
                                className="m-3",
                            ),
                        ),
                        dbc.Col(
                            dbc.Button(
                                children="update",
                                id="button_update_account",
                                color="primary",
                                className="m-3",
                            ),
                        ),
                    ]
                ),
            ]
        ),
    ],
    color="light",
    inverse=True,
)

alert_account = dbc.Alert(
    id="alert_account",
    dismissable=True,
    is_open=False,
)


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(
            dbc.NavLink(
                "Dress Selector",
                id="navlink_dress_selector_account",
                href="/selector",
                external_link=True,
            ),
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Saved Outfits",
                id="navlink_saved_outfits_account",
                href="/wardrobe",
                external_link=True,
            ),
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Account Details",
                id="navlink_account_details_account",
                href="/accountdetails",
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
                # row1: Navbar
                dbc.Row(
                    dbc.Col(
                        navbar,
                    ),
                ),
                # row2: account details
                dbc.Row(
                    dbc.Col(
                        account_card,
                        width={"size": 6, "offset": 3},
                    ),
                    align="center",
                    className="m-5",
                ),
                # row3: alert
                dbc.Row(
                    dbc.Col(
                        alert_account,
                        width={"size": 6, "offset": 3},
                    ),
                    align="center",
                    className="m-5",
                ),
            ]
        )
    ]
)


# ------------------------------------- CALLBACKS --------------------------------------
@app.callback(
    [
        Output("alert_account", "is_open"),
        Output("alert_account", "color"),
        Output("alert_account", "children"),
    ],
    [
        Input("button_delete_account", "n_clicks"),
        Input("button_update_account", "n_clicks"),
    ],
    [
        State("input_user_name_account", "value"),
        State("input_password_account", "value"),
        State("input_first_name_account", "value"),
        State("input_last_name_account", "value"),
        State("input_gender_select_account", "value"),
    ],
)
def update_delete_details(
    button_delete_account_n_clicks,
    button_update_account_n_clicks,
    input_user_name_account_value,
    input_password_account_value,
    input_first_name_account_value,
    input_last_name_account_value,
    input_gender_select_account_value,
):
    if button_delete_account_n_clicks or button_update_account_n_clicks:
        ctx = callback_context
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]

        if button_id == "button_delete_account":
            database.delete_user(database.user_rowid)
            return (
                True,
                "success",
                "Account deleted successfully.",
            )
        elif button_id == "button_update_account":
            database.update_user_details(
                first_name=input_first_name_account_value,
                last_name=input_last_name_account_value,
                gender=input_gender_select_account_value,
                email=input_user_name_account_value,
                password=input_password_account_value,
                user_rowid=database.user_rowid,
            )
            return (
                True,
                "success",
                "Account updated successfully",
            )
        else:
            raise PreventUpdate

    else:
        raise PreventUpdate
