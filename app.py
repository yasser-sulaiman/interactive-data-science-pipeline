from dash import Dash

app = Dash(__name__, use_pages=True)

def main():
    app = Dash(__name__, use_pages=True)
    app.title = "Interactive Data Science Pipeline"
    app.run(debug=True)

if __name__ == '__main__':
    print('Starting...')
    main()