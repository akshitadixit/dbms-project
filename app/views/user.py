import pprint
from app.data.data import DataBase as db
from flask import Blueprint, redirect, render_template, session, url_for

user_blueprint = Blueprint('user', __name__, url_prefix='/user')


def edit(*args, **kwargs):
    pass


@user_blueprint.route('/profile')
def user_profile():
    # load profile
    if session['loggedIn']:
        user = db.users.find({'username': session['user']},{'_id': 0, 'password': 0, 'email': 1})
        print([x for x in user])
        orgs = db.orgs.find({'user': user})
        if orgs:
            print([x for x in orgs])
        return render_template('profile.html', profile=user)

    session['context'] = 'profile'
    return redirect(url_for('login'))


@user_blueprint.route('/edit')
def user_profile_edit(*args, **kwargs):
    # edit params in the profile
    edit(*args, **kwargs)
    pass


@user_blueprint.route('/delete')
def user_delete():
    # delete user from db
    pass
