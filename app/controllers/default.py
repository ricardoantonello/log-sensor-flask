from flask import render_template, flash, redirect, url_for
from app import app # from app=modulo import app=variavel em __init__ do modulo principal
from app import db, lm
from flask_login import login_user, logout_user, login_required

from app.models.forms import LoginForm
from app.models.tables import User

from Sensor import Sensor

@lm.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route('/')
@app.route('/index')
@app.route('/index/')
def index():
  s = Sensor()
  return render_template('index.html', sensor=s, active="index") # busca por padrao na pasta templates

@app.route('/config')
@app.route('/config/')
def config():
  return render_template('config.html', active="config") 

@app.route('/sobre')
@app.route('/sobre/')
def sobre():
  return render_template('sobre.html', active="sobre") 

@app.route('/login', methods=["GET", "POST"])
def login():
  form = LoginForm()
  if form.validate_on_submit():
      user = User.query.filter_by(username=form.username.data).first()
      if user and user.password == form.password.data:
          login_user(user)
          flash('Logado com sucesso! ;)')
          return redirect(url_for('index'))
      else:
          flash('Login falhou!')
  return render_template('login.html', form=form, active="login") 

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Usuário fez logout com sucesso!')
    return redirect(url_for('index'))

#TESTES DE CRUD
@app.route("/teste/<info>")
@app.route("/teste", defaults={"info":None})
def teste(info):
  r = User.query.filter_by(username="rica").all()
  print(r)
  #i = User('rica','1234','ricardo antonello','ricardo@antonello.com.br')
  #db.session.add(i)
  #db.session.commit()
  return 'ok'
  
  

#INFORMACOES E TESTES
#@app.route('/index/id:var') # forca conversao do argumento para inteiro
#@app.route('/index/', methods=['GET']) # filtra o tipo de requisicao HTTP
@app.route('/test' , defaults={'name': None})
@app.route('/test/', defaults={'name': None})
@app.route('/test/<name>')
def test(name):
  if name:
    return 'Olá, %s!' % name  
  else:
    return 'Olá Sr. Anônimo!'
