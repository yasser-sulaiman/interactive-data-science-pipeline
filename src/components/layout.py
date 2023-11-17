from dash import html, dcc
from src.components import uploads, loadings, dropdowns, buttons, ids


def create_cleaning_layout()-> html.Div:
     return html.Div(
        className="body",
        children=[
            # upload data Container
            uploads.upload_data(ids.UPLOAD_DATA_CLEANING),

            # Data Table container
            loadings.data_table(ids.DATA_TABLE_CLEANING),

            html.Br(),

            # Data Summary Container
            html.Div(
                children=[html.Img(src='assets/clean-me.png', style={'width': '80%', 'height': '720px'})],
                id=ids.DATA_SUMMARY_CONTAINER,
                className="data-summary-container"
                
            )

        ],
    )


def create_visualization_layout() -> html.Div:
    return html.Div(
        className='content',
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
                        children=[
                            html.Div(
                                dropdowns.select_attributes(
                                    ids.SELECT_SINGLE_ATTRIBUTE_DROPDOWN,
                                    multiple=False
                                ),
                                className="single-attribute-dropdown-container"
                            ),

                            html.Div(
                                dropdowns.select_plot_type(
                                    ids.SINGLE_ATTRIBUTE_PLOT_TYPE_DROPDOWN,
                                    n_attributes = "one",
                                    multiple=False
                                ),
                                className="single-attribute-dropdown-container"
                            )
                        ],
                        className="vis-dropdowns-container"
                    ),

                    html.Br(),

                    html.Div(
                        id=ids.SINGLE_ATTRIBUTE_GRAPH_CONTAINER,
                        className="visual-container"
                    )
                ]
            ),

            ########################## Two Attributes ########################
            html.Div("Two Attribute Info Container"),

            html.Div(
                className="two-attributes-info-container",
                id=ids.TWO_ATTRIBUTES_INFO_CONTAINER,
                children=[
                    html.Div(
                        children=[
                            html.Div(
                                dropdowns.select_attributes(
                                    ids.SELECT_TWO_ATTRIBUTES_DROPDOWN1,
                                    "Select X-Axis",
                                    multiple=False
                                ),
                                className="two-attributes-dropdown-container"
                            ),

                            html.Div(
                                dropdowns.select_attributes(
                                    ids.SELECT_TWO_ATTRIBUTES_DROPDOWN2,
                                    "Select Y-Axis",
                                    multiple=False
                                ),
                                className="two-attributes-dropdown-container"
                            ),

                            html.Div(
                                dropdowns.select_plot_type(
                                    ids.TWO_ATTRIBUTE_PLOT_TYPE_DROPDOWN,
                                    n_attributes = "two",
                                    multiple=False
                                ),
                                className="single-attribute-dropdown-container"
                            )
                        ],
                        className="vis-dropdowns-container"
                    ),

                    html.Br(),

                    html.Div(
                        id=ids.TWO_ATTRIBUTES_GRAPH_CONTAINER,
                        className="visual-container",
                    )
                ]
            ),

            html.Br(),

            ########################## THREE Attributes ########################
            html.Div("Three Attribute Info Container"),

            html.Div(
                className="three-attributes-info-container",
                id=ids.THREE_ATTRIBUTES_INFO_CONTAINER,
                children=[
                    html.Div(
                        children=[
                                    
                            html.Div(
                                dropdowns.select_attributes(
                                    ids.SELECT_THREE_ATTRIBUTES_DROPDOWN1,
                                    "Select X-Axis",
                                    multiple=False
                                ),
                                className="three-attributes-dropdown-container"
                            ),

                            html.Div(
                                dropdowns.select_attributes(
                                    ids.SELECT_THREE_ATTRIBUTES_DROPDOWN2,
                                    "Select Y-Axis",
                                    multiple=False
                                ),
                                className="three-attributes-dropdown-container"
                            ),

                            html.Div(
                                dropdowns.select_attributes(
                                    ids.SELECT_THREE_ATTRIBUTES_DROPDOWN3,
                                    "Select Z-Axis",
                                    multiple=False
                                ),
                                className="three-attributes-dropdown-container"
                            ),

                            html.Div(
                                dropdowns.select_plot_type(
                                    ids.THREE_ATTRIBUTE_PLOT_TYPE_DROPDOWN,
                                    n_attributes = "three",
                                    multiple=False
                                ),
                                className="single-attribute-dropdown-container"
                            )
                        ],
                        className="vis-dropdowns-container"
                    ),
                    html.Br(),

                    html.Div(
                        id=ids.THREE_ATTRIBUTES_GRAPH_CONTAINER,
                        className="visual-container"
                    )
                ]
            ),

            html.Br(),

            ########################## Correlation Matrix ########################
            html.Div("Correlation Matrix"),
    
            html.Div(
                className="correlation-matrix-info-container",
                id=ids.CORRELATION_MATRIX,
                children=[
                    html.Div(
                        html.Div(
                            dropdowns.select_attributes(
                                ids.SELECT_CORRELATION_MATRIX_ATTRIBUTES_DROPDOWN,
                                multiple=True
                            ),
                            className="correlation-matrix-attributes-dropdown-container"
                        ),
                        className="vis-dropdowns-container"
                    ),

                    html.Br(),

                    html.Div(
                        id=ids.CORRELATION_MATRIX_GRAPH_CONTAINER,
                        className="visual-container"
                    ),
            
                    html.Br(),
                    html.Div("-------")
                ]
            )
        ])


def create_train_layout() -> html.Div:
    return html.Div(
        className="body",
        children=[
            # upload data Container
            uploads.upload_data(ids.UPLOAD_DATA_TRAIN),

            # Data Table container
            loadings.data_table(ids.DATA_TABLE_TRAIN),

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

