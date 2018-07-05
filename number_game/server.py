from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'SecretKey'
import random

@app.route('/')

def index():
    session['someKey'] = 50
    session['guesses'] = random.randint(0, 101)
    return render_template("index.html")

@app.route('/num', methods=['POST'])
def ninja():

    session['guess'] = request.form['guess']

    if int(session['guess']) > session['guesses']:
        return render_template("toohigh.html", hint = "Too high!")
    elif int(session['guess']) < session['guesses']:
        return render_template("toolow.html", hint = "Too low!")
    elif int(session['guess']) == session['guesses']:
        return render_template("correct.html", hint = "You got it!")


@app.route('/clear', methods = ['GET'])
def clear():
    session.pop('someKey')
    return redirect('/')




app.run(debug=True)
