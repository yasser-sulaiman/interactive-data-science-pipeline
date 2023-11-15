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
        Output(ids.SELECT_TWO_ATTRIBUTES_DROPDOWN1, 'options'),
        Output(ids.SELECT_TWO_ATTRIBUTES_DROPDOWN2, 'options'),
        Output(ids.SELECT_THREE_ATTRIBUTES_DROPDOWN1, 'options'),
        Output(ids.SELECT_THREE_ATTRIBUTES_DROPDOWN2, 'options'),
        Output(ids.SELECT_THREE_ATTRIBUTES_DROPDOWN3, 'options'),
        Output(ids.SELECT_CORRELATION_MATRIX_ATTRIBUTES_DROPDOWN, 'options'),
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
            attributes = df_head.columns.values
            return (
                df_head.to_dict('records'),
                [{'name': i, 'id': i} for i in df_head.columns],
                attributes,
                attributes,
                attributes,
                attributes,
                attributes,
                attributes,
                attributes,
            )

    return [], [], [], [], [], [], [], [], []


@callback(
    Output(ids.SINGLE_ATTRIBUTE_GRAPH_CONTAINER, 'children'),
    [
        Input(ids.SELECT_SINGLE_ATTRIBUTE_DROPDOWN, 'value'),
        Input(ids.SINGLE_ATTRIBUTE_PLOT_TYPE_DROPDOWN, 'value')
    ],
    prevent_initial_callbacks=True,
)
def update_single_attribute_graph(col, plot_type):
    global DATA
    
    if DATA is not None and col is not None:

        temp_data = DATA[col]

        if plot_type == "Histogram":
            fig = px.histogram(temp_data)

        elif plot_type == "Box":
            fig = px.box(temp_data)
        
        elif plot_type == "Bar":
            fig = px.bar(temp_data)
        
        else:
            fig = {}

        graph = dcc.Graph(figure=fig)

        return graph
    else:
        return []


@callback(
    Output(ids.TWO_ATTRIBUTES_GRAPH_CONTAINER, 'children'),
    [
        Input(ids.SELECT_TWO_ATTRIBUTES_DROPDOWN1, 'value'),
        Input(ids.SELECT_TWO_ATTRIBUTES_DROPDOWN2, 'value'),
        Input(ids.TWO_ATTRIBUTE_PLOT_TYPE_DROPDOWN, 'value')
    ],
    prevent_initial_callbacks=True,
)
def update_two_attributes_graph(col1, col2, plot_type):
    global DATA
    if DATA is not None and col1 is not None and col2 is not None:
        data_x = DATA[col1]
        data_y = DATA[col2]

        if plot_type == "Scatter":
            fig = px.scatter(x=data_x, y=data_y, labels={'x':col1, 'y':col2})
        
        elif plot_type == "Line":
            fig = px.line(x=data_x, y=data_y, labels={'x':col1, 'y':col2})
        
        else:
            fig = {}

        graph = dcc.Graph(figure=fig)

        return graph
    
    else:
        return []


@callback(
    Output(ids.THREE_ATTRIBUTES_GRAPH_CONTAINER, 'children'),
    [
        Input(ids.SELECT_THREE_ATTRIBUTES_DROPDOWN1, 'value'),
        Input(ids.SELECT_THREE_ATTRIBUTES_DROPDOWN2, 'value'),
        Input(ids.SELECT_THREE_ATTRIBUTES_DROPDOWN3, 'value'),
        Input(ids.THREE_ATTRIBUTE_PLOT_TYPE_DROPDOWN, 'value')
    ],
    prevent_initial_callbacks=True,
)
def update_three_attributes_graph(col1, col2, col3, plot_type):
    global DATA
    if (DATA is not None) and \
        (col1 is not None) and \
        (col2 is not None) and \
        (col3 is not None):

        if plot_type == "Scatter 2D":
            fig = px.scatter(DATA, x=col1, y=col2, color=col3, labels={'x':col1, 'y':col2, 'z':col3})

        elif plot_type == "Scatter 3D":
            fig = px.scatter_3d(DATA, x=col1, y=col2, z=col3) # , labels={'x':col1, 'y':col2, 'z':col3}
        
        else:
            fig = {}

        graph = dcc.Graph(figure=fig)

        return graph
    else:
        return []


@callback(
    Output(ids.CORRELATION_MATRIX_GRAPH_CONTAINER, 'children'),
    Input(ids.SELECT_CORRELATION_MATRIX_ATTRIBUTES_DROPDOWN, 'value'),
    prevent_initial_callbacks=True,
)
def update_correlation_matrix_graph(col):
    global DATA
    if DATA is not None and col is not None:
        corr_data = DATA[col]
        corr_matrix = corr_data.corr()
        fig = px.imshow(corr_matrix, text_auto=True, aspect="auto")
        graph = dcc.Graph(figure=fig)
        return graph
    else:
        return [] 
    