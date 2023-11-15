from dash import  html, dcc
from src.components import ids

def problems():
    dropdown = html.Div([
                        'Select Your Problem',
                        dcc.Dropdown(
                            options=[
                                {
                                    'label': 'Classification',
                                    'value': 'classification',
                                    'disabled': False,
                                },
                                {
                                    'label': 'Regression',
                                    'value': 'regression',
                                    'disabled': True,
                                },
                                {
                                    'label': 'Clustering',
                                    'value': 'clustering',
                                    'disabled': True,
                                },
                            ],
                            id=ids.PROBLEMS_DROPDOWN,
                            placeholder="Select Problem's Type",
                            value='',
                        ),
                    ],
                    id=ids.SELECT_PROBLEM_CONTAINER,
                    className='invisible',
                )
    return dropdown


def select_target():
    dropdown = html.Div([
                        'Select The Target Variable',
                        dcc.Dropdown(
                            id=ids.TARGET_DROPDOWN,
                            placeholder='Select a Target Variable',
                            ),
                        ],
                    id=ids.SELECT_TARGET_CONTAINER,
                    className='invisible-dropdown',
                )
    return dropdown


def models():
    dropdown = html.Div([
                        'Select A Model',
                        dcc.Dropdown(
                            options=[
                                {
                                    'label': 'Logistic Regression',
                                    'value': 'logistic-regression',
                                    'disabled': False,
                                },
                                {
                                    'label': 'K-Nearest Neighbor',
                                    'value': 'knn',
                                    'disabled': False,
                                },
                                {
                                    'label': 'Decision Tree',
                                    'value': 'd-tree',
                                    'disabled': False,
                                },
                            ],
                            id=ids.MODELS_DROPDOWN,
                            placeholder='Select a Model',
                            value='',
                        ),
                    ],
                    id=ids.SELECT_MODEL_CONTAINER,
                    className='invisible',
                )
    return dropdown


def feature_engineering():
    dropdown = html.Div([
                        'Feature Engineering First?',
                        dcc.Dropdown(
                            options=[
                                {
                                    'label': 'Manual Feature Selection',
                                    'value': 'manual',
                                    'disabled': False,
                                },
                                {'label': 'YES', 'value': 'yes', 'disabled': True},
                                {'label': 'NO', 'value': 'no', 'disabled': False},
                            ],
                            id=ids.FEATURE_DROPDOWN,
                            value='',
                        ),
                    ],
                    id=ids.SELECT_FEATURE_CONTAINER,
                    className='invisible',
                )
    return dropdown


def manuel_feature_selection():
    dropdown = html.Div([
                        'Select Wanted Features',
                        dcc.Dropdown(
                            options=[],
                            id=ids.MANUEL_FEATURE_DROPDOWN,
                            value='',
                            multi=True,
                        ),
                    ],
                    id=ids.SELECT_MANUEL_FEATURE_CONTAINER,
                    className='invisible',
                )
    return dropdown


def select_attributes(dd_id, label="Select an Attribute", multiple=False):
    dropdown = html.Div([
                    label,
                    dcc.Dropdown(
                            id=dd_id,
                            placeholder='Select an Attribute',
                            multi=multiple,
                        ),
                    ],
                )
    return dropdown


def select_plot_type(dd_id, n_attributes,multiple=False):
    if n_attributes == "one":
        options = ["Histogram", "Box", "Bar"]
        dropdown = html.Div([
                        'Select a Plot Type',
                        dcc.Dropdown(
                                options=options,
                                id=dd_id,
                                placeholder='Select a Plot Type',
                                multi=multiple,
                                value="Histogram"
                            ),
                        ],
                    )
        
    elif n_attributes == "two":
        options = ["Scatter", "Line"]
        dropdown = html.Div([
                        'Select a Plot Type',
                        dcc.Dropdown(
                                options=options,
                                id=dd_id,
                                placeholder='Select a Plot Type',
                                multi=multiple,
                                value="Scatter"
                            ),
                        ],
                    )
        
    elif n_attributes == "three":
        options = ["Scatter 2D", "Scatter 3D"]
        dropdown = html.Div([
                        'Select a Plot Type',
                        dcc.Dropdown(
                                options=options,
                                id=dd_id,
                                placeholder='Select a Plot Type',
                                multi=multiple,
                                value="Scatter 2D"
                            ),
                        ],
                    )
        
    return dropdown
