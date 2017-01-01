from flask import Flask
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, flash, url_for, redirect, render_template, abort

app = Flask(__name__)

app.config.from_pyfile('app.cfg')
db = SQLAlchemy(app)

from app.models.user_model import Users
db.create_all()

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
        if username == 'admin' and passwd == 'admin':
            return render_template('index.html')
        else:
            user = Users.query.filter_by(username = username).first()
            if not user or not user.verify_password(passwd):
                return "Invalid username or password!"
            return render_template('index.html')
    return render_template('login.html', error=error)

@app.route(web_root + "index", methods=['GET'])
def get_dashboard():
    return render_template('index.html')

@app.route(web_root + "users", methods=['GET'])
def get_users():
    return render_template('users.html',
        users=Users.query.order_by(Users.created_at.desc()).all()
    )
@app.route('/new', methods=['GET', 'POST'])
def new():
    return render_template('new.html')