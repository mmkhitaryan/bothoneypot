from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/<path:dummy>')
def index(dummy=None):
    return 'Hello'