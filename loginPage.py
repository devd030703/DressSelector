import base64
import time

import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from app import app, database

# ---------------------------------------- DATA ----------------------------------------
logo_image = "logo.png"

# --------------------------------------- IMAGES ---------------------------------------
ds_logo_encoded = base64.b64encode(open(logo_image, "rb").read())

img_ds = html.Img(
    src=f"data:image/png;base64,{ds_logo_encoded.decode()}",
    style={
        "float": "centre",
        "width": "50%",
    },
)

# --------------------------------------- CARDS ----------------------------------------
card_login = dbc.Card(
    [
        # dbc.CardHeader(
        #     children="Components",
        #     className="card-header mb-0",
        # ),
        dbc.CardBody(
            [
                dbc.Input(
                    id="input_user_name",
                    placeholder="user name",
                    type="text",
                    className="mb-3",
                ),
                dbc.Input(
                    id="input_password",
                    placeholder="password",
                    type="text",
                    className="mb-3",
                ),
                dbc.Collapse(
                    [
                        dbc.Input(
                            id="input_first_name",
                            placeholder="first name",
                            type="text",
                            className="mb-3",
                        ),
                        dbc.Input(
                            id="input_last_name",
                            placeholder="last name",
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
                                    options=[
                                        {"label": "Female", "value": 1},
                                        {"label": "Male", "value": 2},
                                    ]
                                ),
                            ]
                        ),
                    ],
                    id="collapse",
                ),
                dbc.Row(
                    [
                        dbc.Button(
                            children="login",
                            id="button_login",
                            color="primary",
                            className="m-3",
                        ),
                        dbc.Button(
                            children="signup",
                            id="button_signup",
                            color="primary",
                            className="m-3",
                        ),
                    ]
                ),
            ]
        ),
    ],
    color="light",
    inverse=True,
)

alert = dbc.Alert(
    id="alert",
    dismissable=True,
    is_open=False,
)


# --------------------------------------- LAYOUT ---------------------------------------
layout = dbc.Container(
    [
        html.Div(
            [
                # row1: logos
                dbc.Row(
                    dbc.Col(
                        html.Div("TITLE"),
                        width={"size": 6, "offset": 3},
                    ),
                    align="center",
                    className="m-5",
                ),
                # row2: login
                dbc.Row(
                    dbc.Col(
                        card_login,
                        width={"size": 6, "offset": 3},
                    ),
                    align="center",
                    className="m-5",
                ),
                # row3: success
                dbc.Row(
                    dbc.Col(
                        alert,
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
        Output("alert", "is_open"),
        Output("alert", "color"),
        Output("alert", "children"),
    ],
    [
        Input("button_login", "n_clicks"),
    ],
    [
        State("input_user_name", "value"),
        State("input_password", "value"),
    ],
)
def validate_login(
    login_button_n_clicks,
    input_user_name_value,
    input_password_value,
):
    if login_button_n_clicks:
        if input_user_name_value is not None and ~input_user_name_value.isspace():
            if input_password_value is not None and ~input_password_value.isspace():
                if database.check_user_exists(
                    by="email", value=input_user_name_value
                ) and database.check_password_is_correct(password=input_password_value):
                    return (
                        True,
                        "success",
                        "Please wait while we redirect you",
                    )
                else:
                    return (
                        True,
                        "danger",
                        "Incorrect Username or Password entered",
                    )

            else:
                return (
                    True,
                    "danger",
                    "Please enter your password username.",
                )
        else:
            return (
                True,
                "danger",
                "Please enter your username.",
            )
    else:
        raise PreventUpdate


@app.callback(
    Output("url", "pathname"),
    [
        Input("alert", "color"),
    ],
)
def login(alert_color):

    print("alert_color", alert_color)
    if alert_color == "success":
        time.sleep(1)
        return "/selectorPage"
    else:
        raise PreventUpdate


@app.callback(
    Output("collapse", "is_open"),
    [Input("button_signup", "n_clicks")],
    [State("collapse", "is_open")],
)
def collapse_signup(button_signup_n_clicks, collapse_is_open):
    if button_signup_n_clicks:
        return not collapse_is_open
    return collapse_is_open


# @app.callback(
#     Output("url", "pathname"),
#     [Input("button_signup", "n_clicks")],
#     [
#         State("input_user_name", "value"),
#         State("input_password", "value"),
#         State("input_first_name", "value"),
#         State("input_last_name", "value"),
#         State("drop_down_menu_gender", "n_clicks"),
#     ],
# )
# def signup(button_signup_n_clicks):
#     if button_signup_n_clicks:
#         if input_user_name_value is not None and ~input_user_name_value.isspace():
#             if input_password_value is not None and ~input_password_value.isspace():
#                 return "/selectorPage"
#     else:
#         raise PreventUpdate
