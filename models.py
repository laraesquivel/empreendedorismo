from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy import Column,Integer,String, ForeignKey, Float, Boolean

db = SQLAlchemy()

class Bairro(db.Model):
    __tablename__ = "bairro"
    bairro_id = Column(Integer,primary_key = True)
    bairro_name = Column(String(100),nullable=False)
    city_name = Column(String(100),nullable=False)
    state_name = Column(String(50),nullable=False)
    location = relationship('Pessoa',backref='pessoa_location')
    act = relationship('Empresa',backref='empresa_act')

    def __repr__(self):
        return f"<Bairro {self.bairro_id} - {self.bairro_name}, {self.city_name} - {self.state_name}>"
    
    def to_dict(self):
        return { "bairro_id":self.bairro_id,"bairro_name" : self.bairro_name, "city_name":self.city_name,
            "state_name":self.state_name}


class Pessoa(db.Model):
    __tablename__ = 'pessoa'
    cpf = Column(String(11),unique=True)
    name = Column(String(120), nullable = False)
    street = Column(String(120),nullable=False)
    n_house = Column(Integer,nullable=False)
    cep = Column(String(8),nullable=False)
    another_reference = Column(String(10))
    cellphone_zap = Column(String(13))
   # autority = Column(Boolean,nullable=False)
    bairro_id = Column(Integer,ForeignKey('bairro.bairro_id'),nullable=False)
    id = Column(Integer,primary_key=True,autoincrement=True)
    possui_empresa = relationship('Empresa',backref='possui_empresa')
    faz_pedidos = relationship('Pedido',backref='faz_pedido')

    def to_dict(self):
        return {
            "cpf": self.cpf,
            "name": self.name,
            "street": self.street,
            "n_house": self.n_house,
            "cep": self.cep,
            "another_reference": self.another_reference,
            "cellphone_zap": self.cellphone_zap,
            "bairro_id": self.bairro_id,
            "id" : self.id
        }
    def __repr__(self):
        return f'<Pessoa(cpf={self.cpf}, name={self.name}, street={self.street}, n_house={self.n_house},cep={self.cep}, another_reference={self.another_reference}, cellphone_zap={self.cellphone_zap}, bairro_id={self.bairro_id})>'
    
class Empresa(db.Model):
    __tablename__ = 'empresa'
    cnpj = Column(String(14))
    name = Column(String(100))
    user_id = Column(Integer,ForeignKey('pessoa.id'),nullable=False)
    zone = Column(Integer,nullable=False)
    zone2 = Column(Integer)
    zone3 = Column(Integer)
    bairro_act = Column(Integer,ForeignKey('bairro.bairro_id'),nullable=False)

    id = Column(Integer,primary_key=True,autoincrement=True)
    tem_produtos = relationship('Produto',backref='tem_produtos')
    possui = relationship('Pedido',backref="possui_pedidos") 

    def __repr__(self):
        return f'Empresa(cnpj={self.cnpj}, cpf={self.cpf}, zone={self.zone}, zone2={self.zone2}, zone3={self.zone3}, bairro_act={self.bairro_act})'
    
    def to_dict(self):
        return {
            "cnpj": self.cnpj,
            "name" : self.name,
            "user_id": self.user_id,
            "zone": self.zone,
            "zone2": self.zone2,
            "zone3": self.zone3,
            "bairro_act": self.bairro_act,
            "id":self.id
        }

class Produto(db.Model):
    __tablename__='produto'
    id = Column(db.Integer,primary_key=True)
    name = Column(String)
    empresa_id = Column(db.String(14),ForeignKey('empresa.id'),nullable=False)
    price = Column(db.Float)

    def to_dict(self):
        return {'id': self.id, 'name':self.name, 'empresa_id': self.empresa_id, 'price': self.price}

class Pedido(db.Model):
    __tablename__='pedido'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('pessoa.id'))
    empresa_id = Column(Integer,ForeignKey('empresa.id'))
    total = Column(Float)
    possui_item = relationship('Item_Pedido',backref='item_pedido')

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "empresa_id": self.empresa_id,
            "total": self.total
        }

class Item_Pedido(db.Model):
    __tablename__='item_pedido'
    id = Column(Integer,primary_key=True)
    id_pedido = Column(Integer,ForeignKey('pedido.id'),nullable=False)
    id_produto = Column(Integer,ForeignKey('produto.id'))
    valor = Column(Float)
    quantidade = Column(Integer)

    
    def to_dict(self):
        return {
            "id": self.id,
            "id_pedido": self.id_pedido,
            "valor": self.valor,
            "quantidade": self.quantidade
        }

class Session(db.Model):
    __tablename__='session'
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(String(11),ForeignKey("pessoa.id"))
    senha = Column(String(100))
    token = Column(String(200))

    def to_dict(self):
        return{
            "id":self.id,
            "user_id":self.user_id,
            "senha":self.senha,
            "token":self.token
        }
