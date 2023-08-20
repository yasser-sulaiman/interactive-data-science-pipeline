from dash import html, dcc 

def upload_data(id):
    upload = html.Div(
                # upload data button
                children = dcc.Upload(
                                id=id,
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