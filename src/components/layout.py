from dash import html
from src.components import uploads, loadings, dropdowns, buttons


def create_main_layout() -> html.Div:
    return html.Div(
        className="body",
        children=[
            # html.H1(app.title),
            # Header
            html.Div(
                [
                    html.H1(
                        children='Welcome to HahoML',
                        style={'textAlign': 'center'},
                    ),
                    html.P(
                        children='Where ML made easier than ever!',
                        style={'textAlign': 'center'},
                    ),
                ],
                className='header-container',
            ),

            html.Hr(),

            # upload data Container
            uploads.upload_data(),

            # Data Table container
            loadings.data_table(),

            html.Br(),

            # Dropdowns container
            html.Div(
                [
                    # Problem Dropdown container
                    dropdowns.problems(),
                
                    # Attributes Dropdown container
                    dropdowns.attributes(),
                    
                    # Model Dropdown container
                    dropdowns.models(),

                    # Feature Engineering Dropdown container
                    dropdowns.feature_engineering(),

                    # Manuel Feature Selection Dropdown container
                    dropdowns.manuel_feature_selection(),
                ],
                className='dropdowns-container',
            ),

            # Submit Button
            buttons.submit_button(),

            # results
            loadings.results(),
        ],
    )