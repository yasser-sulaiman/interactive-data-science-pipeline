from dash import callback
from dash import dash_table
from dash import dcc
from dash import html
from dash import Input
from dash import Output
from dash import State
import plotly.express as px

from utils.utils import parse_contents
from src.components import ids


DATA = None
X = None
SELECTED_COLUMNS = None
Y = None
@callback(
    [
        Output(ids.DATA_TABLE_VIS, 'data'),
        Output(ids.DATA_TABLE_VIS, 'columns'),
        Output(ids.SELECT_SINGLE_ATTRIBUTE_DROPDOWN, 'options'),
        Output(ids.SINGLE_ATTRIBUTE_INFO, 'className'),
    ],
    [Input(ids.UPLOAD_DATA_VIS, 'contents')],
    [State(ids.UPLOAD_DATA_VIS, 'filename')],
    prevent_initial_callbacks=True,
    
)
def upload_data_vis(list_of_contents, list_of_names):
    global DATA

    if list_of_contents is not None:
        DATA = parse_contents(list_of_contents, list_of_names)

        if len(DATA) > 0:
            df_head = DATA.head(10)
            return (
                df_head.to_dict('records'),
                [{'name': i, 'id': i} for i in df_head.columns],
                df_head.columns.values,
                "single-attribute-info",
            )

    return [], [], [], 'invisible'


@callback(
    Output('single-attribute-graph', 'figure'),
    Output('single-attribute-visual-container', 'className'),
    Input(ids.SELECT_SINGLE_ATTRIBUTE_DROPDOWN, 'value'),
    prevent_initial_callbacks=True,
)
def update_single_attribute_graph(col):
    global DATA
    if DATA is not None and col is not None:
        column = DATA[col]
        return px.histogram(column), "single-attribute-visual-container"
    else:
        return {}, 'invisible'
