import os
basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
# print(basedir)

SERVICE_NAME = 'bitcoin-margin'

class BaseConfig(object):
    """Base configuration."""
    SERVICE_NAME = SERVICE_NAME
    PORT = 3000
    SECRET_KEY = os.getenv('SECRET_KEY', 'this is secret key but not setting! please set the secret key')
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SIJAX_STATIC_PATH = os.path.join('.', os.path.dirname(__file__), 'static/js/sijax/')
    SIJAX_JSON_URI = '/static/js/sijax/json2.js'

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    HOST = 'localhost'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(os.path.join(basedir, 'dev-{0}.db'.format(SERVICE_NAME)))

class ProductionConfig(BaseConfig):
    """Production configuration."""
    HOST = '0.0.0.0'
    SECRET_KEY = os.getenv('SECRET_KEY', 'this is secret key but not setting! please set the secret key')
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(os.path.join(basedir, '{0}.db').format(SERVICE_NAME))
