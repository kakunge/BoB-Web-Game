from flask import Flask, render_template

# from objects import *
from database import *

app = Flask(__name__)

player = None
monster = None

@app.route('/')
@app.route('/index')
def print_index():
    global player
    player = Player(1, "Novice")
    return render_template("index.html")

@app.route('/1')
def print_1():
    return render_template("1.html")

@app.route('/battle')
def print_battle():
    monster = Monster(1, "Normal", pseudoslimestat_n)
    return render_template("battle.html", player=player, monster=monster)

@app.route('/mypage')
def print_mypage():
    return render_template("mypage.html", player=player)

if __name__ == "__main__":
    app.run()
