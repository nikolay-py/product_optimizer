"""Initialization of Flask app."""
from webapp import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1155)