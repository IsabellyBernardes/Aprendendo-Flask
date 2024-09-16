from app import db

class Usuario(db.Model):
    __tablename__= "usuarios"
    
    id= db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    telefone = db.Column(db.String)
    email = db.Column(db.String, unique=True, NULL=False)
    senha = db.Column(db.String, NULL=False)
    
    def __init__(self, nome, telefone, email, senha):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.senha = senha
        
    def __repr__(self) -> str:
        return "<User %r>" % self.nome
    
    
    
class Imoveis(db.Model):
    __tablename__= "imoveis"
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeingKey('usuario.id'))
    endereco = db.Column(db.String)
    tipo_imovel = db.Column(db.String)
    area = db.Column(db.Decimal)
    data_registro = db.Column(db.DateTime)
    
    usuario = db.relationship('Usuario', foreing_keys= usuario_id)
    
    def __init__(self, usuario_id, endereco, tipo_imovel, area, data_registro):
        self.usuario_id = usuario_id
        self.endereco = endereco
        self.tipo_imovel = tipo_imovel
        self.area = area
        self.data_registro = data_registro
        
    def __repr__(self) -> str:
        return "<Imovel %r>" % self.id
    
    
    
    
class Candidatura(db.Model):
    __tablename__ = "Candidaturas"
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeingKey('usuario.id'))
    imovel_id = db.Column(db.Integer, db.ForeingKey('usuario.id'))
    data_candidatura = db.Column(db.DateTime)
    status = db.Column(db.String)
    
    usuario = db.relationship('Usuario', foreing_keys= usuario_id)
    imovel = db.relationship('Imovel', foreing_keys= imovel_id)
    
    def __init__(self, usuario_id, imovel_id, data_candidatura, status):
        self.usuario_id = usuario_id
        self.imovel_id = imovel_id
        self.data_candidatura = data_candidatura
        self.status = status
        
    def __repr__(self) -> str:
        return "<Candidatura %r>" % self.id
    
    
    
    
class Bonus(db.Model):
    __tablename__ = "Bônus"
    
    id = db.Column(db.Integer, primary_key= True)
    candidatura_id = db.Column(db.Interger, db.ForeingKey('usuario.id'))
    valor = db.Column(db.Decimal)
    data_concessao = db.Column(db.DateTime)
    
    candidatura = db.relationship('Candidatura', foreing_keys= candidatura_id)
    
    def __init__(self, candidatura_id, valor, data_concessao):
        self.candidatura_id = candidatura_id
        self.valor = valor
        self.data_concessao = data_concessao
        
    def __repr__(self) -> str:
        return "<Bonus %r>" % self.id