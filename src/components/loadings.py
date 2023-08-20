from dash import dcc, html, dash_table
from src.components.ids import RESULTS_CONTAINER

def data_table(id):
    spinner = dcc.Loading(
                    html.Div(
                        children=dash_table.DataTable(
                            id=id,
                            data=[],
                            columns=[],
                        ),
                        className='data-table-container',
                    ),
                    type='cube',
                )
    return spinner


def results():
    spinner = dcc.Loading(
                html.Div(
                    children='Here Goes The Results',
                    id=RESULTS_CONTAINER,
                    className='invisible',
                ),
                type='default',
            )
    return spinner

