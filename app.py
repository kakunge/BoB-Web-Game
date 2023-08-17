from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def print_index():
    return render_template("index.html")

@app.route('/1')
def print_1():
    return render_template("1.html")

if __name__ == "__main__":
    app.run()
