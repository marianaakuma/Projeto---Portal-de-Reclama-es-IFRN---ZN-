from flask import Blueprint, render_template, request, redirect, url_for, flash
from utils import db, lm
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models.usuario import Usuario  # Certifique-se de que o modelo está correto

bp_usuarios = Blueprint("login", __name__, template_folder='templates')

@bp_usuarios.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        usuario_nome = request.form.get('usuario')
        senha = request.form.get('senha')

        # Verifica se já existe um usuário com esse nome
        if Usuario.query.filter_by(usuario=usuario_usuario).first():
            flash('Usuário já cadastrado.', 'danger')
            return redirect(url_for('login.html'))

        # Gerar hash da senha
        senha_hash = generate_password_hash(senha)

        # Criar usuário
        usuario = Usuario(usuario=usuario_nome, senha=senha_hash)

        # Salvar no banco
        db.session.add(usuario)
        db.session.commit()

        flash('Dados cadastrados com sucesso!', 'success')
        return redirect(url_for('login.login'))  # Redireciona para tela de login após cadastro

# Rota de login
@bp_usuarios.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if request.method == 'POST':
        nome = request.form.get('usuario')
        senha = request.form.get('senha')

        usuario = Usuario.query.filter_by(usuario=nome).first()

        if usuario and check_password_hash(usuario.senha, senha):
            login_user(usuario)
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('login.login'))  # ajuste para onde o usuário será redirecionado
        else:
            flash('Usuário ou senha incorretos.', 'danger')
            return redirect(url_for('login.login'))
