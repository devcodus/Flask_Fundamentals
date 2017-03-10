from flask import Flask, render_template, session

app = Flask(__name__)

app.secret_key = 'shhh'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    return render_template('index.html')


app.run(debug=True)