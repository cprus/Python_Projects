from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/results', methods=['POST'])
def create_user():
    if len(request.form['name']) < 1 or len(request.form['description']) < 1 :
        flash("Please fill out all fields")
        return redirect('/')
    else:
        if len(request.form['description']) > 120:
            flash("Comment must be less than 120 characters.")
            return redirect('/')
        else:
            return render_template("results.html", name = request.form['name'], location = request.form['dojolocation'], language = request.form['favoritelanguage'], desc = request.form['description'])



@app.route('/', methods=['GET'])
def returnindx():
     return render_template("index.html")
app.run(debug=True)
