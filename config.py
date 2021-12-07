import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'lil secret key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:MyNewPass@localhost/kbsu_app_db'
