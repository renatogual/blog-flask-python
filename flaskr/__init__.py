# O serviço __init__.py é duplo: conterá a fábrica de aplicativos e 
# informa ao Python que o flaskr diretório deve ser tratado como um pacote.
import os
from flask import Flask

def create_app(test_config=None):
    #Cria e configura o app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        #carrega a configuração da instância, se existir, quando não estiver testando
        app.config.from_pyfile('config.py', silent=True)
    else:
        #carrega a configuração de teste se aprovada
        app.config.from_mapping(test_config)

    #verifica se a pasta da instância existe 
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)
    
    return app