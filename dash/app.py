# %%
import base64
import os

import dash_bootstrap_components as dbc
from dash_bootstrap_components import CardSubtitle
import dash_html_components as html

import dash

# %%
# ---------------------------------------- DATA ----------------------------------------
logo_image = os.path.join("images", "models.png")

# %%
# ---------------------------------------- APP -----------------------------------------
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
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
                    className="mb-2",
                ),
                dbc.Input(
                    id="input_password",
                    placeholder="password",
                    type="text",
                    className="mb-2",
                ),
                dbc.Row(
                    [
                        dbc.Button(
                            "Login",
                            color="primary",
                            className = "p-1, m-3",
                        ),
                        dbc.Button(
                            "Signup",
                            color="primary",
                            className ="p-1, m-3",
                        ),
                    ]
                ),
            ]
        ),
    ],
    color="light",
    inverse=True,
)
card_info = dbc.Card(
    [
        dbc.CardHeader(
            "Information",
            className="card-title mb-0",
            
        ),
        
        dbc.CardBody(
            "In development - 2020",
            className = "card-body mb-0",
                ),
    ],
    color="dark",
    inverse=True,
)
# --------------------------------------- LAYOUT ---------------------------------------
app.layout = dbc.Container(
    [
        html.Div(
            [
                # row1: logos
                dbc.Row(
                    dbc.Col(img_ds),
                    align="center",
                    className="mb-5",
                ),
                # row2: login
                dbc.Row(
                    dbc.Col(card_login, width={"size": 6, "offset": 3}),
                    align="center",
                    className="mb-5",   
                ),
                # row3 : info
                dbc.Row(
                    dbc.Col(card_info, width={"size": 3,}),
                    className = "mb-5",
                ),
            ]
        )
    ]
)

# %%
if __name__ == "__main__":
    app.run_server(
        debug=True,
        host="0.0.0.0",
        port="8080",
    )
