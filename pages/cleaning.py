import dash

from callbacks.clean_callbacks import *
from src.components.layout import create_cleaning_layout

dash.register_page(__name__, path='/cleaning')

layout = create_cleaning_layout()