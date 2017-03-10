from flask import Flask, render_template, session, redirect, request 
import random

app = Flask(__name__)
app.secret_key = 'shhhh'

@app.route('/')
def index():
    session['gold'] = 0
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def process_money():
    if request.form['building'] == 'farm':
        gold = random.randrange(10, 21)
        session['gold'] = gold + session['gold']
    if request.form['building'] == 'cave':
        gold = random.randrange(5, 11)
        session['gold'] = gold + session['gold']
    if request.form['building'] == 'house':
        gold = random.randrange(2, 5)
        session['gold'] = gold + session['gold']
    if request.form['building'] == 'casino':
        gold = random.randrange(-50, 50)
        session['gold'] = gold + session['gold']
        # gold = session['gold']
    
    return render_template('index.html', gold=gold)###is the gold variable here needed?###

app.run(debug=True)