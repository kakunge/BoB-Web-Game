from flask import Flask, render_template

from objects import *

app = Flask(__name__)

player = Player(1, "Novice")

@app.route('/')
@app.route('/index')
def print_index():
    return render_template("index.html")

@app.route('/1')
def print_1():
    return render_template("1.html")

@app.route('/battle')
def print_battle():
    return render_template("battle.html", player=player)

if __name__ == "__main__":
    app.run()
