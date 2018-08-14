# -*- coding: utf-8 -*-
#from app import app # from app=modulo import app=variavel apontando pro flask
from app import manager # com o flask_script o manager é que executa o run()

if __name__ == '__main__':
    manager.run()
