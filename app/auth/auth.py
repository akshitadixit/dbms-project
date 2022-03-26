from pprint import pprint
from flask_login import login_user, logout_user, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Blueprint, jsonify, redirect, render_template, session, url_for, request
from app.data.data import DataBase as db

auth_blueprint = Blueprint('auth', __name__)


def signup(name, email, pwd, redirect):
    flag = db.users.find_one(
        {"username": name, "email": email, "password": pwd})
    if flag:
        return url_for('signup', msg="User already exists!")

    db.users.insert_one({'username': name, 'email': email, 'password': pwd})
    return login(email=email, pwd=pwd, redirect=redirect)


def login(email, pwd, redirect):
    flag = db.users.find_one({"email": email, "password": pwd})
    print(flag, email, pwd, redirect)
    # email-pwd login
    if flag:
        session['loggedIn'] = 1
        session['user'] = flag['username']
        return url_for(redirect)

    else:
        flag = db.users.find_one({"username": email, "password": pwd})
        print(flag)
        # username-pwd login
        if flag:
            session['loggedIn'] = 1
            session['user'] = flag['username']
            return url_for(redirect)

    return url_for('login', msg='No user found, check your credentials')


@ auth_blueprint.route("/signup/auth", methods=['GET', 'POST'])
def signup_route():
    if session['loggedIn']:
        # if user is already logged in, do nothing
        return redirect(url_for(session['context']))

    if request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('email')
        pwd = request.form.get('password')
        context = session['context']
        return redirect(signup(name, email, pwd, context))

    return render_template('404.html')


@ auth_blueprint.route("/login/auth", methods=['GET', 'POST'])
def login_route():
    if session['loggedIn']:
        # if user is already logged in, do nothing
        return redirect(url_for(session['context']))

    if request.method == 'POST':
        email = request.form.get('username')
        pwd = request.form.get('password')
        context = session['context']
        return redirect(login(email, pwd, context))

    return render_template('404.html')


@ auth_blueprint.route("/logout", methods=['GET', 'POST'])
def logout_route():
    if session['loggedIn']:
        session['loggedIn'] = 0
        session['context'] = 'home'
        del session['user']
        return redirect(url_for('home'))

    return redirect(url_for(session['context']))
