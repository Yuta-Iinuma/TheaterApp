from flask import Flask, render_template, jsonify, request
import json
import pandas as pd


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test', methods=['POST'])
def test():
    location = request.form.getlist('location')
    print(location)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, use_debugger=False)
