from flask import render_template
from rnnsimple import jointslu
from app import app
from flask import request

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST' :
        sentence = request.form['sentence']
    else :
        sentence = 'flight from denver to boston'
    print sentence
    output = jointslu.test(sentence)
    keys = ['fromloc', 'toloc', 'start_date', 'start_time', 'end_date', 'end_time']
    return render_template("about.html", sentence=sentence, output=output, keys=keys)