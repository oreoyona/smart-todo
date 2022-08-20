
import os


SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG=True

SQLALCHEMY_DATABASE_URI='postgresql://postgres:1234@localhost:5432'

SQLALCHEMY_TRACK_MODIFICATIONS = False
