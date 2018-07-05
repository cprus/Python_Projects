from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'SecretKey'
import random
import datetime
import time


@app.route('/')
def index():
    session['someKey'] = 50

    try:
        session['gold']
    except KeyError:
        session['gold'] = 0

    try:
        session['log']
    except KeyError:
        session['log'] = ''

    stash = session['gold']
    activity = session['log']
    return render_template("index.html", stash = session['gold'], activity = session['log'])



@app.route('/process_money', methods=['POST'])
def proc_money():
    if request.form['building'] == 'farm':
        earned = random.randint(10, 20)
        session['gold'] += earned
        session['log'] += 'Earned ' + str(earned) + ' golds from the farm!' + ' ' + str(time.ctime()) + ", "
    elif request.form['building'] == 'cave':
        earned = random.randint(5, 10)
        session['gold'] += earned
        session['log'] += 'Earned ' + str(earned) + ' golds from the cave!' + ' ' + str(time.ctime()) + ", "
    elif request.form['building'] == 'house':
        earned = random.randint(2, 5)
        session['gold'] += earned
        session['log'] += 'Earned ' + str(earned) + ' golds from the house!' + ' ' + str(time.ctime()) + ", "
    elif request.form['building'] == 'casino':
        earned = random.randint(-50, 50)
        session['gold'] += earned
        session['log'] += 'Earned ' + str(earned) + ' golds from the casino!' + ' ' + str(time.ctime()) + ", "

    stash = session['gold']
    activity = session['log']

    return redirect('/')

@app.route('/clear', methods = ['GET'])
def clear():
    session.pop('someKey')
    del session['log']
    del session['gold']
    return redirect('/')


app.run(debug=True)
