import base64

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
signup_card = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Input(
                    id="input_user_name_signup",
                    placeholder="user name",
                    type="text",
                    className="mb-3",
                ),
                dbc.Input(
                    id="input_password_signup",
                    placeholder="password",
                    type="text",
                    className="mb-3",
                ),
                dbc.Input(
                    id="input_first_name_signup",
                    placeholder="first name",
                    type="text",
                    className="mb-3",
                ),
                dbc.Input(
                    id="input_last_name_signup",
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
                            id="input_gender_select",
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
                        dbc.Button(
                            children="back",
                            id="button_back_signup",
                            color="primary",
                            className="m-3",
                            href="/login",
                        ),
                        dbc.Button(
                            children="create",
                            id="button_create_signup",
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

alert_signup = dbc.Alert(
    id="alert_signup",
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
                # row2: signup
                dbc.Row(
                    dbc.Col(
                        signup_card,
                        width={"size": 6, "offset": 3},
                    ),
                    align="center",
                    className="m-5",
                ),
                # row3: alert
                dbc.Row(
                    dbc.Col(
                        alert_signup,
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
        Output("alert_signup", "is_open"),
        Output("alert_signup", "color"),
        Output("alert_signup", "children"),
    ],
    [Input("button_create_signup", "n_clicks")],
    [
        State("input_user_name_signup", "value"),
        State("input_password_signup", "value"),
        State("input_first_name_signup", "value"),
        State("input_last_name_signup", "value"),
        State("input_gender_select", "value"),
    ],
)
def validate_signup(
    button_create_signup_n_clicks,
    input_user_name_signup_value,
    input_password_signup_value,
    input_first_name_signup_value,
    input_last_name_signup_value,
    input_gender_select_value,
):
    if button_create_signup_n_clicks:
        if (
            input_user_name_signup_value is not None
            and ~input_user_name_signup_value.isspace()
        ):

            if (
                input_password_signup_value is not None
                and ~input_password_signup_value.isspace()
            ):

                if (
                    input_first_name_signup_value is not None
                    and ~input_first_name_signup_value.isspace()
                ):
                    if (
                        input_last_name_signup_value is not None
                        and ~input_last_name_signup_value.isspace()
                    ):

                        if input_gender_select_value is not None:
                            return (
                                True,
                                "success",
                                "Account created successfully, please go back and login with your new details",
                            )

                        else:
                            return (
                                True,
                                "danger",
                                "Please enter your gender.",
                            )

                    else:
                        return (
                            True,
                            "danger",
                            "Please enter your last name.",
                        )

                else:
                    return (
                        True,
                        "danger",
                        "Please enter your first name.",
                    )

            else:
                return (
                    True,
                    "danger",
                    "Please enter your password.",
                )

        else:
            return (
                True,
                "danger",
                "Please enter your username.",
            )
    else:
        raise PreventUpdate
