from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def link_welcome():
    return "WELCOME"

@app.route('/welcome/home')
def link_home():
    return "WELCOME HOME"

@app.route('/welcome/back')
def link_back():
    return "WELCOME BACK"

