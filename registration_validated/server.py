from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/results', methods=['POST'])
def submit():

    if len(request.form['email']) < 1 or len(request.form['name']) < 1 or len(request.form['password']) < 1 or len(request.form['conpassword']) < 1 :
        flash("Please fill out all fields")
        return redirect('/')
    else:
        if str.isalpha(str(request.form['name'])) == False:
            flash("Please use only letters in your name.")
            return redirect('/')
        else:
            if len(request.form['password']) < 8:
                flash("Password must be longer than 8 characters")
                return redirect('/')
            else:
                if not EMAIL_REGEX.match(request.form['email']):
                    flash("Invalid Email Address!")
                    return redirect('/')
                else:
                    if request.form['password'] != request.form['conpassword']:
                        flash("Passwords do not match")
                        return redirect('/')
                    else:
                        flash("Thanks for submitting your information!")


    return redirect('/')
app.run(debug=True)
