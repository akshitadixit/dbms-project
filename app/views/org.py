from app.data.data import DataBase as db
from flask import Blueprint, redirect, render_template, request, session, url_for

organisation_blueprint = Blueprint('organisation', __name__, url_prefix='/org')


def edit(*args, **kwargs):
    pass


@organisation_blueprint.route('/<org>/profile')
def org_profile(org):
    # load profile
    session['context'] = 'org.org_profile'
    return render_template('organisation.html', org=db.orgs.find_one({'name': org}))


@organisation_blueprint.route('/edit')
def user_profile_edit(*args, **kwargs):
    # edit params in the profile
    edit(*args, **kwargs)
    pass


@organisation_blueprint.route('/delete', methods=['DELETE'])
def org_delete():
    # delete org from db
    pass


@organisation_blueprint.route('/apply')
def org_apply():
    if session['loggedIn']:
        return render_template('org_application.html')

    return redirect(url_for('login'))


@organisation_blueprint.route('/create', methods=['GET', 'POST'])
def org_create():
    if request.method == 'POST':
        name = request.form.get('orgname')
        email = request.form.get('orgmail')
        description = request.form.get('description')
        context = session['context']

        db.orgs.insert_one(
            {'user': session['user'], 'name': name, 'email': email, 'description': description})
        return render_template('organisation.html', org={'name': name, 'email': email, 'description': description})

    return redirect(url_for(session['context']))
