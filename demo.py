import json
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def demo():
    with open('data/images.json') as fid:
        images = json.load(fid)
    return render_template('demo.html', images=images)
