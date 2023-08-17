from __future__ import annotations

from dash import callback
from dash import dash_table
from dash import dcc
from dash import html
from dash import Input
from dash import Output
from dash import State

from model.models import train_supervised
from processing.data_cleaning import clean_data
from processing.feature_engineering import select_features
from utils.utils import parse_contents


DATA = None
X = None
SELECTED_COLUMNS = None
Y = None


@callback(
    [
        Output('data-table', 'data'),
        Output('data-table', 'columns'),
        Output('target-dropdown-selection', 'options'),
        Output('select-problem-container', 'className'),
    ],
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename')],
    prevent_initial_callbacks=True,
)
def upload_data(list_of_contents, list_of_names):
    global DATA

    if list_of_contents is not None:
        df = parse_contents(list_of_contents, list_of_names)
        # save data to the global DATA variable
        DATA = df.copy()

        if len(df) > 0:
            df_head = df.head(10)
            del df
            return (
                df_head.to_dict('records'),
                [{'name': i, 'id': i} for i in df_head.columns],
                df_head.columns.values,
                'visible-dropdown',
            )

    return [], [], [], 'invisible'


@callback(
    Output('select-target-container', 'className'),
    Input('problem-dropdown-selection', 'value'),
    prevent_initial_callbacks=True,
)
def select_problem(problem):
    if problem == '' or problem is None:
        return 'invisible'

    return 'visible-dropdown'


@callback(
    Output('select-model-container', 'className'),
    Input('target-dropdown-selection', 'value'),
    prevent_initial_callbacks=True,
)
def select_target(target):
    global DATA, X, Y

    if target == '' or target is None:
        return 'invisible'

    # clean data (drop na / fill na)
    DATA = clean_data(DATA, target)
    # store target to Y and features to X global variables
    Y = DATA[target]
    X = DATA.drop(target, axis=1)

    return 'visible-dropdown'


@callback(
    Output('select-feature-container', 'className'),
    Input('model-dropdown-selection', 'value'),
    prevent_initial_callbacks=True,
)
def select_model(model):
    if model == '' or model is None:
        return 'invisible'
    return 'visible-dropdown'


@callback(
    Output('submit-button-container', 'className'),
    Output('select-manual-feature-container', 'className'),
    Output('manuel-feature-selection', 'options'),
    Input('feature-dropdown-selection', 'value'),
    prevent_initial_callbacks=True,
)
def feature_selection(value):
    global X, SELECTED_COLUMNS
    if value == '' or value is None:
        return 'invisible', 'invisible', []

    elif value == 'manual':
        return 'invisible', 'visible-dropdown', X.columns.values

    elif value == 'yes':
        # should update SELECTED_COLUMNS after applying feature engineering
        SELECTED_COLUMNS = select_features(X, Y)
        return 'submit-button', 'invisible', []

    SELECTED_COLUMNS = X.columns.values
    return 'submit-button', 'invisible', []


@callback(
    Output('submit-button-container', 'className', allow_duplicate=True),
    Input('manuel-feature-selection', 'value'),
    prevent_initial_call=True,
)
def manuel_feature_selection(value):
    global X, SELECTED_COLUMNS

    if value is None or not value:
        pass
    else:
        SELECTED_COLUMNS = value

    return 'submit-button'


@callback(
    Output('results-container', 'children'),
    Output('results-container', 'className'),
    Input('submit-button', 'n_clicks'),
    State('problem-dropdown-selection', 'value'),
    State('target-dropdown-selection', 'value'),
    State('model-dropdown-selection', 'value'),
    State('feature-dropdown-selection', 'value'),
)
def submit(n_clicks, problem, target, model, feature):
    if not n_clicks:
        return '', 'invisible'
    result = f'It is a {problem} problem\n'
    result += f'The target variable is: {target}\n'
    print(f'Used Column set: {SELECTED_COLUMNS}')
    trained_model_info = train_supervised(X[SELECTED_COLUMNS], Y, model)
    test_acc = trained_model_info['test_acc']
    train_acc = trained_model_info['train_acc']
    result += f'\n Test Accuracy is: {round(test_acc, 2)*100} \n'
    result += f'\n Train Accuracy is: {round(train_acc, 2)*100} \n'
    return result, 'results-container '
