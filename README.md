# log-sensor-flask (in progress, do not use!!!)
Logs sensor data (DHT11) in local data base (sqlite), visualize in browser (flask and chart.js) and backup online in firebase.

# -*- coding: utf-8 -*-
#INSTALACAO DO FLASK
#pip3 install virtualenv
#virtualenv -p python3 venv
#. venv/bin/activate
#venv/bin/pip3 install flask
#venv/bin/pip3 freeze > requirements.txt
##venv/bin/pip3 install -r requirements.txt
##__init__ precisa ter dentro da pasta de cada modulo em python

#venv/bin/pip3 install flask-sqlalchemy
#venv/bin/pip3 install flask-migrate
#venv/bin/pip3 install flask-script
#venv/bin/pip3 install flask-wtf   # é wt forms para formularios
#venv/bin/pip3 install flask-login # login depende de wt forms

#depois de instalado o flask_script os comandos sao
#python3 run.py runserver
#python3 run.py db init #apenas no inicio (pasta migrations nao deve ser alterada manualmente)
#python3 run.py db migrate 
#python3 run.py db upgrade 
#sudo apt install sqlitebrowser # para visualizar o banco de dados
#incluir arquivos do bootstrap na pasta arquivos estaticos (static)

### APENDICE Github
#Minha sugestao é criar o repositorio online, fazer o clone para baixar para a maquina local, incluir e alterar os arquivos e depois add, commit e push...
#Use git pull pra atualizar da nuvem para local em repo já criado
##Comandos
#Change the current working directory to your local project.
#git init #Initialize the local directory as a Git repository.
#git add . # Adds the files in the local repository and stages (organize) them for commit. To unstage a file, use 'git reset HEAD YOUR-FILE'.
#git commit -m "First commit" # Commits the tracked changes and prepares them to be pushed to a remote repository. To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit and add the file again.
#git remote add origin remote repository URL # Sets the new remote
#git remote -v ## Verifies the new remote URL
#git push origin master # Pushes the changes in your local repository up to the remote repository you specified as the origin
#Importing a Git repository using the command line
#git clone https://external-host.com/extuser/repo.git # cria a pasta repo.git
#cd repo.git
#git push --mirror https://github.com/ghuser/repo.git # Pushes the mirror to the new GitHub repository
#cd .. E rm -rf repo.git # apaga a pasta temporaria
