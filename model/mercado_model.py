from config import db

class Mercado(db.Model):
    __tablename__ = 'mercado'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    cnpj = db.Column(db.String(20))
    email = db.Column(db.String(100))
    celular = db.Column(db.String(20))
    senha = db.Column(db.String(20))
    status = db.Column(db.Boolean)

    def __init__(self, nome, cnpj, email, celular, senha, status):
        self.nome = nome
        self.cnpj = cnpj
        self.email = email
        self.celular = celular
        self.senha = senha
        self.status = status

    def to_dic(self):
        return {"id": self.id, "nome": self.nome, "cnpj": self.cnpj, "email": self.email, "celular": self.celular, "status": self.status}
    
class MercadoNaoEncontrado(Exception):
    pass
    
def obter(id):
    mercado = Mercado.query.get(id)
    if not mercado:
        raise MercadoNaoEncontrado(f"Mercado com ID {id} não foi encontrado.")
    return mercado.to_dic()

def listar():
    mercados = Mercado.query.all()
    return [mercado.to_dic() for mercado in mercados]

def salvar(dic):
    mercado = Mercado(nome = dic["nome"], cnpj = dic["cnpj"], email = dic["email"], celular = dic["celular"], senha= dic["senha"], status= dic["status"] )
    db.session.add(mercado)
    db.session.commit()

def alterar(dic):
    mercado = Mercado.query.get(dic["id"])
    if not mercado:
        raise MercadoNaoEncontrado(f"Mercado com ID {id} não foi encontrado.")
    mercado.nome = dic["nome"]
    mercado.cnpj = dic["cnpj"]
    mercado.email = dic["email"]
    mercado.celular = dic["celular"]
    mercado.senha = dic["senha"]
    mercado.status = dic["status"]

    db.session.commit()

def excluir(id):
    mercado = Mercado.query.get(id)
    if not mercado:
        raise MercadoNaoEncontrado(f"Mercado com ID {id} não foi encontrado.")
    db.session.delete(mercado)
    db.session.commit()