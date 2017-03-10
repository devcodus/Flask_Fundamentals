from flask import Flask, render_template, request, redirect, session 
import random
app = Flask(__name__)
app.secret_key = 'shhhh'




@app.route('/',methods=['POST'])
def index():
    num = random.randrange(0, 101)
    session['num'] = num

    return render_template('index.html')

@app.route('/result',methods=['POST'])
def result():
    num = session['num']
    message = ""
    session['guess'] = request.form['html_guess']
    guess = int(session['guess'])
    # if 'num' not in session:
    
    if guess == num:
        message =  num, "was the number!"
        session.pop('num')
        return render_template('index.html', message=message)    
    elif guess < num:
        message = "Too Low!"
        return render_template('index.html', message=message)    
    elif guess > num:
        message = "Too High!"
        return render_template('index.html', message=message)    

app.run(debug=True)