import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'lil secret key'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://kakmmddvxvkbxf:cf5678d94f4cb3e49473c53db8a9849513c63184caa831a356746c807e810e95@ec2-52-48-159-67.eu-west-1.compute.amazonaws.com:5432/d1svii7mhlo8r'
