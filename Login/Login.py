from flask import Blueprint, render_template, request, redirect, url_for
from database import db, usuarios
from flask_login import login_user

login_blueprint = Blueprint('login', __name__, template_folder='templates')

@login_blueprint.route('/login', methods=['GET'])
def pagina_login():
    return render_template('login/login.html')

@login_blueprint.route('/login', methods=['POST'])
def user_login():
    email = request.form['email']
    senha = request.form['password']
    
    # Buscar o usuário pelo email
    user = usuarios.query.filter_by(email=email).first()
    
    # Verificar se o usuário existe e se a senha está correta
    if user and user.senha == senha:  # Substitua pela lógica real de verificação de senha
        login_user(user)  # Requer que você configure Flask-Login corretamente
        return redirect(url_for('home.pagina_home'))  # Redireciona para a página inicial após o login bem-sucedido
    else:
        # Redireciona de volta para a página de login com uma mensagem de erro
        return redirect(url_for('login.pagina_login'))  # Você pode adicionar uma mensagem de erro na URL ou usar uma variável de sessão para isso

# Nota: Adicione um método para logout, se necessário, e outras funcionalidades relacionadas ao login.
