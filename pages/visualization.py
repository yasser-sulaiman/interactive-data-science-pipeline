import dash

from callbacks.vis_callbacks import *
from src.components.layout import create_visualization_layout

dash.register_page(__name__, path='/visualization')

layout = create_visualization_layout()