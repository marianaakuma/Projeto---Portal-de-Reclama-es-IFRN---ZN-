from flask import Flask, Blueprint, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from utils import db,lm
from controllers.usuario import bp_usuarios
from models.usuario import Usuario

# Inicializando o Flask
app = Flask(__name__)

# Configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'PIZZA'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o banco de dados
db.init_app(app)
lm.init_app(app)
migrate = Migrate(app, db)

# Registrando Blueprints
app.register_blueprint(bp_usuarios, url_prefix='/user')


# Rotas principais
@app.route('/')
def capa():
    return render_template('capa.html')

@app.route('/Sobre')
def sobre():
    return render_template('Sobre.html')

@app.route('/Volta')
def Volta():
    return render_template('volta.html')

@app.route('/biblioteca')
def biblioteca():
    livros= livros_create.query.all()
    return render_template('biblioteca.html',livros=livros)


@app.route('/Perfil')
def perfil():
    return render_template('Perfil.html')

@app.route('/suporte_create', methods=['GET', 'POST'])
def suporte_create():
    return render_template('suporte_create.html')


@app.route('/favoritos')
def favoritos():
    return render_template('favoritos.html')
# Rota para a página inicial


@app.route('/historico')
def historico():
    return render_template('historico.html')

@app.route('/configuracoes')
def configuracoes():
    return render_template('configuracoes.html')

@app.route('/inicio')
def inicio():
    return render_template('capa.html')

@app.errorhandler(401)
def acesso_negado(e):
    return render_template('acesso_negado.html'), 404

if __name__ == '__main__':
    app.run(debug=True)