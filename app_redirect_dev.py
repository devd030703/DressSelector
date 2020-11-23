# %%
import base64
import os
from pathlib import Path

import dash_bootstrap_components as dbc
import dash_html_components as html

import dash
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate


# %%
# ---------------------------------------- DATA ----------------------------------------
logo_image = "logo.png"


# ---------------------------------------- APP -----------------------------------------
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.FLATLY],
    suppress_callback_exceptions=True,
)

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
                dbc.Row(
                    [
                        dbc.Button(
                            children="login",
                            id="button_login",
                            color="primary",
                            className="m-3",
                            href="dresselector",
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

success = dbc.Alert(
    "Please wait while we redirect you",
    id="success",
    dismissable=True,
    is_open=False,
)

failure = dbc.Alert(
    "Incorrect Username or Password entered",
    id="failure",
    dismissable=True,
    is_open=False,
)

fashion_display = dbc.Card(
    [
        dbc.CardImg(
            src=Path("dataset", "image_sample", "Bottomwear", "Men", "7266.jpg"),
            top=True,
        ),
        dbc.CardBody(html.P("This is the Hat", className="card-text")),
        dbc.CardImg(
            src=Path("dataset", "image_sample", "Bottomwear", "Men", "7266.jpg"),
            top=True,
        ),
        dbc.CardBody(html.P("This is the Tshirt", className="card-text")),
        dbc.CardImg(
            src=Path("dataset", "image_sample", "Bottomwear", "Men", "7266.jpg"),
            top=True,
        ),
        dbc.CardBody(html.P("This is the Jeans", className="card-text")),
        dbc.CardImg(
            src=Path("dataset", "image_sample", "Bottomwear", "Men", "7266.jpg"),
            top=True,
        ),
        dbc.CardBody(html.P("This is the Footwear", className="card-text")),
    ],
    style={"width": "18rem"},
)

user_buttons = dbc.Card(
    [
        dbc.CardBody(
            [
                dbc.Button(
                    children="generate",
                    id="button_senerate",
                    color="primary",
                    className="m-3",
                ),
                dbc.Button(
                    children="save",
                    id="button_save",
                    color="primary",
                    className="m-3",
                ),
            ]
        ),
    ]
)

# --------------------------------------- LAYOUT ---------------------------------------
app.layout = dbc.Container(
    [
        html.Div(
            [
                html.Div(id="page-content"),
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
                # row3: alert
                dbc.Row(
                    dbc.Col(
                        success,
                        width={"size": 6, "offset": 3},
                    ),
                    align="center",
                    className="m-5",
                ),
                # row4 : failure
                dbc.Row(
                    dbc.Col(
                        failure,
                        width={"size": 6, "offset": 3},
                    ),
                    align="center",
                    className="m-5",
                ),
            ]
        )
    ]
)

app2_layout = dbc.Container(
    [
        html.Div(
            [
                dbc.Row(
                    dbc.Col(
                        fashion_display,
                        width={"size": 6, "offset": 0},
                    ),
                    className="m-3",
                    align="center",
                ),
                dbc.Row(
                    dbc.Col(
                        user_buttons,
                        width={"size": 4, "offset": 0},
                    ),
                    className="m-3",
                    align="center",
                ),
            ]
        )
    ]
)

# ------------------------------------- CALLBACKS --------------------------------------
# %%
@app.callback(
    [
        Output("success", "is_open"),
        Output("failure", "is_open"),
        Output("page-content", "children"),
    ],
    [
        Input("button_login", "n_clicks"),
    ],
    [
        State("input_user_name", "value"),
        State("input_password", "value"),
    ],
)
def login(
    login_button_n_clicks,
    input_user_name_value,
    input_password_value,
):
    if login_button_n_clicks:
        if input_user_name_value is not None:
            if input_user_name_value.isspace() == False:
                if input_password_value is not None:
                    if input_password_value.isspace() == False:
                        return True, False, app2_layout
                    else:
                        return False, True, None
                else:
                    return False, True, None
            else:
                return False, True, None
        else:
            return False, True, None
    else:
        return False, False, None


# %%
if __name__ == "__main__":
    app.run_server(
        debug=True,
        host="0.0.0.0",
        port="8080",
    )
