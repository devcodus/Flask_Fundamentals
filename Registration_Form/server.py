from flask import Flask, render_template, session, request, redirect, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = 'shhhh'

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/registration',methods=['POST'])
def registration():
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    password = request.form['password']
    confirmpass = request.form['confirm_password']
    # name_message=""
    # confirmed password? needs to be shown too?
    
    if len(first_name) < 1:
        flash("Name field can't be empty!")
    elif not NAME_REGEX.match(request.form['first_name']):
        flash("letters only!")
    else:
        flash("Yay first name!")

    if len(request.form['last_name']) < 1:
        flash("Sorry! Last name can't be empty!")
    elif not NAME_REGEX.match(request.form['last_name']):
        flash("letters only!")
    else:
        flash("Yay last name!")

#### is str.isalpha() preferable or 
# is NAME_REGEX good for exam time purposes?
###

    # if len(request.form['password']) < 8:
    #     flash("Sorry, your password must be at least 8 charcters!")
    # else:
    #     flash("Nice password!")

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")

    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")

    else:
        flash("Success!")

    if len(password) < 8:
        flash("Sorry, your password must be at least 8 charcters!")
    elif password == confirmpass:
        flash("Yay matching passwords!")
    else:
        flash("passwords don't match :(")

    return redirect('/')
    
    # render_template('registration.html', email=email, first_name=first_name, last_name=last_name, password=password)


app.run(debug=True)