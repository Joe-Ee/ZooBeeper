from flask import Flask, redirect, render_template, request, abort, url_for, session, url_for, flash, send_from_directory
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
#College swe project which I am using as base for this functionality
###https://github.com/dacs-01/picnetic/blob/main/app.py

##FIND A PACKAGE THAT USES MONGO INSTEAD OF SQL
app = Flask(__name__)
@app.route('/animal/1')
def getAnimal():
    if request.method == "GET":
        return render_template('birdPage.html')

 

@app.route('/animal/new')
def createAnimal():
    if request.method == "GET":
        return render_template('newBird.html')

@app.route('/')
def index():
    return render_template('index.html')

#
@app.route('/account/1')
def account():
    return render_template('myAccount.html')

#@app.post('/new_animal')
#def newAnimal():
#    return
#
#@app.route("/edit_animal")
#def editAnimal():
#    return
#
#@app.route("/edit_animal/{id}")
#def editAnimal():
#    return
#
#@app.route("/delete_animal")
#def deleteAnimal():
#    return



if __name__ == '__main__':
    app.run(debug=True)