#!/usr/bin/env python3
""" flask app
"""


from flask import Flask, render_template

application = Flask(__name__)


@app.route('/')
def hello_world():
    """_summary_
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    application.run(port="5000", host="0.0.0.0", debug=True)
