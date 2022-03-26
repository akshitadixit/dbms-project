import imp
from app.data.data import DataBase as db
from flask import Blueprint, redirect, render_template, session

user_blueprint = Blueprint('user', __name__)

def edit(*args, **kwargs):
    pass

@user_blueprint.route('/profile')
def user_profile():
    # load profile
    if session['loggedIn']:
        return render_template('profile.html', values=db.users.find({'user': session['user']}))

    session['context'] = redirect(render_template('profile.html'))
    return redirect(render_template('login.html'))

@user_blueprint.route('/edit')
def user_profile_edit(*args, **kwargs):
    # edit params in the profile
    edit(*args, **kwargs)
    pass

@user_blueprint.route('/delete')
def user_delete():
    # delete user from db
    pass