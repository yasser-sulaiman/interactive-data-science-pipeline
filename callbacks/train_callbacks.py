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
from src.components import ids


DATA = None
X = None
SELECTED_COLUMNS = None
Y = None


@callback(
    [
        Output(ids.DATA_TABLE_TRAIN, 'data'),
        Output(ids.DATA_TABLE_TRAIN, 'columns'),
        Output(ids.TARGET_DROPDOWN, 'options'),
        Output(ids.SELECT_PROBLEM_CONTAINER, 'className'),
    ],
    [Input(ids.UPLOAD_DATA_TRAIN, 'contents')],
    [State(ids.UPLOAD_DATA_TRAIN, 'filename')],
    prevent_initial_callbacks=True,
)
def upload_data_main(list_of_contents, list_of_names):
    global DATA

    if list_of_contents is not None:
        DATA = parse_contents(list_of_contents, list_of_names)

        if len(DATA) > 0:
            df_head = DATA.head(10)
            return (
                df_head.to_dict('records'),
                [{'name': i, 'id': i} for i in df_head.columns],
                df_head.columns.values,
                'visible-dropdown',
            )

    return [], [], [], 'invisible'


@callback(
    Output(ids.SELECT_TARGET_CONTAINER, 'className'),
    Input(ids.PROBLEMS_DROPDOWN, 'value'),
    prevent_initial_callbacks=True,
)
def select_problem(problem):
    if problem == '' or problem is None:
        return 'invisible'

    return 'visible-dropdown'


@callback(
    Output(ids.SELECT_MODEL_CONTAINER, 'className'),
    Input(ids.TARGET_DROPDOWN, 'value'),
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
    Output(ids.SELECT_FEATURE_CONTAINER, 'className'),
    Input(ids.MODELS_DROPDOWN, 'value'),
    prevent_initial_callbacks=True,
)
def select_model(model):
    if model == '' or model is None:
        return 'invisible'
    return 'visible-dropdown'


@callback(
    Output(ids.SUBMIT_BUTTON_CONTAINER, 'className'),
    Output(ids.SELECT_MANUEL_FEATURE_CONTAINER, 'className'),
    Output(ids.MANUEL_FEATURE_DROPDOWN, 'options'),
    Input(ids.FEATURE_DROPDOWN, 'value'),
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
    Output(ids.SUBMIT_BUTTON_CONTAINER, 'className', allow_duplicate=True),
    Input(ids.MANUEL_FEATURE_DROPDOWN, 'value'),
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
    Output(ids.RESULTS_CONTAINER, 'children'),
    Output(ids.RESULTS_CONTAINER, 'className'),
    Input(ids.SUBMIT_BUTTON, 'n_clicks'),
    State(ids.PROBLEMS_DROPDOWN, 'value'),
    State(ids.TARGET_DROPDOWN, 'value'),
    State(ids.MODELS_DROPDOWN, 'value'),
    State(ids.FEATURE_DROPDOWN, 'value'),
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
