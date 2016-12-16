from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, flash, url_for, redirect, render_template, abort

app = Flask(__name__)

app.config.from_pyfile('app.cfg')

web_root = "/web/"

@app.route(web_root)
def index():
    return redirect(web_root+ "login")

@app.route(web_root + "login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        passwd = request.form['password']
    return render_template('login.html', error=error)