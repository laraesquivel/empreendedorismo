from models import db
from flask.cli import AppGroup, with_appcontext
from flask import Blueprint
import click

users_cli = AppGroup('user')

@users_cli.command("create_database")
@with_appcontext
def create_database():
            try:
                db.create_all()
                print("Conexão com o banco de dados estabelecida com sucesso!")
            except Exception as e:
                print("Erro ao conectar-se ao banco de dados:", e)

'''
@users_cli.command("create_user")
@click.argument('cpf','name','street','n_house','cep','another_reference','cellphone_zap','bairro_id')
def create_person(cpf,name,street,n_house,cep,another_reference,cellphone_zap,bairro_id):
    try:
          user = db.Pessoa(cpf,name,street,n_house,cep,another_reference,cellphone_zap,bairro_id)
          print('HTTP 201: Created{}')
    except:
          pass
'''