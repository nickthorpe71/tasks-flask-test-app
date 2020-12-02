# SETUP: https://realpython.com/flask-by-example-part-1-project-setup/

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def tasks():
    return "TASKS"

@app.route("/add")
def add():
    return "ADD A NEW TRACK"

if __name__ == '__main__':
    app.run()
