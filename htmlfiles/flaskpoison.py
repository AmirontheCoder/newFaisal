# app.py

from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    due_date = db.Column(db.DateTime, nullable=False)

@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            error = 'Invalid username or password'
            return render_template('login.html', error=error)
    else:
        return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' in session:
        user_id = session['user_id']
        tasks = Task.query.filter_by(user_id=user_id).all()
        return render_template('dashboard.html', tasks=tasks)
    else:
        return redirect(url_for('login'))

@app.route('/task/new', methods=['GET', 'POST'])
def new_task():
    if 'user_id' in session:
        if request.method == 'POST':
            user_id = session['user_id']
            title = request.form['title']
            description = request.form['description']
            due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')
            task = Task(user_id=user_id, title=title, description=description, due_date=due_date)
            db.session.add(task)
            db.session.commit()
            return redirect(url_for('dashboard'))
        else:
            return render_template('new_task.html')
    else:
        return redirect(url_for('login'))

@app.route('/task/<int:task_id>/edit', methods=['GET', 'POST'])
def edit_task(task_id):
    if 'user_id' in session:
        task = Task.query.get_or_404
