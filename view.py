from flask import Blueprint, request, jsonify, make_response
import models

bp = Blueprint('controller',__name__)

@bp.route('/')
def index():
    return "Eu sou a aplicação de empreendedorismo 1"

@bp.route('/CadastrarBairro',methods=['POST'])
def cadastrar_bairro():
    data = request.get_json()
    bairro = models.Bairro(bairro_id=int(data['bairro_id']),bairro_name=data['bairro_name'],city_name=data['city_name'],
                           state_name=data['state_name'])
    try:
        models.db.session.add(bairro)
        models.db.session.commit()
        return make_response(jsonify({'ok':True}),201)
    except Exception as e:
        print(e)
        return make_response(jsonify({'ok':False,'erro':e}),500)

@bp.route('/bairros',methods=['GET'])
def get_bairros():
    try:
        bairros = models.db.session.execute(models.db.select(models.Bairro).order_by(models.Bairro.bairro_id)).scalars()
        bairros_dict = [bairro.to_dict() for bairro in bairros]
        print(bairros_dict)
        return make_response(jsonify(bairros_dict),200)
    except Exception as e:
        print(e)
        return make_response(e,500)
        
@bp.route('/CadastrarPessoa',methods=['POST'])
def cadastrar_user():
    data = request.get_json()
    user = models.Pessoa(cpf=data['cpf'],name=data['name'],street=data['street'],n_house=data['n_house'],
                         cep=data['cep'],another_reference=data['another_reference'],
                         cellphone_zap=data['cellphone_zap'],
                         bairro_id=data['bairro_id'],email=data['email'])
    try:
        models.db.session.add(user)
        models.db.session.commit()
        user_id = models.db.session.execute(models.db.select(models.Pessoa.id).where(models.Pessoa.cpf==data['cpf'])).fetchone()[0]
        session = models.Session(user_id=user_id,senha=data['senha'])
        models.db.session.add(session)
        models.db.session.commit()
        return make_response(jsonify(data),201)
    except Exception as e:
        print(e)
        e = "Nao foi possivel realizar cadastro"
        return make_response(e,500)
    
@bp.route('/getUsers',methods=['GET'])
def get_users():
    try:
        users = models.db.session.execute(models.db.select(models.Pessoa).order_by(models.Pessoa.name)).scalars()
        users_dict = [user.to_dict() for user in users]
        return make_response(jsonify(users_dict),200)
    except Exception as e:
        return make_response(e,500)
@bp.route('/CadastrarEmpresa',methods=['POST'])
def cadastrar_empresa():
    data = request.get_json()
    try:
        user_id = models.db.session.execute(models.db.select(models.Pessoa.id).where(data['cpf']==models.Pessoa.cpf)).fetchone()
        print(user_id)
        empresa = models.Empresa(cnpj=data['cnpj'],name=data['name'],user_id = user_id[0], zone=data['zone'], zone2=data['zone2'],
                            zone3=data['zone3'], bairro_act=data['bairro_act'])
        models.db.session.add(empresa)
        models.db.session.commit()
        return make_response("Created!",201)
    except Exception as e:
        return make_response(str(e),500)
@bp.route('/empresas',methods=['GET'])
def get_empresas():
    try:
        empresas = models.db.session.execute(models.db.select(models.Empresa).order_by(models.Empresa.name)).scalars()
        empresas_dict = [empresa.to_dict() for empresa in empresas]
        return make_response(jsonify(empresas_dict),200)
    except Exception as e:
        return make_response(e,500)
@bp.route('/empresas/<id>',methods=['GET'])
def get_empresa(id):
    try:
        empresas = models.db.session.execute(models.db.select(models.Empresa).where(models.Empresa.user_id==id).order_by(models.Empresa.name)).scalars()
        empresas_dict = [empresa.to_dict() for empresa in empresas]
        return make_response(jsonify(empresas_dict),200)
    except Exception as e:
        return make_response(str(e),500)

@bp.route('/CadastrarProduto',methods=['POST'])
def cadastrar_produto():
    data = request.get_json()
    try:
        produto = models.Produto(id=int(data["id"]),name=data['name'], empresa_id=int(data['empresa_id']), price=float(data['price']))
        models.db.session.add(produto)
        models.db.session.commit()
        return make_response("Created",201)

    except Exception as e:
        return make_response(str(e),500)
    
#id da empresa
@bp.route('/produtos/<id_empresa>',methods=['GET'])
def get_produtos(id_empresa):
    try:
        produtos = models.db.session.execute(models.db.select(models.Produto).where(models.Produto.empresa_id==int(id_empresa))).scalars()
        produtos_dict = [produto.to_dict() for produto in produtos]
        return make_response(jsonify(produtos_dict),200)
    except Exception as e:
        return make_response(str(e),500)

@bp.route('/categoria/<id_categoria>',methods=['GET'])
def get_empresas_by_zone(id_categoria):
    pass

@bp.route('/login',methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    senha = data['senha']
    try:
        user_id = models.db.session.execute(models.db.select(models.Pessoa.id).where(models.Pessoa.email==email)).fetchone()
        if type(user_id) is not None:
            print(user_id[0])
            senha_t = models.db.session.execute(models.db.select(models.Session.senha).where(models.Session.user_id==user_id[0])).fetchone()
            print(senha_t)
            print(senha_t[0])
            if ( not (senha_t is None) and senha_t[0]==senha):
                return make_response("Login realizado com sucesso",200)
            else:
                return make_response("Senha incorreta",401)
        else:
            return make_response("Email não cadastrado, verifique o seu email",400)
    except Exception as e:
        return make_response(str(e),500)

