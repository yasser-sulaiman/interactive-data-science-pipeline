from dash import html
from src.components import uploads, loadings, dropdowns, buttons, ids


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
            uploads.upload_data(ids.UPLOAD_DATA_MAIN),

            # Data Table container
            loadings.data_table(ids.DATA_TABLE_MAIN),

            html.Br(),

            # Dropdowns container
            html.Div(
                [
                    # Problem Dropdown container
                    dropdowns.problems(),
                
                    # Attributes Dropdown container
                    dropdowns.select_target(),
                    
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


def create_visualization() -> html.Div:
    return html.Div(
        className='body',
        children=[
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
            uploads.upload_data(ids.UPLOAD_DATA_VIS),

            # Data Table container
            loadings.data_table(ids.DATA_TABLE_VIS),

            html.Br(),

            html.Div(
                className="single-attribute-info",
                children=[
                    dropdowns.select_attributes(ids.SELECT_SINGLE_ATTRIBUTE_CONTAINER,
                                                ids.SELECT_SINGLE_ATTRIBUTE_DROPDOWN,
                                                multiple=False)
                ]
            )
        ])

