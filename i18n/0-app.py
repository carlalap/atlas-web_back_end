#!/usr/bin/env python3
"""task0. Basic Flask app"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def my_home():
    """Method template that simply outputs a message"""
    return render_template('./0-index.html')


if __name__ == '__main__':
    app.run()
