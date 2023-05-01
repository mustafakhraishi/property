from flask import Flask
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY
app.config.from_pyfile('config.py')

from routes import *

if __name__ == '__main__':
    app.run(debug=True)