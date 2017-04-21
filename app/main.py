from __future__ import print_function
from flask import Flask, render_template

app = Flask(__name__, static_path='/static')

@app.route('/')
def index():
    return 'awesome'

if __name__ == '__main__':
    app.run()
