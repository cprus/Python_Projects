from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'SecretKey'

@app.route('/')
def index():

    session['counter'] += 1

    return render_template("index.html")

@app.route('/ninja', methods=['POST'])
def ninja():

    session['counter'] += 2
    return redirect('/')


@app.route('/hacker', methods=['POST'])
def hacker():

    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
