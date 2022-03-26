from flask import Flask, redirect, session, url_for, render_template, request
from app.auth.auth import auth_blueprint
from app.auth.user import user_blueprint
from app.controller.controller import controller_blueprint
from app.data.data import data_blueprint
from app.payload.payload import payload_blueprint
from app.views.views import views_blueprint


app = Flask(__name__)
session['loggedIn'] = 0
session['context'] = redirect(url_for('/'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/causes')
def causes():
    return render_template('causes.html')


@app.route('/causes-single')
def causesSingle():
    return render_template('causes-single.html')


app.register_blueprint(auth_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(controller_blueprint)
app.register_blueprint(data_blueprint)
app.register_blueprint(payload_blueprint)
app.register_blueprint(views_blueprint)

if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True)
