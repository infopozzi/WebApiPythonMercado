import os

from config import app,db

from routes.mercado_routes import mercado_blueprint

app.register_blueprint(mercado_blueprint, url_prefix = "/mercado")

#instanciar tabelas na ordem correta para não dar problema nas chaves
from model.mercado_model import Mercado

with app.app_context():
    db.create_all()

if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )
