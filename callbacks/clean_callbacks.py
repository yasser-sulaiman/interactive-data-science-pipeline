from dash import callback
from dash import dash_table
from dash import dcc
from dash import html
from dash import Input
from dash import Output
from dash import State

from utils.utils import parse_contents, get_column_summary
from src.components import ids


DATA = None
X = None
SELECTED_COLUMNS = None
Y = None


@callback(
    [
        Output(ids.DATA_TABLE_CLEANING, 'data'),
        Output(ids.DATA_TABLE_CLEANING, 'columns'),
        Output(ids.DATA_SUMMARY_CONTAINER, 'children'),
    ],
    [Input(ids.UPLOAD_DATA_CLEANING, 'contents')],
    [State(ids.UPLOAD_DATA_CLEANING, 'filename')],
    prevent_initial_callbacks=True,
)
def upload_data_main(list_of_contents, list_of_names):
    global DATA

    if list_of_contents is not None:
        DATA = parse_contents(list_of_contents, list_of_names)

        if len(DATA) > 0:
            df_head = DATA.head(10)
            attributes=[{'name': i, 'id': i} for i in df_head.columns]

            summary=[html.Div(get_column_summary(DATA, col), className="column-summary-container") for col in DATA.columns]

            return (
                df_head.to_dict('records'),
                attributes,
                summary,
            )

    return [], [], [html.Img(src='assets/clean-me.png', style={'width': '80%', 'height': '720px'})]

