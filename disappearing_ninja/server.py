from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")

@app.route('/ninja')
def ninja():
    return render_template("ninja.html")

@app.route('/ninja/<color>')
def show_user_profile(color):
    return render_template("turtle.html", color=color)
app.run(debug=True)
