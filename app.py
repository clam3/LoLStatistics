from flask import Flask
from riotwatcher import LolWatcher, ApiError

app = Flask(__name__)

import config


API_KEY = config.api_key

@app.route('/')
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run()