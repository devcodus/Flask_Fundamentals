from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/result',methods=['POST'])
def users():
    name = request.form['name_text']
    location = request.form['dojo_location']
    language = request.form['favorite_language']
    comment = request.form['comment']
    return render_template('result.html', name=name, location=location, language=language, comment=comment)


app.run(debug=True)