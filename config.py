import os.path
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True # com debug nao precisa reiniciar o servidor a cada alteração

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'storage.db')

SQLALCHEMY_TRACK_MODIFICATIONS = True

SECRET_KEY = 'chave^&%$^&%#Segura_para_formularios'