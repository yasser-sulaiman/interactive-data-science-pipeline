from dash import Dash
from dash import html, dcc
import dash

app = Dash(__name__, use_pages=True)

def main():
    app = Dash(__name__, use_pages=True)
    app.title = "Interactive Data Science Pipeline"

    app.layout = html.Div([
        # Header
        html.Div(
            [
                html.H1(
                    children='Welcome to HahoML',
                    style={'textAlign': 'center'},
                ),
                html.P(
                    children='Where ML made easier than ever!',
                    style={'textAlign': 'center'},
                ),
                html.Div(
                    dcc.Link("Train", href="/")
                ),
                html.Div(
                    dcc.Link(f"Visualize", href="/visualization")
                )
            ],
            className='header-container',
        ),

        html.Hr(),

        dash.page_container
    ])
    app.run(debug=True)

if __name__ == '__main__':
    print('Starting...')
    main()