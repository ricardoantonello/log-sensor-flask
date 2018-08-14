# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager
from Sensor import Sensor

app = Flask(__name__)
app.config.from_object('config') # config nao tem o .py no final

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

lm = LoginManager()
lm.init_app(app)

#instacia o objeto para centralizar a leitura de sensores
sensor = Sensor()
print(sensor.getData(1))
print(sensor.getData(2))
print(sensor.getData(3))

from app.models import tables, forms
from app.controllers import default


