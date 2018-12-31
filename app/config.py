import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # finds app database in package else creates one
    SQLALCHEMY_DATABASE_URI = os.environ.get('sqlite:///app.db') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False