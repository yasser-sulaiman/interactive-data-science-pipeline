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
            ########################## Single Attribute ########################
            html.Div("Single Attribute Info Container"),

            html.Div(
                className="single-attribute-info-container",
                id=ids.SINGLE_ATTRIBUTE_INFO_CONTAINER,
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
                        id=ids.SINGLE_ATTRIBUTE_GRAPH_CONTAINER,
                    )
                ]
            ),

            ########################## Two Attributes ########################
            html.Div("Two Attribute Info Container"),

            html.Div(
                className="two-attribute-info-container",
                id=ids.TWO_ATTRIBUTES_INFO_CONTAINER,
                children=[
                    html.Div(
                        dropdowns.select_attributes(
                            ids.SELECT_TWO_ATTRIBUTES_DROPDOWN1,
                            multiple=False
                        ),
                        className="two-attribute-dropdown-container"
                    ),

                    html.Div(
                        dropdowns.select_attributes(
                            ids.SELECT_TWO_ATTRIBUTES_DROPDOWN2,
                            multiple=False
                        ),
                        className="two-attribute-dropdown-container"
                    ),

                    html.Br(),

                    html.Div(
                        dcc.Graph(id=ids.TWO_ATTRIBUTES_GRAPH),
                        id=ids.TWO_ATTRIBUTES_GRAPH_CONTAINER,
                    )
                ]
            ),

            html.Br(),

            ########################## THREE Attributes ########################
            html.Div("Three Attribute Info Container"),

            html.Div(
                className="three-attribute-info-container",
                id=ids.THREE_ATTRIBUTES_INFO_CONTAINER,
                children=[
                    html.Div(
                        dropdowns.select_attributes(
                            ids.SELECT_THREE_ATTRIBUTES_DROPDOWN1,
                            multiple=False
                        ),
                        className="three-attribute-dropdown-container"
                    ),

                    html.Div(
                        dropdowns.select_attributes(
                            ids.SELECT_THREE_ATTRIBUTES_DROPDOWN2,
                            multiple=False
                        ),
                        className="three-attribute-dropdown-container"
                    ),

                    html.Div(
                        dropdowns.select_attributes(
                            ids.SELECT_THREE_ATTRIBUTES_DROPDOWN3,
                            multiple=False
                        ),
                        className="three-attribute-dropdown-container"
                    ),

                    html.Br(),

                    html.Div(
                        dcc.Graph(id=ids.THREE_ATTRIBUTES_GRAPH),
                        id=ids.THREE_ATTRIBUTES_GRAPH_CONTAINER,
                    )
                ]
            ),

            html.Br(),

            ########################## Correlation Matrix ########################
            html.Div("Correlation Matrix"),

            html.Div(
                className="correlation-matrix-container",
                id=ids.CORRELATION_MATRIX,
                children=[
                    html.Div(
                        dropdowns.select_attributes(
                            ids.SELECT_CORRELATION_MATRIX_ATTRIBUTES_DROPDOWN,
                            multiple=True
                        ),
                        className="multiple-attribute-dropdown-container"
                    ),

                    html.Br(),

                    html.Div(
                        dcc.Graph(id=ids.CORRELATION_MATRIX_GRAPH),
                        id=ids.CORRELATION_MATRIX_GRAPH_CONTAINER,
                    )
                ]
            )
        ])

