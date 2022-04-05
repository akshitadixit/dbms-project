from flask_pymongo import PyMongo
from flask import Blueprint
from dotenv import dotenv_values
import pymongo

# for general data of the application

data_blueprint = Blueprint('data_blueprint', __name__)

__config = dotenv_values(".env")
__mongo = pymongo.MongoClient(__config['MONGO_URI'])

DataBase = __mongo.better_bets
