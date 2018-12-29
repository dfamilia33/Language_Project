# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 13:49:31 2018

@author: famild
"""
from flask import Flask, session
from config import Config
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
#migrate = Migrate(app, db)

from app import routes, models



#app.secret_key = 'your secret'
#app.config['SESSION_TYPE'] = 'filesystem'

if __name__ == '__main__':
  app.run(host='0.0.0.0')
    