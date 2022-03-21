from flask import Flask, redirect, url_for, render_template, request
from app.auth.auth import auth_blueprint
from app.controller.controller import controller_blueprint
from app.data.data import data_blueprint
from app.payload.payload import payload_blueprint
from app.views.views import views_blueprint

app = Flask(__name__)

app.register_blueprint(auth_blueprint)
app.register_blueprint(controller_blueprint)
app.register_blueprint(data_blueprint)
app.register_blueprint(payload_blueprint)
app.register_blueprint(views_blueprint)

if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True)