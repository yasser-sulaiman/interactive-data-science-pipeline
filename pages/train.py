import dash

from callbacks.train_callbacks import *
from src.components.layout import create_train_layout

dash.register_page(__name__, path='/')

layout = create_train_layout()