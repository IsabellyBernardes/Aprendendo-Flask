from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Crie uma instância da aplicação Flask
app = Flask(__name__)
app.config.from_object('config')

#app é a instância, Flask é a classe e name será a variável
#name sinaliza que tipo de arquivo está sendo executado
# Configure a URI do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'

# Crie uma instância do SQLAlchemy e do Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importe os controladores depois da configuração da aplicação
from app.controllers import default




