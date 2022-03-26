from crypt import methods
from flask_login import login_user, logout_user, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request
from app.data.data import DataBase as db

auth_blueprint = Blueprint('auth', __name__)


def signup(name, email, pwd, redirect=redirect('../../index')):
    flag = db.users.find_one({"name": name, "email": email, "password": pwd})
    if flag:
        return render_template('signup.html', msg="User already exists!")

    db.users.insert_one({'username': name, 'email': email, 'password': pwd})
    return login(email=email, pwd=pwd, redirect=redirect)


def login(email, pwd, redirect=redirect('../../index')):
    flag = db.users.find_one({"email": email, "password": pwd})
    # email-pwd login
    if flag:
        session['loggedIn':1, 'user':flag['username']]
        return redirect

    else:
        flag = db.users.find_one({"username": email, "password": pwd})
        # username-pwd login
        if flag:
            session['loggedIn':1, 'user':flag['username']]
            return redirect

    return redirect(render_template('login.html', msg='No user found, check your credentials'))


@auth_blueprint.route("/signup", methods=['GET', 'POST'])
def signup_route():
    if session['loggedIn']:
        # if user is already logged in, do nothing
        return session['context']

    if request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('email')
        pwd = request.form.get('pwd')
        context = session['context']
        return signup(name, email, pwd, context)

    return render_template('404.html')


@auth_blueprint.route("/login", methods=['GET', 'POST'])
def login_route():
    if session['loggedIn']:
        # if user is already logged in, do nothing
        return session['context']

    if request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('email')
        pwd = request.form.get('pwd')
        context = session['context']
        return signup(name, email, pwd, context)

    return render_template('404.html')
