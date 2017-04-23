from __future__ import print_function
from flask import Flask, render_template

app = Flask(__name__, static_path='/static')

srcs = ["""{
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
}""",

"""{
    "ds1/title1":
        [{
            "src": "ddjsk",
            "prediction": 2
        },{
            "src": "vsdsaf",
            "prediction": 3.14
        },
        {
            "src": "vew",
            "prediction": 7.52
        },{
            "src": "breds",
            "prediction": 0.23
        }],
    "ds1/title2":
        [{
            "src": "vcaw",
            "prediction": 2.78
        },{
            "src": "gewqt",
            "prediction": 1.4
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
}""",


"""{
    "ds1/title1":
        [{
            "src": "ddjsk",
            "prediction": 2
        },{
            "src": "vsdsaf",
            "prediction": 3.14
        },
        {
            "src": "vew",
            "prediction": 7.52
        },{
            "src": "breds"
        }],
    "ds1/title2":
        [{
            "src": "vcaw",
            "prediction": 2.78
        },{
            "src": "gewqt",
            "prediction": 1.4
        },
        {
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
}""",

"""{
    "ds1/title1":
        [{
            "src": "ddjsk",
            "prediction": 2
        },{
            "src": "vsdsaf",
            "prediction": 3.14
        },
        {
            "src": "vew",
            "prediction": 7.52
        },{
            "src": "breds"
        }],
}""",



("", 500)

]

@app.route('/a.json')
def _a():
    return srcs[0]

@app.route('/b.json')
def _b():
    return srcs[1]

@app.route('/c.json')
def _c():
    return srcs[2]

@app.route('/d.json')
def _d():
    return srcs[3]

import random
@app.route('/e.json')
def _e():
    return random.choice(srcs)

@app.route('/f.json')
def _f():
    return srcs[4]


if __name__ == '__main__':
    app.run()
