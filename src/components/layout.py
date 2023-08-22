from dash import html, dcc
from src.components import uploads, loadings, dropdowns, buttons, ids


def create_main_layout() -> html.Div:
    return html.Div(
        className="body",
        children=[
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
            # upload data Container
            uploads.upload_data(ids.UPLOAD_DATA_VIS),

            # Data Table container
            loadings.data_table(ids.DATA_TABLE_VIS),

            html.Br(),

            html.Div(
                className="single-attribute-info",
                id=ids.SINGLE_ATTRIBUTE_INFO,
                children=[
                    html.Div(
                        dropdowns.select_attributes(
                            ids.SELECT_SINGLE_ATTRIBUTE_DROPDOWN,
                            multiple=False
                        ),
                        className="single-attribute-dropdown-container"
                    ),

                    html.Br(),

                    html.Div(
                        dcc.Graph(id=ids.SINGLE_ATTRIBUTE_GRAPH),
                        id="single-attribute-visual-container",
                    )
                ]
            )
        ])

