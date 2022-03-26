from flask_pymongo import PyMongo
from flask import Blueprint
from dotenv import dotenv_values

# for general data of the application

data_blueprint = Blueprint('data_blueprint', __name__)

__config = dotenv_values(".env")
data_blueprint.config['MONGO_URI'] = __config['MONGO_URI']
__mongo = PyMongo(data_blueprint)

DataBase = __mongo.db
