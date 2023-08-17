from dash import html
from src.components.ids import SUBMIT_BUTTON_CONTAINER

def submit_button():
    btn = html.Div(
            html.Button('Submit', id='submit-button', n_clicks=0),
            id=SUBMIT_BUTTON_CONTAINER,
            className='invisible',
        )
    return btn