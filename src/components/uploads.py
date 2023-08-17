from dash import html, dcc 
from src.components.ids import UPLOAD_DATA

def upload_data():
    upload = html.Div(
                # upload data button
                children = dcc.Upload(
                                id=UPLOAD_DATA,
                                children=html.Div(
                                    [
                                        'Drag and Drop or ',
                                        html.A('Select Files'),
                                    ],
                                ),
                                multiple=False,
                                className='upload-button',
                            ),
                className='upload-data-container',
            )
    return upload