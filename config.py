
import os


SECRET_KEY = os.urandom(32)
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG=True

SQLALCHEMY_DATABASE_URI='postgresql://yxvwznvt:L20buLJs730v865TPQE7LZKEK3_l_YoM@surus.db.elephantsql.com/yxvwznvt'

SQLALCHEMY_TRACK_MODIFICATIONS = False
