# routes.py
import mysql.connector
import pandas as pd
from flask import session, render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from forms import RegistrationForm, LoginForm, UpdateAccountForm
from models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
    #posts = Post.query.all()
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        
        db.session.add(user)
        db.session.commit()
        registro(user)
        flash('Tu cuenta ha sido creada, ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user1 = User.query.filter_by(email=form.email.data).first()
        user = login1(form)
        print(user)
        if user and bcrypt.check_password_hash(user[3], form.password.data):
            login_user(user1, remember=form.remember.data)
            if user[4] == 'Administrador':
                return redirect(url_for('admin'))
            elif user[4] == 'Empleados':
                return redirect(url_for('empleados'))
            elif user[4] == 'usuarios':
                return redirect(url_for('muestra'))
        else:
            flash('Login inválido. Verifica correo y contraseña.', 'danger')
    return render_template('login.html', form=form)

@app.route("/admin")
def admin():
    return render_template('admin.html')
@app.route("/empleados")
def empleados():
    return render_template('empleados.html')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Tu cuenta ha sido actualizada!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', form=form)

@app.route('/muestra', methods=['GET', 'POST'])
def muestra():
    return render_template('muestra.html')

def registro(user=current_user):
    bd = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'projectciber'
    )

    mycursor = bd.cursor()
    query=f"insert into employees(NameEmploy,ApellidoEmploy,EmailEmploy, Password, IdRoles) values (%s,%s,%s,%s,%s);"
    val = (user.username,user.username,user.email,user.password,3)
    mycursor.execute(query,val)
    bd.commit()
    print(bd)
    return render_template('muestra.html')


def login1(form):
    bd = mysql.connector.connect(
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'projectciber'
    )
    mycursor = bd.cursor()
    val = form.email.data
    query=f"SELECT e.NameEmploy,e.ApellidoEmploy, e.EmailEmploy,e.Password,r.RolName FROM employees as e join roles as r on r.IdRoles = e.IdRoles WHERE EmailEmploy='{val}';"
    
    mycursor.execute(query)
    a =  mycursor.fetchone()
    if a:
        return a
