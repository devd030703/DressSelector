# %%
import base64
import os

import dash_bootstrap_components as dbc
import dash_html_components as html

import dash

# %%
# ----------------------------------- DATA ------------------------------------
logo_image = os.path.join("images", "ds_logo.png")
title_image = os.path.join("images", "models.png")

# recipe classification
recipe_classification_image = os.path.join("images", "recipe_classification.png")
recipe_classification_app_link = (
    "https://recipe-classification-dev-eun-web.azurewebsites.net"
)
recipe_classification_google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLSft8vT9zybUeyDSr8gRGCdC96ZJKHlLkL7qbli_irKvF7XOAQ/viewform?usp=sf_link"

# marketing classification
marketing_classification_image = os.path.join("images", "marketing_classification.png")
marketing_classification_app_link = (
    "https://marketing-classification-dev-eun-web.azurewebsites.net"
)
marketing_classification_google_form_link = "https://docs.google.com/forms/d/e/1FAIpQLSfMAiz5Y0NzUXWiYb1UIuzYFf291haoGBgNzjXnabO2WgwEaw/viewform?usp=sf_link"

# %%
# ------------------------------------ APP ------------------------------------
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

# ----------------------------------- IMAGES ----------------------------------
ds_logo_encoded = base64.b64encode(open(logo_image, "rb").read())

img_ds = html.Img(
    src=f"data:image/png;base64,{ds_logo_encoded.decode()}",
    style={
        "float": "centre",
        "width": "50%",
    },
)

# ----------------------------------- CARDS -----------------------------------
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
                    className="mb-5",
                ),
                dbc.Input(
                    id="input_password",
                    placeholder="password",
                    type="text",
                    className="mb-5",
                ),
                dbc.Row(
                    [
                        dbc.Button(
                            "login",
                            color="primary",
                        ),
                        dbc.Button(
                            "signup",
                            color="primary",
                        ),
                    ]
                ),
            ]
        ),
    ],
    color="light",
    inverse=True,
)

# ----------------------------------- LAYOUT ----------------------------------
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
