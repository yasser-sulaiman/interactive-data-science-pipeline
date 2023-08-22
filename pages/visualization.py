import dash

from callbacks.vis_callbacks import *
from src.components.layout import create_visualization

dash.register_page(__name__, path='/visualization')

layout = create_visualization()