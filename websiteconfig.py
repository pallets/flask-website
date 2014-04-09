import os

_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = False

SECRET_KEY = 'testkey'
DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'flask-website.db')
DATABASE_CONNECT_OPTIONS = {}
ADMINS = frozenset(['http://lucumr.pocoo.org/'])

WHOOSH_INDEX = os.path.join(_basedir, 'flask-website.whoosh')
DOCUMENTATION_PATH = os.path.join(_basedir, '../flask/docs/_build/dirhtml')

del os
