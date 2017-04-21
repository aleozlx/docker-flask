from __future__ import print_function
from flask import Flask, render_template

app = Flask(__name__, static_path='/static')

@app.route('/a.json')
def _a():
    return """{
    "ds1/title1":
        [{
            "src": "ddjsk",
            "prediction": 2
        },{
            "src": "vsdsaf",
            "prediction": 3
        },
        {
            "src": "vew",
            "prediction": 7
        },{
            "src": "breds",
            "prediction": 0
        }],
    "ds1/title2":
        [{
            "src": "vcaw",
            "prediction": 2
        },{
            "src": "gewqt",
            "prediction": 1
        },
        {
            "src": "bkjie",
            "prediction": 0
        },{
            "src": "iewoiiiknv",
            "prediction": 7
        }],
    "ds2/title1":
        [{
            "src": "mskein",
            "prediction": 2
        },{
            "src": "op3",
            "prediction": 5
        },
        {
            "src": "32532",
            "prediction": 5
        },{
            "src": "lol",
            "prediction": 6
        }]
}"""

if __name__ == '__main__':
    app.run()
