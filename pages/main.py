import dash

from callbacks.main_callbacks import *
from src.components.layout import create_main_layout

dash.register_page(__name__, path='/')

layout = create_main_layout()