from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, Github Base_Flask_Project! <BR> <a href="/secondLink">Second page </a>'

@app.route('/secondLink')
def secondLink():
    return 'Hello, Welcome to second page!<BR> <a href="/">Click here to go home</a>'