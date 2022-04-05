from dotenv import dotenv_values
from app.views.views import views_blueprint
from app.payload.payload import payload_blueprint
from app.data.data import data_blueprint
from app.controller.controller import controller_blueprint
from app.views.user import user_blueprint
from app.views.org import organisation_blueprint
from app.auth.auth import auth_blueprint
from flask import Flask, redirect, session, url_for, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = dotenv_values(".env")['SECRET_KEY']
app._static_folder = 'static'


@app.route('/')
def index():
    session['loggedIn'] = 0
    session['context'] = 'home'
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html', msg=request.args.get('msg'))


@app.route('/signup')
def signup():
    return render_template('signup.html', msg=request.args.get('msg'))


@app.route('/about')
def about():
    session['context'] = 'about'
    return render_template('about.html')


@app.route('/contact')
def contact():
    session['context'] = 'contact'
    return render_template('contact.html')


@app.route('/gallery')
def gallery():
    session['context'] = 'gallery'
    return render_template('gallery.html')


@app.route('/causes')
def causes():
    session['context'] = 'causes'
    return render_template('causes.html')


@app.route('/causes-single')
def causesSingle():
    session['context'] = 'causes-single'
    return render_template('causes-single.html')


app.register_blueprint(auth_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(organisation_blueprint)
app.register_blueprint(controller_blueprint)
app.register_blueprint(data_blueprint)
app.register_blueprint(payload_blueprint)
app.register_blueprint(views_blueprint)

if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True)
