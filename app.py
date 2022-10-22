from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/secondLink')
def secondLink():
    return render_template('second.html')