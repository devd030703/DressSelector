import base64

import time
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app, database

# ---------------------------------------- DATA ----------------------------------------
logo_image = "logo.png"

# --------------------------------------- IMAGES ---------------------------------------
ds_logo_encoded = base64.b64encode(open(logo_image, "rb").read())
ds_logo_decoded = f"data:image/png;base64,{ds_logo_encoded.decode()}"

# --------------------------------------- CARDS ----------------------------------------
signup_card = dbc.Card(
    [
        dbc.CardImg(src=ds_logo_decoded, top=True),
        dbc.CardBody(
            [
                dbc.Input(
                    id="input_user_name_signup_update",
                    placeholder="user name",
                    type="text",
                    className="mb-3",
                ),
                dbc.Input(
                    id="input_password_signup_update",
                    placeholder="password",
                    type="text",
                    className="mb-3",
                ),
                dbc.Input(
                    id="input_first_name_signup_update",
                    placeholder="first name",
                    type="text",
                    className="mb-3",
                ),
                dbc.Input(
                    id="input_last_name_signup_update",
                    placeholder="last name",
                    type="text",
                    className="mb-3",
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupAddon("Gender", addon_type="prepend",),
                        dbc.Select(
                            id="input_gender_select_update",
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
                                children="delete",
                                id="button_delete_signup",
                                color="primary",
                                className="m-3",
                                href="",
                            ),
                        ),
                        dbc.Col(
                            dbc.Button(
                                children="update",
                                id="button_update_signup",
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

alert_signup = dbc.Alert(id="alert_signup", dismissable=True, is_open=False,)


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
        dbc.NavItem(dbc.NavLink("Saved Outfits", href="#"),),
        dbc.NavItem(
            dbc.NavLink(
                "Account Details",
                # href="/accountdetails",
                # id="account_details",
                # external_link=True,
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
                # row1: signup
                dbc.Row(
                    dbc.Col(signup_card, width={"size": 6, "offset": 3},),
                    align="center",
                    className="m-5",
                ),
                # row2: alert
                dbc.Row(
                    dbc.Col(alert_signup, width={"size": 6, "offset": 3},),
                    align="center",
                    className="m-5",
                ),
            ]
        )
    ]
)


# ------------------------------------- CALLBACKS --------------------------------------


# i have had to rename output to make this work, not sure why
# also this is an ugly page reload
@app.callback(
    Output("url_account", "pathname_account"), [Input("dress_selector", "n_clicks"),],
)
def change_pathname(account_details_n_clicks):
    if account_details_n_clicks == "success":
        time.sleep(1)
        return "/selector"

    else:
        raise PreventUpdate
